#!/usr/bin/env python3

import argparse
import sys

def count_lines(words):
    return len(words.splitlines())

def count_words(words):
    return len(words.split())

def count_chars(words):
    return len(words)

def process_file(file, flags):
    text = file.read()
    lines = count_lines(text)
    words = count_words(text)
    chars = count_chars(text)
    results = []
    if 'l' in flags:
        results.append(lines)
    if 'w' in flags:
        results.append(words)
    if 'c' in flags:
        results.append(chars)
    if not flags:
        results.extend([lines, words, chars])
    return results

def main():
    parser = argparse.ArgumentParser(description='Count lines, words, and characters in a file or from STDIN.')
    parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=[sys.stdin],
                        help='files to read from (default: STDIN)')
    parser.add_argument('-l', '--lines', action='store_true', help='count lines')
    parser.add_argument('-w', '--words', action='store_true', help='count words')
    parser.add_argument('-c', '--chars', action='store_true', help='count characters')

    args = parser.parse_args()

    flags = []
    if args.lines:
        flags.append('l')
    if args.words:
        flags.append('w')
    if args.chars:
        flags.append('c')

    total = [0, 0, 0]
    for file in args.files:
        try:
            results = process_file(file, flags)
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.exit(1)

        print(' '.join(map(str, results)), end='')
        if file is not sys.stdin:
            print(f' {file.name}')
            total = [t + r for t, r in zip(total, results)]
        else:
            print('')

    if len(args.files) > 1:
        print(' '.join(map(str, total)), 'total')

    sys.exit(0)

if __name__ == "__main__":
    main()
