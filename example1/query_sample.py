#!/usr/bin/env python3
"""Query the sample Databricks user JSON using a simple dot-path query.

Examples:
  python3 example1/query_sample.py --query user_name
  python3 example1/query_sample.py --query repos
  python3 example1/query_sample.py --query workspace_url
"""

import argparse
import json
import os
import sys


def get_by_path(obj, path: str):
    """Resolve a dotted path like 'a.b.c' against a nested dict/list structure."""
    if path == "":
        return obj
    parts = path.split('.')
    cur = obj
    for p in parts:
        if isinstance(cur, dict):
            if p in cur:
                cur = cur[p]
            else:
                raise KeyError(f"Key '{p}' not found")
        else:
            raise KeyError(f"Cannot resolve '{p}' on non-dict object: {cur}")
    return cur


def main():
    parser = argparse.ArgumentParser(description='Query sample Databricks user JSON')
    parser.add_argument('--sample-file', '-f', default=os.path.join(os.path.dirname(__file__), 'sample_user.json'))
    parser.add_argument('--query', '-q', default='user_name', help='Dot-path query (default: user_name)')
    args = parser.parse_args()

    try:
        with open(args.sample_file, 'r') as fh:
            data = json.load(fh)
    except Exception as e:
        print(f"Failed to read sample file '{args.sample_file}': {e}", file=sys.stderr)
        sys.exit(1)

    try:
        res = get_by_path(data, args.query)
    except KeyError as e:
        print(f"Query error: {e}", file=sys.stderr)
        sys.exit(2)

    # Print JSON if result is complex, else print as string
    if isinstance(res, (dict, list)):
        print(json.dumps(res, indent=2))
    else:
        print(res)


if __name__ == '__main__':
    main()
