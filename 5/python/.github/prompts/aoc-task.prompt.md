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

# Steps
1. Come up with a plan of solving the task in Python
2. Use the file in 5/python/test_main.py to write tests for the solution and the solution itself
3. Look at how 4/python/test_main.py is implemented for reference
4. Use sample input to create tests and verify the solution works
5. Create one test first, then implement the solution to make it pass, then continue with the next test and so on