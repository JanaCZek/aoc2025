import pytest

# Function to parse ranges and count unique fresh IDs
def count_unique_fresh_ids_from_file(filepath):
    fresh_ranges = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if '-' in line:
                start, end = map(int, line.split('-'))
                fresh_ranges.append((start, end))
    # Merge overlapping ranges
    fresh_ranges.sort()
    merged = []
    for start, end in fresh_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    # Count unique IDs
    total = sum(end - start + 1 for start, end in merged)
    return total

# Tests
def test_example_ranges():
    # Example from prompt
    ranges = ["3-5", "10-14", "16-20", "12-18"]
    with open("test_input.txt", "w") as f:
        for r in ranges:
            f.write(r + "\n")
    assert count_unique_fresh_ids_from_file("test_input.txt") == 14


def test_single_value_ranges():
    ranges = ["1-1", "2-2", "3-3"]
    with open("test_input.txt", "w") as f:
        for r in ranges:
            f.write(r + "\n")
    assert count_unique_fresh_ids_from_file("test_input.txt") == 3


def test_overlapping_ranges():
    ranges = ["1-5", "3-7", "6-10"]
    with open("test_input.txt", "w") as f:
        for r in ranges:
            f.write(r + "\n")
    assert count_unique_fresh_ids_from_file("test_input.txt") == 10


def test_large_range():
    ranges = ["1-1000000"]
    with open("test_input.txt", "w") as f:
        for r in ranges:
            f.write(r + "\n")
    assert count_unique_fresh_ids_from_file("test_input.txt") == 1000000


def test_real_input():
    # Use the actual input file
    result = count_unique_fresh_ids_from_file("c:/Projects/playground/aoc2025/5/input.txt")
    print("Total fresh ingredient IDs:", result)
    assert isinstance(result, int)
