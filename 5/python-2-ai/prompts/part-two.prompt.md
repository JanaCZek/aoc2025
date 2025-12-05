# Task
--- Part Two ---
The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:
## Test cases
3-5
10-14
16-20
12-18
The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
## End Test cases

## Question
Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

## Answer the question

# Plan
1. The original task was updated by the section above.
2. Come up with a new plan to solve the updated task.
3. The new plan should be similar in style and format to the original plan.
4. Again use TDD and the provided test cases.
5. Finally, use the real input `input.txt` to get the answer to the question. Run the test using `pytest test_main.py -s` to print the final count of fresh ingredient IDs.