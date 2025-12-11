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
    paths_to_out = find_all_paths_to_out(input)

    assert len(paths_to_out) == 5

def test_filter_only_paths_with_fft_and_dac():
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

    paths_to_out_with_fft_and_dac = find_all_paths_to_out_fft_dac(input, 'svr', 'out', ['fft', 'dac'])

    expected_path_count = 2

    assert len(paths_to_out_with_fft_and_dac) == expected_path_count

def test_filter_paths_real_input_small():
    input = """svr: pxq fmq ggx ora
pxq: vay ftt nzt lkf fnt xtu sju zpf ydd qsi dxm gnw rxt dzu pci lml rfx swg fkw gpo
ftt: cys mro
mro: xjj fkd eej
ora: krs fkw qsi lkf sju lml rfx gnw rxt pci
"""

    start_identifier = 'svr'
    end_identifier = 'mro'

    paths = find_all_paths_to_out_fft_dac(input, start_identifier, end_identifier, ['ftt'])

    expected_path_count = 1

    assert len(paths) == expected_path_count

def test_insert_last_identifier_if_paths_are_empty():
    completed_path = ['hpc', 'lgk', 'out']
    paths_to_skip = []

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['lgk']

    assert updated_paths == expected_paths

def test_prepends_previous_identifier_if_last_exists_in_paths():
    completed_path = ['hpc', 'lgk', 'out']
    paths_to_skip = ['lgk']

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['hpc', 'lgk']

    assert updated_paths == expected_paths

    completed_path = ['abc', 'hpc', 'lgk', 'out']
    paths_to_skip = ['hpc', 'lgk']

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['abc', 'hpc', 'lgk']

    assert updated_paths == expected_paths

    completed_path = ['xyz', 'abc', 'hpc', 'lgk', 'out']
    paths_to_skip = ['abc', 'hpc', 'lgk']

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['xyz','abc', 'hpc', 'lgk']

    assert updated_paths == expected_paths
    
def test_does_not_update_paths_when_completed_path_contains_fft():
    completed_path = ['fft', 'lgk', 'out']
    paths_to_skip = []

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = []

    assert updated_paths == expected_paths

    paths_to_skip = ['abc']

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['abc']

    assert updated_paths == expected_paths

def test_does_not_update_paths_when_completed_path_contains_dac():
    completed_path = ['dac', 'lgk', 'out']
    paths_to_skip = []

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = []

    assert updated_paths == expected_paths

    paths_to_skip = ['abc']

    updated_paths = update_paths_to_skip(completed_path, paths_to_skip)

    expected_paths = ['abc']

    assert updated_paths == expected_paths

def test_updates_paths_to_skip_when_an_output_is_in_paths_to_skip():
    current_identifier = 'hpc'
    outputs = ['lgk', 'xyz']
    paths_to_skip = ['lgk']

    updated_paths = update_identifiers_to_skip(current_identifier, outputs, paths_to_skip)

    expected_paths = ['hpc', 'lgk']

    assert updated_paths == expected_paths

    current_identifier = 'fft'

    updated_paths = update_identifiers_to_skip(current_identifier, outputs, paths_to_skip)

    assert updated_paths == expected_paths

def find_input(input, identifier='you'):
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

def find_all_paths_to_out(input, input_identifier='you'):
    end_identifier = 'out'
    line_index = find_input(input, identifier=input_identifier)
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

    return paths_to_out

def find_all_paths_to_out_fft_dac(input, input_identifier='you', end_identifier='out', nodes_of_interest=[], stop_after_found_count=None):
    line_index = find_input(input, identifier=input_identifier)
    if line_index is None:
        return []
    outputs = get_outputs_from_line(input, line_index)

    paths_to_out = []
    stack = [(output, [output]) for output in outputs]
    paths_to_skip = []

    print()

    while stack:
        current_identifier, path = stack.pop()
        if current_identifier == end_identifier:
            continue
        current_line_index = find_input(input, identifier=current_identifier)
        if current_line_index is None:
            continue
        current_outputs = get_outputs_from_line(input, current_line_index)
        
        paths_to_skip = update_identifiers_to_skip(current_identifier, current_outputs, paths_to_skip)

        if current_identifier in paths_to_skip:
            continue

        # Comment to test out original logic
        current_outputs = [output for output in current_outputs if output not in paths_to_skip]

        for output in current_outputs:
            if output == end_identifier:
                if (len(nodes_of_interest) == 0) or all(node in path for node in nodes_of_interest):
                    path = path + [output]
                    paths_to_out.append(path)
                    # Comment to test out original logic
                    paths_to_skip = update_paths_to_skip(path, paths_to_skip)

                    if stop_after_found_count is not None and len(paths_to_out) >= stop_after_found_count:
                        return paths_to_out
            elif output not in path:
                stack.append((output, path + [output]))

    return paths_to_out

def update_paths_to_skip(completed_path, paths_to_skip):
    if 'fft' in completed_path or 'dac' in completed_path:
        return paths_to_skip

    if not paths_to_skip:
        last_before_out = completed_path[-2]
        paths_to_skip.append(last_before_out)
    else:
        index = -2
        while completed_path[index] in paths_to_skip:
            index -= 1
            if abs(index) > len(completed_path):
                break
        previous_identifier = completed_path[index]
        paths_to_skip.insert(0, previous_identifier)

    return paths_to_skip

def update_identifiers_to_skip(current_identifier, outputs, paths_to_skip):
    if current_identifier == 'fft' or current_identifier == 'dac':
        return paths_to_skip
    
    if all(skip in outputs for skip in paths_to_skip):
        paths_to_skip.insert(0, current_identifier)

    return paths_to_skip

# def test_input_part_one():
#     with open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8') as f:
#         lines = f.read()
#         paths_to_out = find_all_paths_to_out(lines)
#         print(f"Part One: {len(paths_to_out)}")
#     assert True

# def test_input_part_two_small_one():
#     with open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8') as f:
#         lines = f.read()
#         start_identifier = 'svr'
#         end_identifier = 'out'

#     assert True
