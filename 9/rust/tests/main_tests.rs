use std::{collections::HashSet, fs};

// Run tests with output
// cargo test -- --nocapture

#[test]
fn test_parses_string_to_coordinates() {
    let input = "7,1\n3,4\n5,6";
    let expected = vec![(7, 1), (3, 4), (5, 6)];

    let result = aoc_day_9::parse_strings_to_coordinates(input);

    assert_eq!(result, expected);
}

#[test]
fn test_calculates_area_of_two_coordinates() {
    let coords = vec![(2, 5), (11, 1)];
    let expected_area = 50;

    let result = aoc_day_9::calculate_area(coords[0], coords[1]);

    assert_eq!(result, expected_area);
}

#[test]
fn test_creates_matrix_of_areas() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";
    let expected_max_area = 50;

    let coords = aoc_day_9::parse_strings_to_coordinates(input);
    let (result_matrix, result_max_area) = aoc_day_9::create_matrix_of_areas(&coords);

    assert_eq!(result_max_area, expected_max_area);
}

#[test]
fn input_test_part_one() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\9\\input.txt").unwrap();

    let mut coords = aoc_day_9::parse_strings_to_coordinates(&contents);
    let (matrix, max_area) = aoc_day_9::create_matrix_of_areas(&coords);

    println!("Max area: {}", max_area);
    assert_eq!(true, true);
}