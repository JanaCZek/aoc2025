def test_finds_input():
    input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    expected_index = 1

    assert find_input(input) == expected_index

def test_finds_outputs_on_line():
    input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    line_index = 1
    expected_outputs = ['bbb', 'ccc']

    assert get_outputs_from_line(input, line_index) == expected_outputs

def test_feed_output_into_input():
    input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    line_index = find_input(input)
    expected_index = 1

    assert line_index == expected_index

    outputs = get_outputs_from_line(input, line_index)
    expected_outputs = ['bbb', 'ccc']

    assert outputs == expected_outputs

    first_feed = find_input(input, identifier=outputs[0])

    assert first_feed == 2

    second_feed = find_input(input, identifier=outputs[1])

    assert second_feed == 3

def test_finds_all_paths_to_out():
    input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    paths_to_out = find_count_of_all_paths_to_out(input)

    assert paths_to_out == 5

def find_input(input, identifier='you'):
    line_index = 0
    identifier_with_colon = identifier + ':'

    for line in input.splitlines():
        if identifier_with_colon in line:
            return line_index
        line_index += 1

    return 0

def get_outputs_from_line(input, line_index):
    lines = input.splitlines()
    line = lines[line_index]
    parts = line.split(':')
    
    outputs_part = parts[1].strip()
    outputs = outputs_part.split(' ')

    return outputs

def find_count_of_all_paths_to_out(input):
    end_identifier = 'out'
    line_index = find_input(input)
    outputs = get_outputs_from_line(input, line_index)

    paths_to_out = []
    stack = [(output, [output]) for output in outputs]
    while stack:
        current_identifier, path = stack.pop()
        current_line_index = find_input(input, identifier=current_identifier)
        current_outputs = get_outputs_from_line(input, current_line_index)

        for output in current_outputs:
            if output == end_identifier:
                paths_to_out.append(path + [output])
            else:
                stack.append((output, path + [output]))
    return len(paths_to_out)

def test_input_part_one():
    with open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8') as f:
        lines = f.read()
        paths_to_out = find_count_of_all_paths_to_out(lines)
        print(f"Part One: {paths_to_out}")
    assert True
