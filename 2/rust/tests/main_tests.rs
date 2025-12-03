use std::fs;

use aoc_day_2::{chunks_up_to_half_point, duplicate_numbers_in_range, generate_range, has_duplicate_digits, multiple_duplicate_numbers_in_range, split_input_by_chunk_size};

#[test]
fn generates_range() {
    let inputs: Vec<(&str, &str, Vec<&str>)> = vec![
        ("5", "10", vec!["5", "6", "7", "8", "9", "10"]),
        ("0", "3", vec!["0", "1", "2", "3"]),
        ("8", "8", vec!["8"]),
    ];

    for (start, end, expected) in inputs {
        let result = generate_range(start, end);
        let expected_u64= expected.to_vec();
        assert_eq!(result, expected_u64);
    }
}

#[test]
fn detects_duplicate_digits() {
    let inputs: Vec<(&str, bool)> = vec![
        ("11", true),
        ("12", false),
        ("1111", true),
        ("1112", false),
        ("1212", true),
        ("111111", true),
        ];

    for (input, expected) in inputs {
        let result = has_duplicate_digits(input);
        assert_eq!(result, expected, "Failed on input: {input}");
    }
}

#[test]
fn finds_duplicate_numbers_in_range() {
    let inputs: Vec<(&str, &str, Vec<u64>)> = vec![
        ("11", "22", vec![11, 22]),
        ("95", "115", vec![99]),
        ("998", "1012", vec![1010]),
        ("1188511880", "1188511890", vec![1188511885]),
        ("222220", "222224", vec![222222]),
        ("1698522", "1698528", vec![]),
        ("446443", "446449", vec![446446]),
        ("38593856", "38593862", vec![38593859]),
    ];

    for (start, end, expected) in inputs {
        let result = duplicate_numbers_in_range(start, end);
        assert_eq!(result, expected, "Failed on range: {start}-{end}");
    }
}

#[test]
fn chunks_input_up_to_half_point() {
    let inputs : Vec<(&str, Vec<&str>)> = vec![
        ("123456", vec!["1", "12", "123"]),
        ("11", vec!["1"]),
    ];

    for (input, expected) in inputs {
        let result = chunks_up_to_half_point(input);
        assert_eq!(result, expected, "Failed on input: {input}");
    }
}

#[test]
fn splits_input_by_chunk_size() {
    let inputs: Vec<(&str, usize, Vec<&str>)> = vec![
        ("111", 1, vec!["1", "1", "1"]),
        ("123456", 2, vec!["12", "34", "56"]),
    ];

    for (input, chunk_size, expected) in inputs {
        let result = split_input_by_chunk_size(input, chunk_size);
        assert_eq!(result, expected, "Failed on input: {input} with chunk size: {chunk_size}");
    }
}

#[test]
fn finds_multiple_duplicate_numbers_in_range() {
    let inputs: Vec<(&str, &str, Vec<u64>)> = vec![
        ("11", "22", vec![11, 22]),
        ("95", "115", vec![99, 111]),
        ("998", "1012", vec![999, 1010]),
        ("1188511880", "1188511890", vec![1188511885]),
        ("222220", "222224", vec![222222]),
        ("1698522", "1698528", vec![]),
        ("446443", "446449", vec![446446]),
        ("38593856", "38593862", vec![38593859]),
        ("565653", "565659", vec![565656]),
        ("824824821", "824824827", vec![824824824]),
        ("2121212118", "2121212124", vec![2121212121]),
    ];

    for (start, end, expected) in inputs {
        let result = multiple_duplicate_numbers_in_range(start, end);
        assert_eq!(result, expected, "Failed on range: {start}-{end}");
    }
}

#[test]
fn input_test_part_one() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\2\\input.txt").unwrap();
    let ranges = contents.split(',');
    let mut sum = 0;
    for line in ranges {
        let parts: Vec<&str> = line.trim().split('-').collect();
        let start = parts[0];
        let end = parts[1];

        let duplicates = duplicate_numbers_in_range(start, end);
        sum += duplicates.iter().sum::<u64>();
    }
    println!("Total sum of duplicate numbers in ranges: {sum}");

    assert_eq!(true, true);
}

#[test]
fn input_test_part_two() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\2\\input.txt").unwrap();
    let ranges = contents.split(',');
    let mut sum = 0;
    for line in ranges {
        let parts: Vec<&str> = line.trim().split('-').collect();
        let start = parts[0];
        let end = parts[1];

        let duplicates = multiple_duplicate_numbers_in_range(start, end);
        sum += duplicates.iter().sum::<u64>();
    }
    println!("Total sum of duplicate numbers in ranges: {sum}");

    assert_eq!(true, true);
}
