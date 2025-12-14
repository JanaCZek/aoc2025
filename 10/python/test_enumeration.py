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
        (0, 1),
        (2,),
        (1, 2),
    ]
    desired_state = [3, 4]

    expected_combinations = (
        {
            (0, 1): 0,
            (2,): 0,
            (1, 2): 0,
        },
        {
            (0, 1): 1,
            (2,): 0,
            (1, 2): 0,
        },
        {
            (0, 1): 0,
            (2,): 1,
            (1, 2): 0,
        },
        {
            (0, 1): 0,
            (2,): 0,
            (1, 2): 1,
        },
        {
            (0, 1): 1,
            (2,): 1,
            (1, 2): 0,
        },
        {
            (0, 1): 1,
            (2,): 0,
            (1, 2): 1,
        },
        {
            (0, 1): 0,
            (2,): 1,
            (1, 2): 1,
        },
        {
            (0, 1): 1,
            (2,): 1,
            (1, 2): 1,
        },
    )

    generated_combinations = button_press_combination_generator(button_sets, desired_state)

    for expected in expected_combinations:
        frozen = frozenset(expected.items())
        found = False
        for generated in button_press_combination_generator(button_sets, desired_state):
            if frozen == frozenset(generated.items()):
                found = True
                break
        assert found, f"Expected combination not found: {expected}"

def test_button_press_counts():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    all_counts = all_counts_of_button_presses_for_joltage(line)

    print()
    print("Combinations")
    for generated in all_counts:
        print(generated)
    assert True

    line = "[##...##] (0,3,4,6) (1,2,4,5,6) (0,1,2,5,6) (0,1,3,5) (0,2,3,4,6) {29,26,26,12,9,26,26}"
    all_counts = all_counts_of_button_presses_for_joltage(line)

    print()
    print("Combinations")
    for generated in all_counts:
        print(generated)
    assert True
    
def all_counts_of_button_presses_for_joltage(line):
    desired_state, button_sets = parse_line_to_machine_with_joltage(line)
    combinations = button_press_combination_generator(button_sets, desired_state)

    for combo in combinations:
        current_joltage = [0] * len(desired_state)
        new_joltage = increase_joltage(combo, current_joltage)
        if new_joltage == desired_state:
            yield combo

def button_press_combination_generator(button_sets, desired_state):
    from itertools import product

    num_button_sets = len(button_sets)
    joltage_range = range(len(desired_state))
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
