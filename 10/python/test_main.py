import numpy as np

# def test_hillclimber_machine_one():
#     button_sets = [
#         [3],
#         [1, 3],
#         [2],
#         [2, 3],
#         [0, 2],
#         [0, 1],
#     ]
#     current_state = [False, False, False, False]
#     desired_state = [False, True, True, False]

#     best_button_press_count, _ = hillclimber_button_press_count(button_sets, current_state, desired_state)

#     print("ONE Best button press count found:", best_button_press_count)

#     assert True

# def test_hillclimber_machine_two():
#     button_sets = [
#         [0, 2, 3, 4],
#         [2, 3],
#         [0, 4],
#         [0, 1, 2],
#         [1, 2, 3, 4],
#     ]
#     current_state = [False, False, False, False, False]
#     desired_state = [False, False, False, True, False]

#     best_button_press_count, best = hillclimber_button_press_count(button_sets, current_state, desired_state)

#     print("TWO Best button press count found:", best_button_press_count)

#     assert True

# def test_hillclimber_machine_three():
#     button_sets = [
#         (0, 1, 2, 3, 4),
#         (0, 3, 4),
#         (0, 1, 2, 4, 5),
#         (1, 2),
#     ]
#     current_state = [False, False, False, False, False, False]
#     desired_state = [False, True, True, True, False, True]

#     best_button_press_count, best = hillclimber_button_press_count(button_sets, current_state, desired_state)

#     print("TWO Best button press count found:", best_button_press_count)

#     assert True

def test_parse_line_to_machine():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected_desired_state = [False, True, True, False]
    expected_button_sets = [
        [3],
        [1, 3],
        [2],
        [2, 3],
        [0, 2],
        [0, 1],
    ]

    desired_state, button_sets = parse_line_to_machine(line)

    assert desired_state == expected_desired_state
    assert button_sets == expected_button_sets

def test_toggle():
    button_sets = [
        [3],
        [1, 3],
        [2],
        [2, 3],
        [0, 2],
        [0, 1],
    ]
    current_state = [False, False, False, False]
    desired_state = [False, True, True, False]

    new_state = toggle([button_sets[-1], button_sets[-2]], current_state)
    assert new_state == desired_state

def test_fitness_function():
    current_state = [False, False, False, False]
    desired_state = [False, True, True, False]

    button_press_count = 2
    best_score = fitness_function(button_press_count, current_state, desired_state)

    button_press_count = 3
    worse_score = fitness_function(button_press_count, current_state, desired_state)

    assert best_score > worse_score

def test_joltage_parsing():
    line = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"

    expected = [3, 5, 4, 7]

    desired_state, _ = parse_line_to_machine_with_joltage(line)

    assert desired_state == expected

def test_increase_joltage():
    button_sets = [
        [0, 2],
        [1, 3],
    ]
    current_joltage = [0, 0, 0, 0]

    new_joltage = increase_joltage(button_sets, current_joltage)

    expected_joltage = [1, 1, 1, 1]

    assert new_joltage == expected_joltage

def test_hillclimber_joltage_machine_one():
    button_sets = [
        [3],
        [1, 3],
        [2],
        [2, 3],
        [0, 2],
        [0, 1],
    ]
    current_state = [0, 0, 0, 0]
    desired_state = [3,5,4,7]

    best_button_press_count, best = hillclimber_joltage_button_press_count(button_sets, current_state, desired_state)

    print("ONE Best button press count found:", best_button_press_count)
    print("Best individual:", best)

    assert best_button_press_count == 10

def test_hillclimber_joltage_machine_two():
    button_sets = [
        [0, 2, 3, 4],
        [2, 3],
        [0, 4],
        [0, 1, 2],
        [1, 2, 3, 4],
    ]
    current_state = [0, 0, 0, 0, 0]
    desired_state = [7,5,12,7,2]

    best_button_press_count, best = hillclimber_joltage_button_press_count(button_sets, current_state, desired_state)

    print("TWO Best button press count found:", best_button_press_count)
    print("Best individual:", best)

    assert best_button_press_count == 12

def test_hillclimber_joltage_machine_three():
    button_sets = [
        [0, 1, 2, 3, 4],
        [0, 3, 4],
        [0, 1, 2, 4, 5],
        [1, 2],
    ]
    current_state = [0, 0, 0, 0, 0, 0]
    desired_state = [10,11,11,5,10,5]

    best_button_press_count, best = hillclimber_joltage_button_press_count(button_sets, current_state, desired_state)

    print("THREE Best button press count found:", best_button_press_count)
    print("Best individual:", best)

    assert best_button_press_count == 11

def hillclimber_button_press_count(button_sets, current_state, desired_state):
    # button_sets: [[0, 1, 2], [1, 3], ...]
    # current_state: [true, false, ...]

    population_size = 100
    population = create_population(button_sets, population_size, None)
    generations_count = 500
    generation = 0
    retry_count = 0

    global_best_score = -np.inf
    global_best_individual = None
    global_minimum_button_press_count = np.inf
    result_found = False

    while not result_found and generation < generations_count:
        fitness_scores = []

        for individual in population:
            new_state = toggle(individual, current_state)

            button_press_count = len(individual)
            score = fitness_function(button_press_count, new_state, desired_state)

            fitness_scores.append(score)

        best_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])
        best_individual = population[best_index]
        best_score = fitness_scores[best_index]

        if best_score >= global_best_score:
            global_best_score = best_score
            global_best_individual = best_individual

        if len(best_individual) < global_minimum_button_press_count:
            global_minimum_button_press_count = len(best_individual)

        population = create_population(button_sets, population_size, global_best_individual)

        if generation == generations_count - 1:
            new_state = toggle(global_best_individual, current_state)
            if new_state != desired_state:
                result_found = False
                generations_count += 10
                if retry_count > 10:
                    population = create_population(button_sets, population_size, None)
                    retry_count = 0
            else:
                result_found = True

        generation += 1

    return len(global_best_individual), global_best_individual

def hillclimber_joltage_button_press_count(button_sets, current_state, desired_state):

    population_size = 600
    stddev_size = 4
    population = create_population_joltage(button_sets, population_size, None, stddev_size)
    generations_count = 500
    generation = 0
    retry_count = 0

    global_best_score = -np.inf
    global_best_individual = None
    global_minimum_button_press_count = np.inf
    result_found = False

    while generation < generations_count:
        fitness_scores = []

        for individual in population:
            new_state = increase_joltage(individual, current_state)

            button_press_count = len(individual)
            score = fitness_function_joltage(button_press_count, new_state, desired_state)

            fitness_scores.append(score)

        best_index = max(range(len(fitness_scores)), key=lambda i: fitness_scores[i])
        best_individual = population[best_index]
        best_score = fitness_scores[best_index]

        new_state = []
        if global_best_individual is not None:
            new_state = increase_joltage(global_best_individual, current_state)

        if best_score >= global_best_score:
            global_best_score = best_score
            global_best_individual = best_individual

        if len(best_individual) < global_minimum_button_press_count:
            global_minimum_button_press_count = len(best_individual)

        population = create_population_joltage(button_sets, population_size, global_best_individual, stddev_size)

        # print("Generation:", generation, "Best score:", best_score, "Global best score:", global_best_score, "New state:", new_state, "Desired state:", desired_state, "Button presses:", len(best_individual))
        # print("Global best individual:", global_best_individual)
        # print_hillclimber_data(population, fitness_scores, desired_state)

        # if generation == generations_count - 1:
        #     if new_state != desired_state:
        #         result_found = False
        #         generations_count += 10
        #         if retry_count > 10:
        #             population = create_population_joltage(button_sets, population_size, None, stddev_size)
        #             retry_count = 0
        #     else:
        #         result_found = True

        generation += 1

    print("Final best state:", increase_joltage(global_best_individual, current_state), "Desired state:", desired_state)

    return len(global_best_individual), global_best_individual

def fitness_function(button_press_count, current_state, desired_state):
    button_state_match_score = 100
    button_press_count_penalty_multiplier = 0.9
    score = 0

    for i in range(len(current_state)):
        if current_state[i] == desired_state[i]:
            score += button_state_match_score

    score -= button_press_count * button_press_count_penalty_multiplier

    return score

def fitness_function_joltage(button_press_count, current_state, desired_state):
    button_state_match_score = 100
    button_press_count_penalty_multiplier = 0.9
    score = 0

    for i in range(len(current_state)):
        diff = abs(current_state[i] - desired_state[i])
        if diff == 0:
            score += button_state_match_score
        else:
            score += button_state_match_score / diff

    score -= button_press_count * button_press_count_penalty_multiplier

    return score

def toggle(button_sets, current_state):
    new_state = current_state.copy()
    for button_set in button_sets:
        for button in button_set:
            new_state[button] = not new_state[button]
    return new_state

def create_population(button_sets, population_size, best_individual, stddev_size=3):
    # Generate button set counts up to len(button_sets) using normal distribution around best_individual
    button_set_count = np.random.randint(1, len(button_sets), size=population_size)
    if best_individual is not None:
        mean_size = len(best_individual)
        button_set_count = np.random.normal(mean_size, stddev_size, size=population_size).astype(int)
        button_set_count = np.clip(button_set_count, 1, len(button_sets))
        
    population = []
    
    # Generate individuals up to population_size using normal distribution around best_individual
    if best_individual is not None:
        for _ in range(population_size):
            mean_size = len(best_individual)
            individual_size = int(np.random.normal(mean_size, stddev_size))
            individual_size = max(1, min(individual_size, len(button_sets)))

            selected_button_set_indexes = np.random.randint(0, len(button_sets), size=individual_size)
            selected_button_sets = [button_sets[index] for index in selected_button_set_indexes]
            population.append(selected_button_sets)
    else:
        for i in range(population_size):
            selected_button_set_indexes = np.random.randint(0, len(button_sets), size=button_set_count[i])
            selected_button_sets = [button_sets[index] for index in selected_button_set_indexes]
            population.append(selected_button_sets)
            
    return population

def create_population_joltage(button_sets, population_size, best_individual, stddev_size=3):
    button_set_count = np.random.randint(1, len(button_sets), size=population_size)
    if best_individual is not None:
        mean_size = len(best_individual)
        button_set_count = np.random.normal(mean_size, stddev_size, size=population_size).astype(int)
        np.clip(button_set_count, min=1, max=len(best_individual) + stddev_size)
        
    population = []
    
    if best_individual is not None:
        population.append(best_individual)
        for _ in range(population_size - 1):
            mean_size = len(best_individual)
            individual_size = int(np.random.normal(mean_size, stddev_size))
            individual_size = np.clip(individual_size, 1, mean_size + stddev_size)

            selected_button_set_indexes = np.random.randint(0, len(button_sets), size=individual_size)
            selected_button_sets = [button_sets[index] for index in selected_button_set_indexes]
            population.append(selected_button_sets)
    else:
        for i in range(population_size):
            selected_button_set_indexes = np.random.randint(0, len(button_sets), size=button_set_count[i])
            selected_button_sets = [button_sets[index] for index in selected_button_set_indexes]
            population.append(selected_button_sets)
            
    return population

def parse_line_to_machine(line):
    parts = line.split(" ")
    desired_state_str = parts[0]
    button_sets_strs = parts[1:-1]

    desired_state = []
    for char in desired_state_str[1:-1]:
        if char == "#":
            desired_state.append(True)
        else:
            desired_state.append(False)

    button_sets = []
    for button_set_str in button_sets_strs:
        button_set_str = button_set_str[1:-1]
        button_indexes = [int(x) for x in button_set_str.split(",")]
        button_sets.append(button_indexes)

    return desired_state, button_sets

def parse_line_to_machine_with_joltage(line):
    parts = line.split(" ")
    button_sets_strs = parts[1:-1]
    desired_state_str = parts[-1]

    desired_state = desired_state_str[1:-1].split(",")
    desired_state = [int(x) for x in desired_state]

    button_sets = []
    for button_set_str in button_sets_strs:
        button_set_str = button_set_str[1:-1]
        button_indexes = [int(x) for x in button_set_str.split(",")]
        button_sets.append(button_indexes)

    return desired_state, button_sets

def increase_joltage(button_sets, current_joltage):
    new_state = current_joltage.copy()
    for button_set in button_sets:
        for button in button_set:
            new_state[button] += 1
    return new_state

def print_hillclimber_data(population, fitness_scores, desired_state):
    for i in range(len(population)):
        individual = population[i]
        score = fitness_scores[i]
        print("Individual:", individual, "\nScore:", score)
        current_state = increase_joltage(individual, [0]*len(desired_state))
        print("Current state:", current_state, "\nDesired state:", desired_state)
        print("-----")

# def test_input_part_one():
#     with open(r"c:/Projects/playground/aoc2025/10/input.txt", encoding='utf-8') as f:
#         total_counts = 0
#         for line in f:
#             desired_state, button_sets = parse_line_to_machine(line.strip())
#             current_state = [False] * len(desired_state)
#             best_button_press_count, best_individual = hillclimber_button_press_count(button_sets, current_state, desired_state)
#             print("Best button press count found for line:", best_button_press_count)
#             total_counts += best_button_press_count
#         print("Final total button press counts:", total_counts)
            
#     assert True
