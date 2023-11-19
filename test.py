#!/usr/bin/env python3

import os
import sys
import subprocess

def run_test(prog, input_file, output_file, mode, column_indices):
    with open(input_file, 'r') as f:
        input_data = f.read()

    cmd = [f'./prog/{prog}.py'] + column_indices
    try:
        if mode == 'stdin':
            result = subprocess.run(cmd, input=input_data, capture_output=True, text=True, check=True)
        elif mode == 'arg':
            cmd.insert(1, input_file)
            print(cmd)
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output_data = result.stdout
    except subprocess.CalledProcessError as e:
        return (False, 'ProcessError', e.stderr, None)

    try:
        with open(output_file, 'r') as f:
            expected_data = f.read()
    except FileNotFoundError:
        expected_data = ''
    
    if output_data != expected_data:
        return (False, 'OutputMismatch', output_data, expected_data)
    
    return (True, None, None, expected_data)

def main():
    test_dir = 'test'
    total_tests = 0
    passed_tests = 0
    failures = []
    
    for file in os.listdir(test_dir):
        if file.endswith('.in'):
            prog, name, _ = file.split('.')
            input_file = os.path.join(test_dir, file)
            output_file_stdin = os.path.join(test_dir, f'{prog}.{name}.out')
            output_file_arg = os.path.join(test_dir, f'{prog}.{name}.arg.out')

            # Read column indices from a separate file
            # they are stored in a file like 'csvsum.test.args'
            args_file = os.path.join(test_dir, f'{prog}.{name}.args')
            if os.path.exists(args_file):
                with open(args_file, 'r') as af:
                    column_indices = af.read().split()
            else:
                column_indices = []  # Default to empty if no args file
            
            # Run test for standard input
            total_tests += 1
            passed, reason, data, expected_data = run_test(prog, input_file, output_file_stdin, 'stdin', column_indices)
            if passed:
                passed_tests += 1
            else:
                failures.append((prog, 'stdin', reason, data, expected_data))
            
            # Run test for command-line argument
            total_tests += 1
            passed, reason, data, expected_data = run_test(prog, input_file, output_file_arg, 'arg', column_indices)
            if passed:
                passed_tests += 1
            else:
                failures.append((prog, 'arg', reason, data, expected_data))
    
    for prog, mode, reason, data, expected_data in failures:
        print(f'FAIL:     {prog} failed in {mode} mode ({reason})')
        if data is not None:
            print(f'Expected: {expected_data}')
            print(f'Got:      {data}')
    
    print(f'\nOK: {passed_tests}')
    print(f'Total: {total_tests}')
    
    if passed_tests < total_tests:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
