import numpy as np

def test_product_of__sizes_of_three_largest_junctions():
    input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    assert product_of_sizes_of_three_largest_junctions(input) == 40

def test_eucleidian_distance():
    assert eucleidian_distance(convert_string_to_3d_coordinate("162,817,812"), convert_string_to_3d_coordinate("425,690,689")) == 316.90219311326957113731618173808

def test_convert_string_to_3d_coordinate():
    assert convert_string_to_3d_coordinate("162,817,812") == (162, 817, 812)

def test_create_matrix_of_distances():
    input = [
        (162,817,812),
        (57,618,57),
        (906,360,560)
    ]

    expected_output = np.array([
        [0.0, 787.814064357828, 908.7843528582565],
        [787.814064357828, 0.0, 1019.9872548223335],
        [908.7843528582565, 1019.9872548223335, 0.0]
    ])

    np.testing.assert_array_almost_equal(create_matrix_of_distances(input), expected_output)

def test_get_pair_indexes_sorted_by_shortest_distance():
    distance_matrix = np.array([
        [0.0, 787.814064357828, 908.7843528582565],
        [787.814064357828, 0.0, 1019.9872548223335],
        [908.7843528582565, 1019.9872548223335, 0.0]
    ])
    
    expected_output = [(0, 1), (0, 2), (1, 2)]

    assert get_pair_indexes_sorted_by_shortest_distance(distance_matrix) == expected_output

def test_create_0_connections():
    input = [(0, 1), (0, 2), (1, 2)]

    assert create_connections(input, 0) == [[0], [1], [2]]

def test_create_sample_connections():
    input = """162,817,812
906,360,560
431,825,988
805,96,715
425,690,689"""

    coords = [convert_string_to_3d_coordinate(line) for line in input.splitlines()]
    distance_matrix = create_matrix_of_distances(coords)
    index_pairs = get_pair_indexes_sorted_by_shortest_distance(distance_matrix)
    connections = create_connections(index_pairs, 4)

    expected_output = [
        [0, 2, 4],
        [1, 3]
    ]

    assert connections == expected_output

def test_get_sizes_of_3_largest_connections():
    connections = [
        [0, 2, 4],
        [1, 3],
        [5, 6, 7, 8],
        [9]
    ]

    expected_output = [4, 3, 2]

    sizes = get_sizes_of_n_largest_connections(connections, 3)

    assert sizes == expected_output

def product_of_sizes_of_three_largest_junctions(input, n = 10):
    coords = [convert_string_to_3d_coordinate(line) for line in input.splitlines()]
    distance_matrix = create_matrix_of_distances(coords)
    index_pairs = get_pair_indexes_sorted_by_shortest_distance(distance_matrix)
    connections = create_connections(index_pairs, n)
    sizes = get_sizes_of_n_largest_connections(connections, 3)
    return sizes[0] * sizes[1] * sizes[2]

def eucleidian_distance(point_1, point_2):    
    p1 = np.array(point_1)
    p2 = np.array(point_2)

    return np.linalg.norm(p1 - p2)

def convert_string_to_3d_coordinate(point_str):
    return tuple(map(int, point_str.split(',')))

def create_matrix_of_distances(points):
    num_points = len(points)
    distance_matrix = np.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(num_points):
            if i != j:
                distance_matrix[i][j] = eucleidian_distance(points[i], points[j])
            else:
                distance_matrix[i][j] = 0.0

    return distance_matrix

def get_pair_indexes_sorted_by_shortest_distance(distance_matrix):
    num_points = distance_matrix.shape[0]
    pairs = []

    for i in range(num_points):
        for j in range(i + 1, num_points):
            pairs.append((i, j))

    pairs.sort(key=lambda pair: distance_matrix[pair[0], pair[1]])

    return pairs

def create_connections(index_pairs, num_connections):    
    connections = []
    unique_indexes = []
    for pair in index_pairs:
        if pair[0] not in unique_indexes:
            unique_indexes.append(pair[0])
        if pair[1] not in unique_indexes:   
            unique_indexes.append(pair[1])

    connections = [[index] for index in unique_indexes]

    connections_made = 0
    for pair in index_pairs:
        if connections_made >= num_connections:
            break

        first_index = pair[0]
        second_index = pair[1]

        existing_connection = None
        first_connection = None
        second_connection = None
        for connection in connections:
            if first_index in connection and second_index in connection:
                existing_connection = connection
            if first_index in connection:
                first_connection = connection
            if second_index in connection:
                second_connection = connection

        connection_to_update = first_connection if len(first_connection) >= len(second_connection) else second_connection
        connection_to_remove = second_connection if len(first_connection) >= len(second_connection) else first_connection
        index_to_add = first_index if first_index not in connection_to_update else second_index

        # print("Connections made so far:", connections_made)
        # print("Processing pair:", pair)
        # print("Current connections:", connections)
        # print("First connection:", first_connection)
        # print("Second connection:", second_connection)
        # print("Connection to update:", connection_to_update)
        # print("Connection to remove:", connection_to_remove)
        # print("Index to add:", index_to_add)

        if existing_connection is None:
            if connection_to_update is not None:
                connections.remove(connection_to_remove)
                connections.remove(connection_to_update)
                connection_to_update += connection_to_remove

                connections.append(connection_to_update)

            connections_made += 1
        else:
            if index_to_add not in existing_connection:
                connections.remove(existing_connection)
                existing_connection += connection_to_remove

                connections.remove(connection_to_update)
                connections.append(existing_connection)
            connections_made += 1

    # Sort each connection's indexes
    for connection in connections:
        connection.sort()

    return connections

def get_sizes_of_n_largest_connections(connections, n):
    sizes = sorted([len(connection) for connection in connections], reverse=True)[:n]
    return sizes

def test_input_part_one():
    with open(r"c:/Projects/playground/aoc2025/8/input.txt", encoding='utf-8') as f:
        input_str = f.read()
        result = product_of_sizes_of_three_largest_junctions(input_str, 1000)
        print("Final result:", result)
    assert True
    