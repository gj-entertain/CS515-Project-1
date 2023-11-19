#!/usr/bin/env python3

import csv
import sys

def sum_csv_columns(csvfile, columns):
    reader = csv.reader(csvfile)
    sums = {col: 0 for col in columns}
    for row in reader:
        for col in columns:
            try:
                sums[col] += float(row[col])
            except (ValueError, IndexError):
                continue
    return sums

def main():
    columns = []
    input_stream = None

    if len(sys.argv) < 2:
        print("Usage: python csvsum.py <filename> <column_index_1> <column_index_2> ... OR | python csvsum.py <column_index_1> <column_index_2> ...")
        sys.exit(1)

    if len(sys.argv) == 2 or not sys.argv[1].isdigit():
        # Assume the first argument is a filename
        filename = sys.argv[1]
        try:
            input_stream = open(filename, newline='')
            columns = [int(col) for col in sys.argv[2:]]
        except ValueError:
            print("Error: Column indices must be integers.")
            sys.exit(1)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)
    else:
        # Reading from stdin
        input_stream = sys.stdin
        try:
            columns = [int(col) for col in sys.argv[1:]]
        except ValueError:
            print("Error: Column indices must be integers.")
            sys.exit(1)

    sums = sum_csv_columns(input_stream, columns)
    if input_stream != sys.stdin:
        input_stream.close()
    
    for col, sum_value in sums.items():
        print(f"Sum of column {col}: {sum_value}")

if __name__ == "__main__":
    main()
