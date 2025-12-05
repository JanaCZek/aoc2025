## Plan: Solve AoC Part Two in Python

Process the fresh ingredient ID ranges, count all unique IDs considered fresh, and write tests for the solution in `5/python-ai/test_main.py`.

# Task 
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

## Important
1. New functions should be appended to the end of the file

### Steps
1. Review the format of the input data in `5/input.txt` for fresh ingredient ID ranges.
2. Design a Python function to parse ranges and count all unique fresh IDs.
3. Implement the solution and corresponding tests in `5/python-ai/test_main_part_two.py`.
4. Ensure the solution ignores the "available ingredient IDs" section per instructions.
5. Run tests using `pytest 5/python-ai/test_main_part_two.py -s` to validate correctness.

### Further Considerations
1. Confirm if input format matches the example (one range per line, or other).
2. Consider edge cases: overlapping ranges, single-value ranges, large ranges.
3. Should output be the count only, or also the list of fresh IDs?
