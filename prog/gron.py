#!/usr/bin/env python3

import sys
import json
import argparse

def gron(data, prefix='json'):
    lines = []

    def traverse(data, prefix):
        if isinstance(data, dict):
            lines.append(f"{prefix} = {{}};")
            for key, value in data.items():
                path = f"{prefix}.{key}"
                traverse(value, path)
        elif isinstance(data, list):
            lines.append(f"{prefix} = [];")
            for index, value in enumerate(data):
                path = f"{prefix}[{index}]"
                traverse(value, path)
        else:
            lines.append(f"{prefix} = {json.dumps(data)};")

    traverse(data, prefix)
    return "\n".join(sorted(lines))

def main():
    parser = argparse.ArgumentParser(description='Convert JSON to assignment statements.')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='file to read from (default: STDIN)')
    parser.add_argument('--obj', default='json', help='name of the base object (default: "json")')

    args = parser.parse_args()

    try:
        if args.file is sys.stdin:
            data = json.load(sys.stdin)
        else:
            data = json.load(args.file)
        print(gron(data, args.obj))
    except json.JSONDecodeError as e:
        sys.stderr.write(f"Error: Failed to parse JSON. {e}\n")
        sys.exit(1)
    except FileNotFoundError as e:
        sys.stderr.write(f"Error: File not found. {e}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error: An unexpected error occurred. {e}\n")
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
