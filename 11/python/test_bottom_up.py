sample_input = """svr: aaa bbb
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

def test_intializes_nodes():
    expected_nodes = [
        ['svr', ['svr'], 2, 0],
        ['aaa', ['fft'], 1, 0],
        ['fft', ['fft'], 1, 0],
        ['bbb', [], 1, 0],
        ['tty', [], 1, 0],
        ['ccc', [], 2, 0],
        ['ddd', [], 1, 0],
        ['hub', [], 1, 0],
        ['eee', ['dac'], 1, 0],
        ['dac', ['dac'], 1, 0],
        ['fff', [], 2, 0],
        ['ggg', ['out'], 1, 0],
        ['hhh', ['out'], 1, 0],
    ]

    nodes = initialize_nodes(sample_input)

    assert nodes == expected_nodes

def test_two_different_identifier_data_are_not_equal():
    data_one = [
        ['svr', ['svr'], 2, 0],
        ['aaa', ['fft'], 1, 0],
    ]
    data_two = [
        ['svr', ['svr', 'fft'], 2, 1],
        ['aaa', ['fft'], 1, 0],
    ]

    assert data_one != data_two

def test_identifies_duplicate():
    item = ['svr', ['svr'], 2, 0]
    list_of_data = [
        item
    ]

    assert item in list_of_data

def test_finds_starting_identifiers():
    input = """svr: aaa bbb
aaa: out
bbb: out
"""
    expected_starting_identifiers = ['aaa', 'bbb']

    starting_identifiers = find_starting_identifiers(input)

    assert starting_identifiers == expected_starting_identifiers


identifiers_of_interest = {'svr', 'fft', 'dac', 'out'}

def test_creates_connection_map():
    expected_map = [
        ['svr', ['aaa', 'bbb']],
        ['aaa', ['fft']],
        ['fft', ['ccc']],
        ['bbb', ['tty']],
        ['tty', ['ccc']],
        ['ccc', ['ddd', 'eee']],
        ['ddd', ['hub']],
        ['hub', ['fff']],
        ['eee', ['dac']],
        ['dac', ['fff']],
        ['fff', ['ggg', 'hhh']],
        ['ggg', ['out']],
        ['hhh', ['out']],
    ]

    connection_map = create_connections(sample_input)

    assert connection_map == expected_map

def test_gets_identifiers_connected_to():
    connection_map = create_connections(sample_input)

    connected_to_fft = get_identifiers_connected_to('fft', connection_map)
    expected_connected_to_fft = ['aaa']

    assert connected_to_fft == expected_connected_to_fft

    connected_to_dac = get_identifiers_connected_to('dac', connection_map)
    expected_connected_to_dac = ['eee']

    assert connected_to_dac == expected_connected_to_dac

    connected_to_out = get_identifiers_connected_to('out', connection_map)
    expected_connected_to_out = ['ggg', 'hhh']

    assert connected_to_out == expected_connected_to_out

def test_process_single_indentifier():
    identifier_data = initialize_nodes(sample_input)
    connection_map = create_connections(sample_input)

    updated_identifier_data = process_single_identifier(identifier_data[-1][0], identifier_data, connection_map)

    expected_updated_record = ['fff', ['out'], 2, 1]

    assert expected_updated_record in updated_identifier_data

    updated_identifier_data = process_single_identifier(identifier_data[-3][0], updated_identifier_data, connection_map)

    expected_updated_records = [
        ['dac', ['dac', 'out'], 1, 1],
        ['hub', ['out'], 1, 1],
    ]

    for record in expected_updated_records:
        assert record in updated_identifier_data

def test_process_all_identifiers():
    input = """svr: uvz ucg
uvz: fft
ucg: dac
fft: oll
dac: uhp
xwe: vol
oll: vol
uhp: zmp
mig: xtq
vol: out
xtq: out
zmp: out
"""

    updated_identifier_data = process_all_identifiers(input)

    expected_updated_records = [
        ['svr', ['svr', 'fft', 'dac', 'out'], 2, 2],
        ['uvz', ['fft', 'out'], 1, 1],
        ['ucg', ['dac', 'out'], 1, 1],
        ['fft', ['fft', 'out'], 1, 1],
        ['dac', ['dac', 'out'], 1, 1],
        ['oll', ['out'], 1, 1],
        ['uhp', ['out'], 1, 1],
        ['vol', ['out'], 1, 1],
        ['xwe', ['out'], 1, 1],
        ['mig', ['out'], 1, 1],
        ['xtq', ['out'], 1, 1],
        ['zmp', ['out'], 1, 1],
    ]

    for i in range(len(expected_updated_records)):
        identifier = expected_updated_records[i][0]
        actual = []
        for record in updated_identifier_data:
            if record[0] == identifier:
                actual = record
                break
        expected = expected_updated_records[i]

        assert_identifier_record(actual, expected)

def assert_identifier_record(actual, expected):
    assert actual[0] == expected[0]
    assert set(actual[1]) == set(expected[1])
    assert actual[2] == expected[2]
    assert actual[3] == expected[3]

def test_process_all_simple():
    input = """svr: dac
dac: fft
fft: ddd
ddd: aaa ccc
ccc: bbb
bbb: out
aaa: out
"""
    expected_updated_records = [
        ['svr', ['svr', 'dac', 'fft', 'out'], 1, 2],
        ['dac', ['dac', 'fft', 'out'], 1, 2],
        ['fft', ['fft', 'out'], 1, 2],
        ['ddd', ['out'], 2, 2],
        ['aaa', ['out'], 1, 1],
        ['ccc', ['out'], 1, 1],
        ['bbb', ['out'], 1, 1]
    ]

    updated_identifier_data = process_all_identifiers(input)

    for i in range(len(expected_updated_records)):
        identifier = expected_updated_records[i][0]
        actual = []
        for record in updated_identifier_data:
            if record[0] == identifier:
                actual = record
                break
        expected = expected_updated_records[i]

        assert_identifier_record(actual, expected)

def test_get_paths_of_interest():
    input = """svr: dac
dac: fft
fft: ddd
ddd: aaa ccc
ccc: bbb
bbb: out
aaa: out
"""

    expected_paths = [
        ['svr', 'dac', 'fft', 'ddd', 'aaa', 'out'],
        ['svr', 'dac', 'fft', 'ddd', 'ccc', 'bbb', 'out'],
    ]
    connection_map = create_connections(input)
    identifier_data = process_all_identifiers(input)

    paths = get_paths_of_interest(identifier_data, connection_map)

    assert len(paths) == 2

    for expected_path in expected_paths:
        assert expected_path in paths 

def test_skip_path_if_not_relevant():
    input = """svr: dac xyz
dac: fft
fft: ddd
ddd: aaa ccc
ccc: bbb
bbb: out
aaa: out
xyz: out
"""

    expected_paths = [
        ['svr', 'dac', 'fft', 'ddd', 'aaa', 'out'],
        ['svr', 'dac', 'fft', 'ddd', 'ccc', 'bbb', 'out'],
    ]
    connection_map = create_connections(input)
    identifier_data = process_all_identifiers(input)

    paths = get_paths_of_interest(identifier_data, connection_map)

    for path in paths:
        print("Found path:", path)

    assert len(paths) == 2

    for expected_path in expected_paths:
        assert expected_path in paths

def test_input_part_two_small_one():
    with open(r"c:/Projects/playground/aoc2025/11/input.txt", encoding='utf-8') as f:
        lines = f.read()
        data = process_all_identifiers(lines)

        print("Output")
        for item in data:
            if {'fft', 'dac', 'out'}.issubset(set(item[1])):
                print(item)

        paths = get_paths_of_interest(data, create_connections(lines))

        print("Paths of interest", len(paths))
        for path in paths:
            print(path)

    assert True

def initialize_nodes(input):
    # output: [ identifier, [ identifiers_of_interest_found ], total_connections, traversed_connections ]
    output = []
    for line in input.strip().split('\n'):
        parts = line.split(':')
        identifier = parts[0].strip()
        connections = parts[1].strip().split() if len(parts) > 1 else []
        found_identifiers_of_interest = []
        for conn in connections:
            if conn in identifiers_of_interest:
                found_identifiers_of_interest.append(conn)
        if identifier in identifiers_of_interest:
            found_identifiers_of_interest.insert(0, identifier)

        output.append([identifier, found_identifiers_of_interest, len(connections), 0])

    return output

def find_starting_identifiers(input):
    starting_identifiers = []

    for line in input.strip().split('\n'):
        parts = line.split(':')
        identifier = parts[0].strip()
        connections = parts[1].strip().split() if len(parts) > 1 else []

        if len(connections) == 1 and connections[0] == 'out':
            starting_identifiers.append(identifier)

    return starting_identifiers

def create_connections(input):
    connection_map = []

    for line in input.strip().split('\n'):
        parts = line.split(':')
        identifier = parts[0].strip()
        connections = parts[1].strip().split() if len(parts) > 1 else []

        connection_map.append([identifier, connections])

    return connection_map

def get_identifiers_connected_to(identifier, connection_map):
    connections = []

    for conn in connection_map:
        if identifier in conn[1]:
            connections.append(conn[0])

    return connections

def get_connections_of_identifier(identifier, connection_map):
    for conn in connection_map:
        if conn[0] == identifier:
            return conn[1]
    return []

def process_all_identifiers(input):
    identifier_data = initialize_nodes(input)
    connection_map = create_connections(input)

    output = identifier_data.copy()

    identifiers_to_process = find_starting_identifiers(input)

    for identifier in identifiers_to_process:
        data = []
        for record in output:
            if record[0] == identifier:
                data = record
                break
        data[3] += 1  # Increment traversed connections
        for record in output:
            if record[0] == identifier:
                record[3] = data[3]
                break

    previous = []
    current = output

    while current != previous:
        identifiers_to_process_next = []
        previous = current.copy()

        for identifier in identifiers_to_process:
            current = process_single_identifier(identifier, current, connection_map)
            
            connected_identifiers = get_identifiers_connected_to(identifier, connection_map)
            identifiers_to_process_next.extend(connected_identifiers)

        identifiers_to_process = list(set(identifiers_to_process_next))

    return current

def process_single_identifier(identifier, identifier_data, connection_map):
    single_identifier_data = []
    for data in identifier_data:
        if data[0] == identifier:
            single_identifier_data = data
            break

    connected_identifiers = get_identifiers_connected_to(identifier, connection_map)

    updated_records = []

    for connected_identifier in connected_identifiers:
        for record in identifier_data:
            if record[0] == connected_identifier:
                updated_identifiers_of_interest = record[1].copy()
                for item in single_identifier_data[1]:
                    if item not in updated_identifiers_of_interest:
                        updated_identifiers_of_interest.append(item)
                updated_total_connections = record[2]
                updated_traversed_connections = record[3] + 1

                updated_record = [
                    record[0],
                    updated_identifiers_of_interest,
                    updated_total_connections,
                    updated_traversed_connections
                ]

                updated_records.append(updated_record)
                
    output = identifier_data.copy()
    for updated_record in updated_records:
        for i in range(len(output)):
            if output[i][0] == updated_record[0]:
                output[i] = updated_record

    return output

def get_paths_of_interest(identifier_data, connection_map):
    paths = []
    paths_count = 0
    relevant_connections = []
    for record in identifier_data:
        if set(['fft', 'dac', 'out']) == set(record[1]):
            relevant_connections.append(record[0])

    connections = get_connections_of_identifier('svr', connection_map)

    # Traverse all paths from 'svr' to 'out' that go through relevant connections
    # Use a stack for depth-first search
    # A path must either go through a relevant connection, or if it contains 'fft' then the next connection must contain ['dac','out']
    # A path must either go through a relevant connection, or if it contains 'dac' then the next connection must contain ['fft','out']
    # A path must either go through a relevant connection, or if it contains both 'dac' and 'fft' then the next connection must contain ['out']
    stack = [(['svr'], connections)]
    while stack:
        current_path, current_connections = stack.pop()
        for conn in current_connections:
            new_path = current_path + [conn]
            if conn == 'out':
                # print(new_path)
                # paths.append(new_path)
                paths_count += 1
            else:
                next_connections = get_connections_of_identifier(conn, connection_map)
                if conn in relevant_connections:
                    stack.append((new_path, next_connections))
                else:
                    contains_fft = 'fft' in new_path
                    contains_dac = 'dac' in new_path
                    if contains_fft and not contains_dac:
                        for next_conn in next_connections:
                            for record in identifier_data:
                                if record[0] == next_conn and set(['dac', 'out']).issubset(set(record[1])):
                                    stack.append((new_path, [next_conn]))
                    elif contains_dac and not contains_fft:
                        for next_conn in next_connections:
                            for record in identifier_data:
                                if record[0] == next_conn and set(['fft', 'out']).issubset(set(record[1])):
                                    stack.append((new_path, [next_conn]))
                    elif contains_dac and contains_fft:
                        for next_conn in next_connections:
                            for record in identifier_data:
                                if (record[0] == next_conn and 'out' in record[1]) or next_conn == 'out':
                                    stack.append((new_path, [next_conn]))
    
    print("Total paths of interest found:", paths_count)
    
    return paths
