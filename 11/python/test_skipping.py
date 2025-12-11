import pytest

def test_prefills_output_identifiers_to_skip():
    input = """aaa: bbb ccc
you: ddd eee
bbb: out
ccc: out
ddd: fff
"""
    expected_identifiers_to_skip = ['bbb', 'ccc']
    identifiers_to_skip = prefill_output_identifiers_to_skip(input)

    assert identifiers_to_skip == expected_identifiers_to_skip

@pytest.mark.parametrize("path, identifiers_to_skip", [
    (['aaa', 'bbb', 'ccc'], ['ddd', 'eee']),
    (['fft', 'bbb'], ['bbb']),
    (['dac', 'bbb'], ['bbb']),
    (['bbb', 'fft'], ['bbb']),
    (['bbb', 'dac'], ['bbb']),
    (['bbb', 'dac', 'fft'], ['bbb']),
    (['bbb', 'fft', 'dac'], ['bbb']),
])
def test_should_continue_on_path(path, identifiers_to_skip):
    assert continue_on_path(path, identifiers_to_skip) == True

@pytest.mark.parametrize("path, identifiers_to_skip", [
    (['aaa', 'bbb', 'ccc'], ['ccc']),
])
def test_should_not_continue_on_path(path, identifiers_to_skip):
    assert continue_on_path(path, identifiers_to_skip) == False

@pytest.mark.parametrize("input, expected_paths", [
    ("""svr: aaa bbb
aaa: out
bbb: out
""", []),

    ("""svr: fft aaa
fft: dac
aaa: out
dac: out
""", [['svr', 'fft', 'dac', 'out']]),
])
def test_traverses_both_branches_in_graph(input, expected_paths):
    paths = find_all_paths_from_svr_to_out_over_fft_dac_with_skipping(input)

    assert paths == expected_paths

def test_traverse_sample_data():
    input = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
    expected_path_count = 2
    paths = find_all_paths_from_svr_to_out_over_fft_dac_with_skipping(input)

    assert len(paths) == expected_path_count

def test_skipping():
    input = """svr: ita sbh
ita: xwe oll sjz hpc ops
sbh: xwe oll sjz hpc ops
xwe: fft
oll: fft lgk
sjz: fft lgk
hpc: lgk
ops: lgk abc
fft: dac
dac: out
lgk: out
abc: out
"""
    expected_path_count = 6
    paths = find_all_paths_from_svr_to_out_over_fft_dac_with_skipping(input)

    assert len(paths) == expected_path_count


def test_input_part_two_small_one():
    with open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8') as f:
        lines = f.read()
        paths = find_all_paths_from_svr_to_out_over_fft_dac_with_skipping(lines)

        print(f"Part Two Small One: {len(paths)}")

    assert True

input_identifier='svr'
end_identifier='out'
identifiers_of_interest = ['fft', 'dac'] 

def find_all_paths_from_svr_to_out_over_fft_dac_with_skipping(input):
    line_index = find_input_index(input, input_identifier)
    if line_index is None:
        return []
    outputs = get_outputs_from_line(input, line_index)

    paths_to_out = []
    stack = [(output, [input_identifier] + [output]) for output in outputs]
    identifiers_to_skip = prefill_output_identifiers_to_skip(input)

    while stack:
        current_identifier, path = stack.pop()
        current_line_index = find_input_index(input, identifier=current_identifier)

        if current_line_index is None:
            continue
    
        current_outputs = get_outputs_from_line(input, current_line_index)

        identifiers_to_check = [identifier for identifier in identifiers_to_skip if identifier not in identifiers_of_interest]

        if is_identifier_of_interest_in_path(path) == False and all(output in identifiers_to_check for output in current_outputs):
            identifiers_to_skip.insert(0, current_identifier)
            print("Skipping on path:", path)
            print("Identifiers to skip:", len(identifiers_to_skip))
            continue

        for output in current_outputs:
            possible_path = path + [output]

            if possible_path[-1] == end_identifier:
                print(f"Reached out without fft/dac: {possible_path}")

            if possible_path[-1] == end_identifier and all(identifier in possible_path for identifier in identifiers_of_interest):
                paths_to_out.append(possible_path)
                print(f"Found path to out: {possible_path}")
                continue

            if continue_on_path(possible_path, identifiers_to_skip):
                stack.append((output, possible_path))

    return paths_to_out

def prefill_output_identifiers_to_skip(input):
    identifiers_to_skip = []
    lines = input.splitlines()

    for line in lines:
        parts = line.split(':')
        
        outputs_part = parts[1].strip()
        outputs = outputs_part.split(' ')

        if len(outputs) == 1 and outputs[0] == 'out':
            identifiers_to_skip.append(parts[0].strip())

    return identifiers_to_skip

def find_input_index(input, identifier='you'):
    line_index = 0
    identifier_with_colon = identifier + ':'

    for line in input.splitlines():
        if identifier_with_colon in line:
            return line_index
        line_index += 1

    return None

def get_outputs_from_line(input, line_index):
    lines = input.splitlines()
    line = lines[line_index]
    parts = line.split(':')
    
    outputs_part = parts[1].strip()
    outputs = outputs_part.split(' ')

    return outputs

def continue_on_path(path, identifiers_to_skip):
    if is_identifier_of_interest_in_path(path):
        return True
        
    if any(identifier in path for identifier in identifiers_to_skip):
        return False
        
    return True

def is_identifier_of_interest_in_path(path):
    return any(identifier in path for identifier in identifiers_of_interest)

# TODO:
# - Cycle detection
# - Be more strict with checking already traversed subgraphs