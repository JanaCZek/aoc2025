## Plan: Solve Math Worksheet Grand Total

Solve the worksheet by parsing problems, computing each result, and summing for the grand total. Use provided examples for tests, then apply the solution to both sample and full input files.

### Detailed Steps
1. **Read the input file**
   - Open `input-small.txt` and `input.txt` in `6/python-ai-2/`.
   - Example input:
     ```
     123 328  51 64 
      45 64  387 23 
       6 98  215 314
     *   +   *   +  
     ```
2. **Parse the problems**
   - Each column (ignoring spaces) is a separate problem.
   - For the example above, problems are:
     - 123 * 45 * 6
     - 328 + 64 + 98
     - 51 * 387 * 215
     - 64 + 23 + 314
   - The last row in each column gives the operation (`*` or `+`).
3. **Extract numbers and operations**
   - For each column, collect all numbers above the operation symbol.
   - Example: For the first column, numbers are 123, 45, 6 and operation is `*`.
4. **Compute each problem's result**
   - Apply the operation to all numbers in the column.
   - Example: 123 * 45 * 6 = 33210
   - Example: 328 + 64 + 98 = 490
5. **Sum all results for the grand total**
   - Add all individual results together.
   - Example: 33210 + 490 + 4243455 + 401 = 4277556
6. **Write tests in `test_main.py`**
   - Use the above examples as test cases.
   - Example test:
     ```python
     def test_example():
         assert solve([[123, 45, 6], '*']) == 33210
         assert solve([[328, 64, 98], '+']) == 490
     ```
7. **Run tests with pytest**
   - Command: `pytest c:/Projects/playground/aoc2025/6/python-ai/test_main.py -s`
   - Verify all tests pass before running on full input.
8. **Run the algorithm on the full input**
   - Parse and solve all problems in `input.txt`.
   - Print or return the grand total as the final answer.
