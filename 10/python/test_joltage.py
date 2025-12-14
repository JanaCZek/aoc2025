import numpy as np

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

def test_fitness_function_joltage():
    current_state = [0, 0, 0, 0]
    desired_state = [1, 1, 1, 1]

    button_press_count = 1
    worse_score = fitness_function_joltage(button_press_count, current_state, desired_state)

    current_state = [1, 1, 1, 1]

    button_press_count = 1
    best_score = fitness_function_joltage(button_press_count, current_state, desired_state)

    assert best_score > worse_score

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
    # 0 0 0 1
    # 0 0 0 2
    # 0 0 1 2
    # 0 0 2 2
    # 0 0 3 2
    # 1 0 4 2
    # 2 0 5 2
    # 3 1 5 2
    current_joltage = [1, 2, 3, 4]

    new_joltage = increase_joltage(button_sets_dict, current_joltage)

    # [3, 1, 5, 2] + [1, 2, 3, 4]
    expected_joltage = [4, 3, 8, 6]

    assert new_joltage == expected_joltage

def test_create_population_without_best():
    button_sets = [
        (3,),
        (1, 3),
        (2,),
        (2, 3),
        (0, 2),
        (0, 1),
    ]

    desired_joltage = [3, 5, 4, 7]

    population = create_population(10, button_sets, desired_joltage, None)

    assert len(population) == 10

def test_create_population_with_best():
    button_sets = [
        (3,),
        (1, 3),
        (2,),
        (2, 3),
        (0, 2),
        (0, 1),
    ]

    desired_joltage = [3, 5, 4, 7]

    best = {
        (3,): 2,
        (1, 3): 0,
        (2,): 3,
        (2, 3): 0,
        (0, 2): 2,
        (0, 1): 1,
    }

    population = create_population(10, button_sets, desired_joltage, best)

    assert len(population) == 10

def test_ga_joltage_machine_one():
    button_sets = [
        (3,),
        (1, 3),
        (2,),
        (2, 3),
        (0, 2),
        (0, 1),
    ]

    current_state = [0, 0, 0, 0]
    desired_state = [3, 5, 4, 7]
    expected_button_press_count = 10

    button_press_count, button_press_dict = ga_joltage(button_sets, current_state, desired_state)

    new_state = increase_joltage(button_press_dict, current_state)

    print("New state:", new_state)
    print("Desired state:", desired_state)
    print("Button press count:", button_press_count)

    assert new_state == desired_state
    assert button_press_count == expected_button_press_count

def test_ga_joltage_machine_two():
    button_sets = [
        (0, 2, 3, 4,),
        (2, 3,),
        (0, 4,),
        (0, 1, 2,),
        (1, 2, 3, 4,),
    ]
    current_state = [0, 0, 0, 0, 0]
    desired_state = [7, 5, 12, 7, 2]
    expected_button_press_count = 12

    button_press_count, button_press_dict = ga_joltage(button_sets, current_state, desired_state)

    new_state = increase_joltage(button_press_dict, current_state)

    print("New state:", new_state)
    print("Desired state:", desired_state)
    print("Button press count:", button_press_count)

    assert new_state == desired_state
    assert button_press_count == expected_button_press_count

def fitness_function_joltage(button_press_count, current_state, desired_state):
    button_state_match_score = 100
    button_press_count_penalty_multiplier = 0.9
    score = 0

    score += sum(
        button_state_match_score if abs(current_state[i] - desired_state[i]) == 0 
        else button_state_match_score / (abs(current_state[i] - desired_state[i]) + 1)
        for i in range(len(current_state))
    )

    score -= button_press_count * button_press_count_penalty_multiplier

    return score

def increase_joltage(button_sets_dict, current_joltage):
    return [
        current_joltage[i] + 
        sum(count for button_set, count in button_sets_dict.items() if i in button_set)
        for i in range(len(current_joltage))
    ]

def create_population(population_size, button_sets, desired_joltage, best_individual):
    population = set()
    max_button_presses = max(desired_joltage)

    if best_individual is None:
        button_press_counts = np.random.randint(0, max_button_presses, size=(population_size, len(button_sets)))
        population = {
            frozenset({button_sets[i]: bpc[i] for i in range(len(button_sets))}.items())
            for bpc in button_press_counts
        }
    else:
        max_spread = 1
        min_spread = -1 * max_spread
        
        while len(population) < population_size:
            new_individual = {
                button_set: max(0, count + np.random.randint(min_spread, max_spread + 1))
                for button_set, count in best_individual.items()
            }
            population.add(frozenset(new_individual.items()))

    return population

def calculate_fitness_score(individual, current_state, desired_state):
    new_state = increase_joltage(individual, current_state)

    button_press_count = len(individual)
    score = fitness_function_joltage(button_press_count, new_state, desired_state)
    return score

def ga_joltage(button_sets, current_state, desired_state):
    population_size = 500
    generations_count = 100
    generation = 0

    global_best_score = -np.inf
    global_best_individual = None
    global_minimum_button_press_count = np.inf

    while generation < generations_count:
        population = create_population(population_size, button_sets, desired_state, None)

        fitness_scores = {
            individual: calculate_fitness_score(dict(individual), current_state, desired_state)
            for individual in population
        }

        best_individual = max(fitness_scores, key=fitness_scores.get)
        best_score = fitness_scores[best_individual]

        total_button_presses = sum(count for _, count in dict(best_individual).items())
        matches_desired = increase_joltage(dict(best_individual), current_state) == desired_state
        
        if best_score > global_best_score and total_button_presses < global_minimum_button_press_count and matches_desired:
            global_best_score = best_score
            global_best_individual = best_individual
            global_minimum_button_press_count = total_button_presses
        
        generation += 1

    if global_best_individual is None:
        global_best_individual = best_individual
        global_minimum_button_press_count = total_button_presses

    return global_minimum_button_press_count, dict(global_best_individual)

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
