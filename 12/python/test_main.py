import pytest

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

    for index, (shape, x_offset, y_offset) in enumerate(placement_data):
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

# def test_input_part_one():
#     with open(r"c:/Projects/playground/aoc2025/12/input.txt", encoding='utf-8') as f:
#         total_counts = 0
#         lines = f.read()

#         for line in f:
#             print()

#     assert True
