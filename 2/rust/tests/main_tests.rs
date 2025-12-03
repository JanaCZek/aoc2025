use std::fs;

use aoc_day_2::{duplicate_numbers_in_range, generate_range, has_duplicate_digits};

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