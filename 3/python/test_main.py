def test_input_part_one():
    with open("C:\\Projects\\playground\\aoc2025\\3\\input.txt", "r") as file:
        data = file.read()
        trimmed_data = data.strip()
        
        sum = 0
        for line in trimmed_data.split("\n"):
            largest = find_largest_n_digit_number_in_bank(line, 2)
            sum += largest

        print(f"Sum of largest two digit numbers: {sum}")
    assert True == True

def test_input_part_two():
    with open("C:\\Projects\\playground\\aoc2025\\3\\input.txt", "r") as file:
        data = file.read()
        trimmed_data = data.strip()
        
        sum = 0
        for line in trimmed_data.split("\n"):
            largest = find_largest_n_digit_number_in_bank(line, 12)
            sum += largest

        print(f"Sum of largest twelve digit numbers: {sum}")
    assert True == True

def test_find_largest_two_digit_number_in_bank():
    expected = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ]

    for bank, expected_result in expected:
        assert find_largest_n_digit_number_in_bank(bank, 2) == expected_result

def find_largest_n_digit_number_in_bank(bank, n):
    characters = []
    for i in range(len(bank)):
        characters.append((i, int(bank[i])))

    min_index = 0
    max_index = len(characters) - n
    digit_index = 0
    largest_number = 0
    output = []
    found_digits = 0

    while found_digits < n:
        for character_index in range(0, len(characters)):
            index, value = characters[character_index]
            if index >= min_index and index <= max_index and value > largest_number:
                largest_number = value
                digit_index = index
        output.append(largest_number)
        found_digits += 1
        min_index = digit_index + 1
        max_index += 1
        largest_number = 0
        
    return int("".join(map(str, output)))
