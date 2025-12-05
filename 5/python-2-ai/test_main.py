def test_addition():
    # Dummy test to keep file valid
    assert True
def test_count_fresh_ids_sample():
    # Sample data: fresh ranges
    fresh_ranges = [(100, 200), (250, 300)]
    # Expected fresh IDs: 101 (100-200) + 51 (250-300) = 152
    expected_count = 101 + 51
    result = count_fresh_ids(fresh_ranges)
    assert result == expected_count

def test_count_fresh_ids_overlap():
    # Overlapping ranges
    fresh_ranges = [(100, 200), (150, 250)]
    # Merged: (100, 250) => 151 IDs
    expected_count = 151
    result = count_fresh_ids(fresh_ranges)
    assert result == expected_count

def test_count_fresh_ids_boundaries():
    # IDs on boundaries
    fresh_ranges = [(10, 20), (30, 40)]
    # 11 IDs (10-20) + 11 IDs (30-40) = 22
    expected_count = 11 + 11
    result = count_fresh_ids(fresh_ranges)
    assert result == expected_count

def test_count_fresh_ids_spoiled():
    # No fresh IDs
    fresh_ranges = []
    expected_count = 0
    result = count_fresh_ids(fresh_ranges)
    assert result == expected_count


# Function to be implemented
def count_fresh_ids(fresh_ranges, available_ids=None):
    # Step 2: Merge overlapping/adjacent ranges
    if not fresh_ranges:
        return 0
    sorted_ranges = sorted(fresh_ranges, key=lambda x: x[0])
    merged = []
    for rng in sorted_ranges:
        if not merged:
            merged.append(list(rng))
        else:
            last = merged[-1]
            if rng[0] <= last[1] + 1:
                last[1] = max(last[1], rng[1])
            else:
                merged.append(list(rng))
    # Step 3: Efficiently count all unique fresh IDs
    total_count = 0
    for start, end in merged:
        total_count += end - start + 1
    return total_count


def parse_input_file(path):
    fresh_ranges = []
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if '-' in line:
                try:
                    start, end = map(int, line.split('-'))
                    fresh_ranges.append((start, end))
                except ValueError:
                    pass
    return fresh_ranges

def test_real_input():
    fresh_ranges = parse_input_file('c:/Projects/playground/aoc2025/5/input.txt')
    result = count_fresh_ids(fresh_ranges)
    print(f"Fresh ingredient IDs count: {result}")
