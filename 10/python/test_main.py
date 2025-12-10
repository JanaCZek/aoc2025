import numpy as np

def test_hillclimber_machine_one():
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

    best_button_press_count, _ = hillclimber_button_press_count(button_sets, current_state, desired_state)

    print("ONE Best button press count found:", best_button_press_count)

    assert True

def test_hillclimber_machine_two():
    button_sets = [
        [0, 2, 3, 4],
        [2, 3],
        [0, 4],
        [0, 1, 2],
        [1, 2, 3, 4],
    ]
    current_state = [False, False, False, False, False]
    desired_state = [False, False, False, True, False]

    best_button_press_count, best = hillclimber_button_press_count(button_sets, current_state, desired_state)

    print("TWO Best button press count found:", best_button_press_count)

    assert True

def test_hillclimber_machine_three():
    button_sets = [
        (0, 1, 2, 3, 4),
        (0, 3, 4),
        (0, 1, 2, 4, 5),
        (1, 2),
    ]
    current_state = [False, False, False, False, False, False]
    desired_state = [False, True, True, True, False, True]

    best_button_press_count, best = hillclimber_button_press_count(button_sets, current_state, desired_state)

    print("TWO Best button press count found:", best_button_press_count)

    assert True

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

def hillclimber_button_press_count(button_sets, current_state, desired_state):
    # button_sets: [[0, 1, 2], [1, 3], ...]
    # current_state: [true, false, ...]

    population_size = 10
    population = create_population(button_sets, population_size, None)
    generations_count = 20
    generation = 0
    retry_count = 0

    global_best_score = -np.inf
    global_best_individual = None
    result_found = False

    while not result_found:
        fitness_scores = []

        for individual in population:
            new_state = toggle(individual, current_state)

            button_press_count = len(individual)
            score = fitness_function(button_press_count, new_state, desired_state)

            fitness_scores.append(score)

        best_index = np.argmax(fitness_scores)
        best_individual = population[best_index]
        best_score = fitness_scores[best_index]

        if best_score > global_best_score and (global_best_individual is None or len(best_individual) <= len(global_best_individual)):
            global_best_score = best_score
            global_best_individual = best_individual
            print(f"Generation {generation}: New best individual found with button press count {global_best_individual}")

        population = create_population(button_sets, population_size, global_best_individual)

        if generation == generations_count - 1:
            new_state = toggle(global_best_individual, current_state)
            if new_state != desired_state:
                generations_count += 10
                if retry_count > 10:
                    population = create_population(button_sets, population_size, None)
                    retry_count = 0
            else:
                result_found = True

        generation += 1

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

def toggle(button_sets, current_state):
    new_state = current_state.copy()
    for button_set in button_sets:
        for button in button_set:
            new_state[button] = not new_state[button]
    return new_state

def create_population(button_sets, population_size, best_individual):
    stddev_size = 1

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

def test_input_part_one():
    with open(r"c:/Projects/playground/aoc2025/10/input.txt", encoding='utf-8') as f:
        total_counts = 0
        for line in f:
            desired_state, button_sets = parse_line_to_machine(line.strip())
            current_state = [False] * len(desired_state)
            best_button_press_count, _ = hillclimber_button_press_count(button_sets, current_state, desired_state)
            print("Best button press count found for line:", best_button_press_count)
            total_counts += best_button_press_count
        print("Final total button press counts:", total_counts)
            
    assert True
    
# def test_input_part_two():
#     with open(r"c:/Projects/playground/aoc2025/10/input.txt", encoding='utf-8') as f:
#         input_str = f.read()
#         result = product_of_last_two_x_coordinates(input_str)
#         print("Final result:", result)
#     assert True
    