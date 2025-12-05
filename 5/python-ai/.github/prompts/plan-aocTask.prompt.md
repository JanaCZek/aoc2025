## Plan: Count Fresh Ingredient IDs in Python

Solve the task of counting how many available ingredient IDs are fresh, based on inclusive and possibly overlapping ranges, using a test-driven approach in Python.

# Task
The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

## Sample Input
3-5
10-14
16-20
12-18

1
5
8
11
17
32
## End sample input

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.
So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?

### Steps
1. Review [test_main.py](../5/python/test_main.py) for structure and entry points.
2. Analyze [4/python/test_main.py](../4/python/test_main.py) for reference implementation and test style.
3. Write an initial test in `test_main.py` using the sample input from the prompt.
4. Implement a function in `test_main.py` to parse ranges and IDs, and count fresh IDs.
5. Iterate: Add more tests for edge cases (overlapping ranges, single ID, etc.), refining the solution as needed.
6. Finally, use 5/input.txt to get the final answer.

### Further Considerations
1. Should the solution handle malformed input gracefully, or assume well-formed input?
2. Consider efficiency for large input files, but prioritize correctness and clarity first.
