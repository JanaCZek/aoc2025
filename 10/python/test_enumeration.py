def test_increase_joltage():
    button_set = [0, 2]
    current_joltage = [0, 0, 0, 0]

    new_joltage = increase_joltage(button_set, current_joltage)

    expected_joltage = [1, 0, 1, 0]

    assert new_joltage == expected_joltage
    
def test_is_over_target():
    target = [1, 1]
    current_joltage = [1, 1]
    result = is_over_target(target, current_joltage)

    assert result is False

    current_joltage = [1, 2]
    result = is_over_target(target, current_joltage)

    assert result is True

    current_joltage = [2, 1]
    result = is_over_target(target, current_joltage)

    assert result is True

    current_joltage = [2, 2]
    result = is_over_target(target, current_joltage)

    assert result is True

def test_advances_up():
    button_sets = [
        [0, 2],
        [1],
    ]
    button_set_index = 0
    current_joltage = [0, 0, 0]

    new_joltage = advance_up(button_sets, button_set_index, current_joltage)

    expected_joltage = [1, 0, 1]

    assert new_joltage == expected_joltage

def test_levels_are_initially_zero():
    button_sets = [
        [0, 2],
        [1],
    ]

    levels = initialize_levels(button_sets)

    expected_levels = [0, 0]

    assert levels == expected_levels

def test_advances_up_until_over_target():
    button_sets = [
        [0, 2],
        [1],
    ]

    current_joltage = [0, 0, 0]
    button_set_index = 0

    target_joltage = [2, 1, 2]
    target_level = 2

    level = advance_up_until_on_target(button_sets, button_set_index, current_joltage, target_joltage)

    assert level == target_level

    target_joltage = [2, 1, 3]
    target_level = 2

    level = advance_up_until_on_target(button_sets, button_set_index, current_joltage, target_joltage)

    assert level == target_level

    target_joltage = [3, 1, 2]
    target_level = 2

    level = advance_up_until_on_target(button_sets, button_set_index, current_joltage, target_joltage)

    assert level == target_level

def test_converts_levels_to_joltage():
    button_sets = [
        [0, 2],
        [1],
    ]

    levels = [2, 3]
    expected_joltage = [2, 3, 2]
    current_joltage = [0, 0, 0]

    joltage = levels_to_joltage(button_sets, levels, current_joltage)

    assert joltage == expected_joltage

def test_advance_to_target_scenario():
    button_sets = [
        [0, 2],
        [1],
    ]

    current_joltage = [0, 0, 0]
    button_set_index = 0
    levels = [0, 0]

    target_joltage = [2, 0, 2]

    level = advance_up_until_on_target(button_sets, button_set_index, current_joltage, target_joltage)

    levels[button_set_index] = level

    assert levels == [2, 0]

    joltage = levels_to_joltage(button_sets, levels, current_joltage)

    assert joltage == target_joltage

def increase_joltage(button_set, current_joltage):
    new_state = current_joltage.copy()

    for button in button_set:
        new_state[button] += 1

    return new_state

def is_over_target(target, current_joltage):
    for i in range(len(target)):
        if current_joltage[i] > target[i]:
            return True
    return False

def advance_up(button_sets, button_set_index, current_joltage):
    new_joltage = increase_joltage(button_sets[button_set_index], current_joltage)
    return new_joltage

def initialize_levels(button_sets):
    return [0] * len(button_sets)

def advance_up_until_on_target(button_sets, button_set_index, current_joltage, target_joltage):
    current_level = 0
    joltage = current_joltage.copy()

    while True:
        joltage = advance_up(button_sets, button_set_index, joltage)
        current_level += 1
        if is_over_target(target_joltage, joltage):
            current_level -= 1
            break

    return current_level

def levels_to_joltage(button_sets, levels, current_joltage):
    joltage = current_joltage.copy()

    for i in range(len(button_sets)):
        for _ in range(levels[i]):
            joltage = increase_joltage(button_sets[i], joltage)

    return joltage