#!/usr/bin/env python3
"""Simple Databricks client using environment variables.

Reads DATABRICKS_HOST and DATABRICKS_TOKEN from the environment and
calls the SCIM "Me" endpoint to return the current user information.

Usage:
  export DATABRICKS_HOST="https://<your-workspace>"
  export DATABRICKS_TOKEN="<your-token>"
  python3 example1/databricks_client.py

This script uses the `requests` package. Install with:
  pip install -r requirements.txt
"""

import os
import sys
import json

try:
    import requests
except Exception as e:
    print("Missing dependency 'requests'. Install with: pip install requests", file=sys.stderr)
    raise


def masked_token(token: str) -> str:
    if not token:
        return "(none)"
    if len(token) <= 8:
        return token
    return f"{token[:4]}...{token[-4:]}"


def get_current_user(host: str, token: str, timeout: int = 10):
    """Call Databricks SCIM Me endpoint and return parsed JSON on success."""
    url = host.rstrip('/') + '/api/2.0/preview/scim/v2/Me'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
    except requests.RequestException as e:
        raise RuntimeError(f"Request error: {e}") from e

    if resp.status_code == 200:
        try:
            return resp.json()
        except json.JSONDecodeError:
            raise RuntimeError("Received non-JSON response from Databricks")
    elif resp.status_code in (401, 403):
        raise RuntimeError(f"Authentication failed (status {resp.status_code}). Check your token and host.")
    else:
        raise RuntimeError(f"Databricks API error: {resp.status_code} {resp.text}")


if __name__ == '__main__':
    host = os.environ.get('DATABRICKS_HOST', '').strip()
    token = os.environ.get('DATABRICKS_TOKEN', '').strip()

    print(f"DATABRICKS_HOST = {host or '(not set)'}")
    print(f"DATABRICKS_TOKEN = {masked_token(token)}")

    if not host:
        print("Error: DATABRICKS_HOST is not set. Export it and run again.", file=sys.stderr)
        sys.exit(2)
    if not token:
        print("Error: DATABRICKS_TOKEN is not set. Export it and run again.", file=sys.stderr)
        sys.exit(2)

    try:
        user = get_current_user(host, token)
    except Exception as e:
        print(f"Failed to get current user: {e}", file=sys.stderr)
        sys.exit(1)

    print("\nCurrent user info:")
    print(json.dumps(user, indent=2))
