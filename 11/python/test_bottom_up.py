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

def process_all_identifiers(input):
    identifier_data = initialize_nodes(input)
    connection_map = create_connections(input)

    output = identifier_data.copy()

    identifiers_to_process = find_starting_identifiers(input)
    processed_count = 0
    max_processed_count = len(identifier_data)

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

    while processed_count < max_processed_count:
        identifiers_to_process_next = []
        for identifier in identifiers_to_process:
            output = process_single_identifier(identifier, output, connection_map)
            processed_count += 1

            connected_identifiers = get_identifiers_connected_to(identifier, connection_map)
            identifiers_to_process_next.extend(connected_identifiers)

        identifiers_to_process = identifiers_to_process_next

    return output

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