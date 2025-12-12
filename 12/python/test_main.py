import pytest
import numpy as np

def test_rotate_right_once():
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    expected = [
        ['#', '#', '#'],
        ['#', '.', '.'],
        ['#', '#', '#'],
    ]

    result = rotate_right(shape)

    assert result == expected

def test_rotate_right_twice():
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    expected = [
        ['#', '#', '#'],
        ['#', '.', '#'],
        ['#', '.', '#'],
    ]

    result = rotate_right(rotate_right(shape))

    assert result == expected

def test_rotate_right_thrice():
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    expected = [
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]

    result = rotate_right(rotate_right(rotate_right(shape)))

    assert result == expected

def test_flip_horizontally():
    shape = [
        ['#', '#', '#'],
        ['.', '#', '#'],
        ['.', '.', '#'],
    ]

    expected = [
        ['#', '#', '#'],
        ['#', '#', '.'],
        ['#', '.', '.'],
    ]

    result = flip_horizontally(shape)

    assert result == expected

def test_flip_vertically():
    shape = [
        ['#', '#', '#'],
        ['.', '#', '#'],
        ['.', '.', '#'],
    ]

    expected = [
        ['.', '.', '#'],
        ['.', '#', '#'],
        ['#', '#', '#'],
    ]

    result = flip_vertically(shape)

    assert result == expected

def test_rotate_right_and_flip_horizontally():
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    expected = [
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]

    result = flip_horizontally(rotate_right(shape))

    assert result == expected

@pytest.mark.parametrize("line, expected_size, expected_counts", [
    ("4x4: 0 0 0 0 2 0", [4, 4], [0, 0, 0, 0, 2, 0]),
    ("12x5: 1 0 1 0 2 2", [12, 5], [1, 0, 1, 0, 2, 2]),
])
def test_parse_line_to_requirements(line, expected_size, expected_counts):
    expected = (expected_size, expected_counts)

    result = parse_line_to_requirements(line)

    assert result == expected

@pytest.mark.parametrize("width, height", [
    (3, 3)
])
def test_empty_grid(width, height):
    expected = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
    ]

    result = empty_grid(width, height, '.')

    assert result == expected

def test_get_grid_dimensions():
    grid = [
        ['.', '.'],
        ['.', '.'],
        ['.', '.'],
    ]

    expected_width = 2
    expected_height = 3

    result_width, result_height = get_grid_dimensions(grid)

    assert result_width == expected_width
    assert result_height == expected_height

@pytest.mark.parametrize("grid_width, grid_height, placement_data, expected_occupancy", [
    (3, 3, [([['#', '#', '#']], 0, 0)], [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]),
    (3, 3, [([['#', '#', '#']], 0, 0), ([['#', '#', '#']], 0, 0)], [
        [2, 2, 2],
        [0, 0, 0],
        [0, 0, 0]
    ]),
    (3, 3, [([['#', '#', '#']], 0, 0), ([['#', '#', '#']], 0, 1)], [
        [1, 1, 1],
        [1, 1, 1],
        [0, 0, 0]
    ])
])
def test_get_occupancy_grid(grid_width, grid_height, placement_data, expected_occupancy):
    result_occupancy = get_occupancy_grid(grid_width, grid_height, placement_data)

    assert result_occupancy == expected_occupancy

def test_get_occupancy_grid_with_sample_data():
    grid_width = 4
    grid_height = 4
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]
    shape_flipped = flip_vertically(shape)

    placement_data = [
        (shape_flipped, 0, 0),
        (shape, 1, 1),
    ]

    expected_occupancy = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]

    result_occupancy = get_occupancy_grid(grid_width, grid_height, placement_data)

    assert result_occupancy == expected_occupancy

def test_place_shapes_no_overlap():
    grid = empty_grid(4, 4, '.')
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]
    shape_flipped = flip_vertically(shape)

    placement_data = [
        (shape_flipped, 0, 0),
        (shape, 1, 1),
    ]

    expected_grid = [
        ['#', '#', '#', '.'],
        ['#', '#', '#', '#'],
        ['#', '#', '#', '#'],
        ['.', '#', '#', '#'],
    ]
    expected_occupancy = [
        [1, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]

    result_grid, result_occupancy = place_shapes(grid, placement_data)

    assert result_grid == expected_grid
    assert result_occupancy == expected_occupancy

def test_place_shapes_with_overlap():
    grid = empty_grid(4, 4, '.')
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    placement_data = [
        (shape, 0, 0),
        (shape, 0, 0),
    ]

    expected_grid = [
        ['#', '.', '#', '.'],
        ['#', '.', '#', '.'],
        ['#', '#', '#', '.'],
        ['.', '.', '.', '.'],
    ]
    expected_occupancy = [
        [2, 0, 2, 0],
        [2, 0, 2, 0],
        [2, 2, 2, 0],
        [0, 0, 0, 0],
    ]

    result_grid, result_occupancy = place_shapes(grid, placement_data)

    assert result_grid == expected_grid
    assert result_occupancy == expected_occupancy

def test_get_max_x_and_y():
    grid_width = 4
    grid_height = 4

    expected_max_x = 1
    expected_max_y = 1

    result_max_x, result_max_y = get_max_x_and_y(grid_width, grid_height)

    assert result_max_x == expected_max_x
    assert result_max_y == expected_max_y

def test_get_required_shapes():
    shapes = [
        [['#', '#'], ['#', '#']],
        [['#', '#', '#'], ['.', '#', '.']],
    ]
    required_counts = [1, 2]

    expected = [
        [['#', '#'], ['#', '#']],
        [['#', '#', '#'], ['.', '#', '.']],
        [['#', '#', '#'], ['.', '#', '.']],
    ]

    result = get_required_shapes(shapes, required_counts)

    assert result == expected

sample_input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###
"""

def test_parses_shapes():
    expected_shapes = [
        [['#', '#', '#'], 
         ['#', '#', '.'], 
         ['#', '#', '.']],
        [['#', '#', '#'], 
         ['#', '#', '.'], 
         ['.', '#', '#']],
        [['.', '#', '#'], 
         ['#', '#', '#'], 
         ['#', '#', '.']],        
        [['#', '#', '.'], 
         ['#', '#', '#'], 
         ['#', '#', '.']],
        [['#', '#', '#'], 
        ['#', '.', '.'], 
        ['#', '#', '#']],
        [['#', '#', '#'], 
         ['.', '#', '.'], 
         ['#', '#', '#']],
    ]

    result_shapes = parse_shapes(sample_input)

    assert result_shapes == expected_shapes

def rotate_right(shape):
    return [list(reversed(col)) for col in zip(*shape)]

def flip_horizontally(shape):
    return [list(reversed(row)) for row in shape]

def flip_vertically(shape):
    return shape[::-1]

def parse_line_to_requirements(line):
    size_part, counts_part = line.split(":")

    size = [int(x) for x in size_part.split("x")]
    counts = [int(x) for x in counts_part.strip().split(" ")]

    return size, counts

def empty_grid(width, height, item):
    return [[item for _ in range(width)] for _ in range(height)]

def place_shapes(grid, placement_data):
    # grid: [['.', '.', '.'], ... ]
    # placement_data: [ (shape, x, y), ... ]
    # x and y are the top-left corner where the shape is placed
    # Output: updated_grid, occupancy_grid
    # updated_grid: [['#', '.', '#'], ['#', '#', '#'] ]
    # occupancy_grid: [[1, 1, 1], ... ] where the number indicates how many shapes cover that cell

    grid_width, grid_height = get_grid_dimensions(grid)
    occupancy_grid = empty_grid(grid_width, grid_height, 0)
    updated_grid = [row[:] for row in grid]

    for _, (shape, x_offset, y_offset) in enumerate(placement_data):
        shape_height = len(shape)
        shape_width = len(shape[0]) if shape_height > 0 else 0

        for y in range(shape_height):
            for x in range(shape_width):
                if shape[y][x] == '#':
                    grid_x = x + x_offset
                    grid_y = y + y_offset

                    if 0 <= grid_x < grid_width and 0 <= grid_y < grid_height:
                        updated_grid[grid_y][grid_x] = '#'
                        occupancy_grid[grid_y][grid_x] += 1
                    else:
                        pass

    return updated_grid, occupancy_grid

def get_grid_dimensions(grid):
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    return width, height

def get_occupancy_grid(grid_width, grid_height, placement_data):
    # placement_data: (shape, x, y)
    occupancy_grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
    for shape, x_offset, y_offset in placement_data:
        shape_height = len(shape)
        shape_width = len(shape[0]) if shape_height > 0 else 0

        for y in range(shape_height):
            for x in range(shape_width):
                if shape[y][x] == '#':
                    occupancy_grid[y + y_offset][x + x_offset] += 1

    return occupancy_grid

def get_max_x_and_y(grid_width, grid_height):
    return grid_width - 3, grid_height - 3

def parse_shapes(input):
    shapes = []
    shape_blocks = input.strip().split("\n\n")
    for block in shape_blocks:
        lines = block.strip().split("\n")
        shape = [list(line) for line in lines[1:]]
        shapes.append(shape)

    return shapes

def test_input_part_one():
    with open(r"c:/Projects/playground/aoc2025/12/input.txt", encoding='utf-8') as f:
        lines = f.read()

        requirement_index = 1
        for line in lines.splitlines():
            if 'x' in line:
                break
            requirement_index += 1

        split_lines = lines.splitlines()
        shape_lines = split_lines[0:requirement_index - 1]
        requirement_lines = split_lines[requirement_index - 1:]

        shape_line = '\n'.join(shape_lines)

        shapes = parse_shapes(shape_line)

        # for requirement_line in requirement_lines:
        #     expected_size, expected_counts = parse_line_to_requirements(requirement_line)

        #     _ = ga_for_placement_in_grid(shapes, expected_size, expected_counts)

    assert True

def test_fitness_function():
    good_occupancy_grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ]
    worse_occupancy_grid = [
        [0, 1, 0],
        [2, 2, 1],
        [0, 1, 0],
    ]
    even_worse_occupancy_grid = [
        [0, 2, 0],
        [3, 2, 1],
        [0, 1, 0],
    ]
    good_fitness = fitness_function(good_occupancy_grid)
    worse_fitness = fitness_function(worse_occupancy_grid)
    even_worse_fitness = fitness_function(even_worse_occupancy_grid)

    assert good_fitness < worse_fitness
    assert worse_fitness < even_worse_fitness

def test_create_population_with_no_best_individual():
    required_shapes = [
        [['#', '#'], ['#', '#']],
        [['#', '#', '#'], ['.', '#', '.']],
    ]
    population_size = 10
    max_x = 5
    max_y = 5
    best_individual = None

    population = create_population(population_size, required_shapes, max_x, max_y, best_individual)

    assert len(population) == population_size

    for individual in population:
        assert len(individual) == len(required_shapes)

        for item in individual:
            num_rotations, flipped_horizontally, flipped_vertically, x, y = item

            assert num_rotations in [0, 1, 2, 3]
            assert flipped_horizontally in [True, False]
            assert flipped_vertically in [True, False]
            assert 0 <= x <= max_x
            assert 0 <= y <= max_y

def test_applies_transformations():
    shape = [
        ['#', '.', '#'],
        ['#', '.', '#'],
        ['#', '#', '#'],
    ]

    transformed_shape = apply_transformations(shape, 1, True, False)

    expected_shape = [
        ['#', '#', '#'],
        ['.', '.', '#'],
        ['#', '#', '#'],
    ]

    assert transformed_shape == expected_shape

def test_ga_debug():
    shapes = [
        [['#', '#', '#'], 
         ['#', '#', '.'], 
         ['#', '#', '.']],
        [['#', '#', '#'], 
         ['#', '#', '.'], 
         ['.', '#', '#']],
        [['.', '#', '#'], 
         ['#', '#', '#'], 
         ['#', '#', '.']],        
        [['#', '#', '.'], 
         ['#', '#', '#'], 
         ['#', '#', '.']],
        [['#', '#', '#'], 
        ['#', '.', '.'], 
        ['#', '#', '#']],
        [['#', '#', '#'], 
         ['.', '#', '.'], 
         ['#', '#', '#']],
    ]
    size = [4, 4]
    counts = [0, 0, 0, 0, 2, 0]

    best_individual = ga_for_placement_in_grid(shapes, size, counts)

    visualize_individual(best_individual, shapes, size, counts, False)

    assert True

# def test_ga_with_bigger_sample():
#     shapes = parse_shapes(sample_input)
#     size = [12, 5]
#     counts = [1, 0, 1, 0, 2, 2]

#     best_individual = ga_for_placement_in_grid(shapes, size, counts)

#     visualize_individual(best_individual, shapes, size, counts, False)

#     assert True

def get_required_shapes(shapes, required_counts):
    required_shapes = []
    for shape, count in zip(shapes, required_counts):
        for _ in range(count):
            required_shapes.append(shape)

    return required_shapes

def fitness_function(occupancy_grid):
    single_occupancy_count = 0
    overlaps = []

    for row in occupancy_grid:
        for cell in row:
            if cell == 1:
                single_occupancy_count += 1
            elif cell > 1:
                overlaps.append(cell + cell)

    return single_occupancy_count + sum(overlaps)

def create_population(population_size, required_shapes, max_x, max_y, best_individual):
    # individual: [
    #   (num_rotations, flipped_horizontally, flipped_vertically, x, y),
    #   (num_rotations, flipped_horizontally, flipped_vertically, x, y),
    #   ...
    # ]
    # individual length is the same as required_shapes length
    # num_rotations: random pick from 0, 1, 2, 3
    # flipped_horizontally: random pick from True, False
    # flipped_vertically: random pick from True, False
    # x: random pick from 0 to max_x
    # y: random pick from 0 to max_y
    # The above apply when best_individual is None
    # When best_individual is provided, create a new individual by slightly mutating the best_individual

    population = []
    flip_probability = 0.1
    max_rotations = 4

    if best_individual is None:
        for _ in range(population_size):
            individual = []
            duplicate = True
            while duplicate:
                for shape_index, _ in enumerate(required_shapes):
                    individual.append(create_random_individual(max_rotations, max_x, max_y))

                if individual not in population:
                    duplicate = False

            population.append(individual)
        return population
    else:
        for _ in range(population_size):
            individual = []
            duplicate = True
            while duplicate:
                for shape_index, _ in enumerate(required_shapes):
                    best_item = best_individual[shape_index]
                    individual.append(create_mutated_individual(best_item, max_rotations, max_x, max_y, flip_probability))

                if individual not in population:
                    duplicate = False

            population.append(individual)

        # Ensure best individual is retained
        population[0] = best_individual

    return population

def create_random_individual(max_rotations, max_x, max_y):
    num_rotations = np.random.randint(0, max_rotations)
    flipped_horizontally = np.random.choice([True, False])
    flipped_vertically = np.random.choice([True, False])
    x = np.random.randint(0, max_x + 1)
    y = np.random.randint(0, max_y + 1)

    return (num_rotations, flipped_horizontally, flipped_vertically, x, y)

def create_mutated_individual(best_item, max_rotations, max_x, max_y, flip_probability):
    max_spread = 1
    min_spread = -1 * max_spread

    num_rotations = (best_item[0] + np.random.choice([min_spread, 0, max_spread])) % max_rotations
    flipped_horizontally = best_item[1] if np.random.rand() > flip_probability else not best_item[1]
    flipped_vertically = best_item[2] if np.random.rand() > flip_probability else not best_item[2]
    x = min(max(best_item[3] + np.random.choice([min_spread, 0, max_spread]), 0), max_x)
    y = min(max(best_item[4] + np.random.choice([min_spread, 0, max_spread]), 0), max_y)

    return (num_rotations, flipped_horizontally, flipped_vertically, x, y)

def ga_for_placement_in_grid(shapes, expected_size, expected_counts):
    required_shapes = get_required_shapes(shapes, expected_counts)
    grid_width, grid_height = expected_size
    max_x, max_y = get_max_x_and_y(grid_width, grid_height)

    population_size = 150
    max_generation_count = 50

    generation = 0
    best_individual = None
    best_fitness = np.inf
    best_occupancy_grid = None

    while generation < max_generation_count:
        population = create_population(population_size, required_shapes, max_x, max_y, best_individual)

        for individual in population:
            placement_data = []
            for shape, item in zip(required_shapes, individual):
                num_rotations, flipped_horizontally, flipped_vertically, x, y = item
                transformed_shape = apply_transformations(shape, num_rotations, flipped_horizontally, flipped_vertically)
                placement_data.append((transformed_shape, x, y))

            occupancy_grid = get_occupancy_grid(grid_width, grid_height, placement_data)
            empty_grid_for_placement = empty_grid(grid_width, grid_height, '.')

            # Acutal placement
            _, occupancy_grid = place_shapes(empty_grid_for_placement, placement_data)

            fitness = fitness_function(occupancy_grid)

            if fitness < best_fitness:
                best_fitness = fitness
                best_individual = individual
                best_occupancy_grid = occupancy_grid

        if generation == max_generation_count - 1 and has_any_overlap(best_occupancy_grid):
            generation = 0

            visualize_individual(best_individual, shapes, expected_size, expected_counts, placement=False)

            best_individual = None
            best_fitness = np.inf
            best_occupancy_grid = None

        generation += 1

    return best_individual

def visualize_individual(individual, shapes, expected_size, expected_counts, placement=True):
    print()

    required_shapes = get_required_shapes(shapes, expected_counts)
    grid_width, grid_height = expected_size
    placement_data = []
    for shape, item in zip(required_shapes, individual):
        num_rotations, flipped_horizontally, flipped_vertically, x, y = item
        transformed_shape = apply_transformations(shape, num_rotations, flipped_horizontally, flipped_vertically)
        for line in transformed_shape:
            if placement:
                print(line)

        placement_data.append((transformed_shape, x, y))
        if placement:
            print(f"Placed at: ({x}, {y})\n")

    empty_grid_for_placement = empty_grid(grid_width, grid_height, '.')
    result_grid, occupancy_grid = place_shapes(empty_grid_for_placement, placement_data)

    print("Resulting Grid:")
    for row in result_grid:
        print(''.join(row))

    print("\nOccupancy Grid:")
    for row in occupancy_grid:
        print(' '.join(str(cell) for cell in row))

    # Total number of cells in occupancy grid that have occupancy greater than 1
    overlap_occupied_cells = sum(1 for row in occupancy_grid for cell in row if cell > 1)
    print(f"\nTotal overlapping occupied cells: {overlap_occupied_cells}")

def has_any_overlap(occupancy_grid):
    return sum(1 for row in occupancy_grid for cell in row if cell > 1) > 0

def apply_transformations(shape, num_rotations, flipped_horizontally, flipped_vertically):
    transformed_shape = shape
    for _ in range(num_rotations):
        transformed_shape = rotate_right(transformed_shape)
    if flipped_horizontally:
        transformed_shape = flip_horizontally(transformed_shape)
    if flipped_vertically:
        transformed_shape = flip_vertically(transformed_shape)

    return transformed_shape