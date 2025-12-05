## Plan: TDD for Fresh Ingredient IDs (All in test_main.py, Iterative Loop)

Implement the solution entirely in `test_main.py` using TDD (Pytest), following the sample data and test cases in the prompt.

### Subtasks
1. **Write initial test**  
   In `test_main.py`, create a test function using the sample data from the prompt.  
   - Input: fresh ranges and available IDs.  
   - Assert: count of fresh IDs matches expected result.

2. **Implement parsing and checking logic**  
   Define all necessary functions/classes directly in `test_main.py`:  
   - Parse input into fresh ranges and available IDs.  
   - Check each available ID for freshness (inclusive, handle overlaps).  
   - Return the count of fresh IDs.

3. **Run test and confirm failure**  
   Execute the test to ensure it fails, verifying TDD workflow.

4. **Write minimal code to pass test**  
   Implement only enough logic in `test_main.py` to make the test pass.  
   - Use correct range checking and parsing.

5. **Iterate: Add new test, run, and update code**  
   Repeat steps 3 and 4 for each new test case:  
   - Add a new test (edge cases, boundaries, overlaps, spoiled IDs, etc.).  
   - Run tests and update code minimally to pass the new test.

6. **Refactor and finalize**  
   Refactor code for clarity and efficiency within `test_main.py`.  
   - Ensure all tests pass.  
   - Confirm the function answers the question.

7. **Use real input for final verification**  
   Test the final implementation with real input data to ensure correctness.
   Print the final count of fresh ingredient IDs using `pytest test_main.py -s` command.