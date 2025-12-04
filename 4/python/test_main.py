def test_file():
    with open("C:\\Projects\\playground\\aoc2025\\4\\input.txt", "r") as file:
        data = file.read()
        trimmed_data = data.strip()
        
        accessible_paper_roles = detect_accessible_paper_rolls(trimmed_data)
        print(f"Accessible paper rolls: {accessible_paper_roles}")
    assert True == True

def test_detects_accessible_paper_rolls():
    grid = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    assert detect_accessible_paper_rolls(grid) == 13

def test_get_subgrid():
    grid = """..@@.@@@@."""

    assert get_all_paper_positions(grid) == [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8)]

    grid = """..@@.@@@@.
@@@.@.@.@@"""
    assert get_all_paper_positions(grid) == [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8),
                                             (1, 0), (1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 9)]

def test_get_adjacent_count():
    paper_positions = [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8),
                       (1, 0), (1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 9)]
    
    assert get_adjacent_count(paper_positions, (0, 2)) == 3
    assert get_adjacent_count(paper_positions, (0, 3)) == 3
    assert get_adjacent_count(paper_positions, (0, 5)) == 3

    paper_positions = [(0, 2), (0, 3), (0, 5), (0, 6), (0, 7), (0, 8),
                       (1, 0), (1, 1), (1, 2), (1, 4), (1, 6), (1, 8), (1, 9),
                       (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 6), (2, 8), (2, 9)]
    
    assert get_adjacent_count(paper_positions, (1, 0)) == 3

def get_adjacent_count(paper_positions, position):
    y, x = position
    adjacent_positions = [
        (y-1, x), (y+1, x),
        (y, x-1), (y, x+1),
        (y-1, x-1), (y-1, x+1),
        (y+1, x-1), (y+1, x+1)
    ]
    adjacent_positions = [(ay, ax) for ay, ax in adjacent_positions if ay >= 0 and ax >= 0]
    count = 0
    for adj in adjacent_positions:
        if adj in paper_positions:
            count += 1
    return count

def get_all_paper_positions(grid):
    positions = []
    for y, row in enumerate(grid.splitlines()):
        for x, cell in enumerate(row):
            if cell == '@':
                positions.append((y, x))
    return positions
    

def detect_accessible_paper_rolls(grid):
    paper_positions = get_all_paper_positions(grid)
    accessible_count = 0
    for position in paper_positions:
        if get_adjacent_count(paper_positions, position) < 4:
            accessible_count += 1
    return accessible_count