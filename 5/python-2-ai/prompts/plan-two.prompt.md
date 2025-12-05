## Plan: Count Fresh Ingredient IDs from Ranges

Process the database to count all unique ingredient IDs considered fresh by any given range, ignoring the available ingredient IDs section.

### Subtasks

#### 1. Parse fresh ingredient ID ranges from `input.txt`
1.1. Read the contents of `input.txt`.
1.2. Identify and extract all lines representing fresh ingredient ID ranges.
1.3. Parse each line into a tuple of (start, end) integers.

#### 2. Merge overlapping and adjacent ranges
2.1. Sort the list of range tuples by their start value.
2.2. Iterate through the sorted ranges, merging any that overlap or are adjacent.
2.3. Store the merged ranges in a new list.

#### 3. Generate the set of all unique fresh ingredient IDs
3.1. For each merged range, generate all IDs from start to end (inclusive).
3.2. Add each ID to a set to ensure uniqueness.
3.3. Count the total number of unique IDs in the set.

#### 4. Write and run TDD tests in `test_main.py`
4.1. Implement unit tests for parsing ranges.
4.2. Implement unit tests for merging ranges.
4.3. Implement unit tests for counting unique IDs.
4.4. Use provided test cases to verify correctness.

#### 5. Print the final count of fresh ingredient IDs using pytest
5.1. Add code to print the final count when running tests.
5.2. Run `pytest test_main.py -s` to display the result.