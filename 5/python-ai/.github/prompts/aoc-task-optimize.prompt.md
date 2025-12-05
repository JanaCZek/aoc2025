## Plan: Optimize Memory Usage in Fresh ID Counter

Optimize the count_fresh_ingredient_ids function in test_main.py to reduce memory usage, especially for large input ranges, while ensuring all tests still pass.

### Steps
1. Refactor count_fresh_ingredient_ids to avoid building a full set of all fresh IDs.
2. Parse ranges into a list of tuples and available IDs as before.
3. For each available ID, check if it falls within any range using efficient iteration.
4. Run all tests to confirm correctness and performance.

### Further Considerations
1. Consider sorting and merging ranges for faster lookup (binary search).
2. If performance is still an issue, explore interval trees or other advanced data structures.
3. Ensure edge cases (overlapping, single, none) are still handled correctly.

Let me know if you want a specific optimization approach (e.g., merge intervals, binary search, etc.) or if you want to keep it simple.
