# CS515 Project 1 Test Harness

## Author Information

- **Name:** [Jia Gao]
- **Stevens Login:** [jgao32@stevens.edu]

## Repository URL

[Public GitHub Repo](https://github.com/gj-entertain/CS515-Project-1)

## Project Overview

### Time Spent

I spent approximately 30 hours on this project, encompassing development, testing, and debugging phases.

### Testing Approach

For testing, I developed a custom script, `test.py`, which automated the testing process for both `wc.py` and `gron.py` and `csvsum.py`. This included:

- Regular tests with a variety of input cases to ensure functionality.
- Handling edge cases and erroneous inputs to test robustness.
- Continual test execution during development for consistent performance.

### Known Bugs and Issues

- Currently, there are no major unresolved bugs in the project.
- Any minor issues encountered during development have been thoroughly documented within the code.

### Resolving a Difficult Issue

- **Issue:** While developing the automated test script test.py for utility programs like `wc.py` and `gron.py` and `csvsum.py`, a challenging issue was encountered. The scripts were designed to accept a variety of command-line arguments, including file paths and specific flags. The difficulty arose in dynamically configuring test.py to correctly and flexibly pass these arguments to the utility scripts during testing. The challenge was compounded when the scripts were extended to support multiple file inputs, as the test harness needed to handle an arbitrary number of arguments in various formats.
- **Resolution:** Implementing Flexible Argument Parsing and Subprocess Handling

The solution involved several key steps and thoughtful design considerations:

1. Dynamic Argument Reading: Modified test.py to read arguments from a separate configuration file (*.args) for each test case. This approach provided the flexibility to specify any combination of arguments needed for a particular test.
2. Subprocess Command Construction: Updated the run_test function to construct the subprocess command dynamically. This included concatenating the program path with the arguments read from the configuration file. Special care was taken to handle different modes ('stdin' and 'arg') correctly.
    - In 'stdin' mode, the contents of the input file were piped directly into the program using subprocess.run.
    - In 'arg' mode, the input file's path (and any additional arguments) were passed as command-line arguments to the program.
3. Testing and Debugging: Rigorously tested the updated test.py with various combinations of arguments and input files. This involved creating multiple test cases, each with different requirements (single file, multiple files, various flag combinations).
4. Error Handling and Output Comparison: Enhanced error handling in test.py to capture and report any subprocess errors. Improved the logic for comparing the actual output of the utility scripts against the expected output, considering different argument configurations.


## Implemented Extensions

1. **Advanced `wc`: Multiple Files**
   - Enhanced `wc.py` to handle multiple file inputs, providing a total count across all files.
   - How to test them: 
        - Argument: ./prog/wc.py test/wc.foo.in test/gron.eg.in
        - STDIN: cat test/wc.foo.in test/gron.eg.in | ./prog/wc.py
    Output should be:
    4 5 21 test/wc.foo.in
    11 25 259 test/gron.eg.in
    15 30 280 total

2. **Advanced `wc`: Output Control Flags**
   - Integrated flags (`-l`, `-w`, `-c`) in `wc.py` for selective output (lines, words, characters).
   - Enabled both combined and individual use of these flags for flexible output.
   - How to test them:
        Just modify the wc.foo.args file with:
        - -lw
        - Then run the ./test.py

3. **Enhanced `gron`: Custom Base-Object Naming**
   - Modified `gron.py` to allow users to specify the base object name in the output, enhancing the readability for complex JSON structures.
   - How to test them:
        Just modify the gron.eg.args file with:
        - --obj o
        - Then run the ./test.py
