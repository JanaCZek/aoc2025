from itertools import product

def test_parse_line_to_machine():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected_button_sets = [
        (3,),
        (1, 3),
        (2,),
        (2, 3),
        (0, 2),
        (0, 1),
    ]

    _, button_sets = parse_line_to_machine_with_joltage(line)

    assert button_sets == expected_button_sets

def test_joltage_parsing():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected = [3, 5, 4, 7]

    desired_state, _ = parse_line_to_machine_with_joltage(line)

    assert desired_state == expected

def test_increase_joltage():
    button_sets_dict = {
        (3,): 0,
        (1, 3): 1,
        (2,): 0,
        (2, 3): 0,
        (0, 2): 1,
        (0, 1): 0,
    }
    current_joltage = [0, 0, 0, 0]

    new_joltage = increase_joltage(button_sets_dict, current_joltage)

    expected_joltage = [1, 1, 1, 1]

    assert new_joltage == expected_joltage

    button_sets_dict = {
        (3,): 2,
        (1, 3): 0,
        (2,): 3,
        (2, 3): 0,
        (0, 2): 2,
        (0, 1): 1,
    }
    
    current_joltage = [1, 2, 3, 4]

    new_joltage = increase_joltage(button_sets_dict, current_joltage)

    expected_joltage = [4, 3, 8, 6]

    assert new_joltage == expected_joltage

def test_combination_generator():
    button_sets = [
        (0,),
        (1,),
        (0, 1),
    ]
    desired_state = [2, 2]

    expected_combinations = (
        {
            (0,): 2,
            (1,): 2,
            (0, 1): 0,
        },
        {
            (0,): 0,
            (1,): 0,
            (0, 1): 2,
        },
        {
            (0,): 1,
            (1,): 1,
            (0, 1): 1,
        },
    )

    for expected in expected_combinations:
        frozen = frozenset(expected.items())
        found = False
        for generated in button_press_combination_generator(button_sets, desired_state):
            if frozen == frozenset(generated.items()):
                found = True
                break
        assert found, f"Expected combination not found: {expected}"

    # for generated in button_press_combination_generator(button_sets, desired_state):
    #     print(generated)

def test_button_press_counts():
    lines = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}",
        "[.#.#] (0,2) (1,3) {1,16,1,16}",
        "[#.#.] (1,3) (0,2) {11,1,11,1}",
        "[#.#.] (2,3) (1,3) (0,3) {8,9,6,23}",
        "[#.##] (0,1,3) (0,2,3) {20,15,5,20}",
    ]
    # for line in lines:
    #     all_counts = all_counts_of_button_presses_for_joltage(line)

    #     print()
    #     print("Combinations")
    #     for generated in all_counts:
    #         print(generated)
    #         print(sum(generated.values()))
    #     assert True

def test_subset_check():
    full_set = {
        frozenset({(0,): 0, (1,): 0, (0, 1): 0}.items()),
        frozenset({(0,): 0, (1,): 0, (0, 1): 1}.items()),
        frozenset({(0,): 0, (1,): 0, (0, 1): 2}.items()),
    }
    subset = frozenset({(1,): 0, (0, 1): 2}.items())
    
    found = any(subset.issubset(set) for set in full_set)

    subset = frozenset({(1,): 0, (0, 1): 3}.items())
    
    found = any(subset.issubset(set) for set in full_set)

    assert not found

def test_get_button_set_presses_satisfying_joltage():
    button_sets = [
        (0,),
        (1,),
        (0, 1),
    ]

    button_set_index = 0
    desired_joltage = 2
    
    expected = {
        frozenset({(0,): 2, (0, 1): 0}.items()),
        frozenset({(0,): 1, (0, 1): 1}.items()),
        frozenset({(0,): 0, (0, 1): 2}.items()),
    }

    for item in get_button_set_presses_satisfying_joltage(button_sets, button_set_index, desired_joltage):
        print(item)

    for item in expected:
        found = False
        for generated in get_button_set_presses_satisfying_joltage(button_sets, button_set_index, desired_joltage):
            if item == generated:
                found = True
                break
        assert found, f"Expected combination not found: {item}"

    button_set_index = 1
    desired_joltage = 2
    
    expected = {
        frozenset({(1,): 2, (0, 1): 0}.items()),
        frozenset({(1,): 1, (0, 1): 1}.items()),
        frozenset({(1,): 0, (0, 1): 2}.items()),
    }

    print()
    for item in get_button_set_presses_satisfying_joltage(button_sets, button_set_index, desired_joltage):
        print(item)

    for item in expected:
        found = False
        for generated in get_button_set_presses_satisfying_joltage(button_sets, button_set_index, desired_joltage):
            if item == generated:
                found = True
                break
        assert found, f"Expected combination not found: {item}"

    expected_combinations = {
        frozenset({(0,): 0, (1,): 0, (0, 1): 2}.items()),
        frozenset({(0,): 1, (1,): 1, (0, 1): 1}.items()),
        frozenset({(0,): 2, (1,): 2, (0, 1): 0}.items()),
    }

    print()
    
    combinations = set()

    for combo_one in get_button_set_presses_satisfying_joltage(button_sets, 0, 2):
        for combo_two in get_button_set_presses_satisfying_joltage(button_sets, 1, 2):
            combined = dict(combo_one)
            combined.update(dict(combo_two))
            frozen_combined = frozenset(combined.items())
            if frozen_combined in expected_combinations:
                print(frozen_combined)
                combinations.add(frozen_combined)

    for item in expected_combinations:        
        assert item in combinations, f"Expected combination not found: {item}"

def all_counts_of_button_presses_for_joltage(line):
    desired_state, button_sets = parse_line_to_machine_with_joltage(line)
    combinations = button_press_combination_generator(button_sets, desired_state)

    for combo in combinations:
        current_joltage = [0] * len(desired_state)
        new_joltage = increase_joltage(combo, current_joltage)
        if new_joltage == desired_state:
            yield combo

def button_press_combination_generator(button_sets, desired_state):
    num_button_sets = len(button_sets)
    joltage_range = range(max(desired_state) + 1)
    for counts in product(joltage_range, repeat=num_button_sets):
        yield {
            button_sets[i]: counts[i]
            for i in range(num_button_sets)
        }

def increase_joltage(button_sets_dict, current_joltage):
    return [
        current_joltage[i] + 
        sum(count for button_set, count in button_sets_dict.items() if i in button_set)
        for i in range(len(current_joltage))
    ]

def get_button_set_presses_satisfying_joltage(button_sets, button_set_index, joltage_requirement):
    relevant_button_sets = [bs for bs in button_sets if button_set_index in bs]
    num_relevant_button_sets = len(relevant_button_sets)
    joltage_range = range(joltage_requirement + 1)

    for counts in product(joltage_range, repeat=num_relevant_button_sets):
        combo = {
            relevant_button_sets[i]: counts[i]
            for i in range(num_relevant_button_sets)
        }
        total_joltage = sum(
            count for _, count in combo.items()
        )
        if total_joltage == joltage_requirement:
            yield frozenset(combo.items())

def parse_line_to_machine_with_joltage(line):
    parts = line.split(" ")
    button_sets_strs = parts[1:-1]
    desired_state_str = parts[-1]

    desired_state = desired_state_str[1:-1].split(",")
    desired_state = [int(x) for x in desired_state]

    button_sets = []
    for button_set_str in button_sets_strs:
        button_set_str = button_set_str[1:-1]
        button_indices = button_set_str.split(",")
        button_indices = [int(x) for x in button_indices]
        button_sets.append(button_indices)

    button_tuples = [tuple(bs) for bs in button_sets]

    return desired_state, button_tuples
