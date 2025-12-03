use std::fs;

use aoc_day_3::{find_largest_n_digit_number_in_bank, find_largest_two_digit_number_in_bank, generate_n_digit_combinations};

// Run tests with output
// cargo test -- --nocapture

#[test]
fn finds_two_largest_digits_in_bank() {
    let inputs: Vec<(Vec<&str>, u8)> = vec![
        (vec!["987654321111111"], 98),
        (vec!["811111111111119"], 89),
        (vec!["234234234234278"], 78),
        (vec!["818181911112111"], 92),
    ];

    for (banks, expected_largest) in inputs {
        for bank in banks {
                let largest_two_digit_number = find_largest_two_digit_number_in_bank(bank);
                assert_eq!(largest_two_digit_number, expected_largest, "Failed for bank: {bank}");
        }
    }
    
    assert_eq!(true, true);
}

#[test]
fn generates_n_digit_combinations() {
    let inputs: Vec<(&[u8], u8, Vec<u64>)> = vec![
        (&[1, 2, 3, 4, 5, 6], 3, vec![
            123, 124, 125, 126,
            134, 135, 136,
            145, 146,
            156,
            234, 235, 236,
            245, 246,
            256,
            345, 346,
            356,
            456
        ]),
    ];

    for (digits, n, expected_combinations) in inputs {
        let generated_combinations = generate_n_digit_combinations(digits, n);
        assert_eq!(generated_combinations, expected_combinations, "Failed for digits: {digits:?}, n: {n}");
    }
    
    assert_eq!(true, true);
}

#[test]
fn finds_largest_n_digit_number_in_bank() {
    let inputs: Vec<(&str, u8, u64)> = vec![
        ("987654321111111", 3, 987),
        ("811111111111119", 3, 819),
        ("234234234234278", 3, 478),
        ("818181911112111", 3, 921),
        ("987654321111111", 12, 987654321111),
        ("811111111111119", 12, 811111111119),
        ("234234234234278", 12, 434234234278),
        ("818181911112111", 12, 888911112111),        
    ];

    for (bank, n, expected_largest) in inputs {
        let largest_n_digit_number = aoc_day_3::find_largest_n_digit_number_in_bank(bank, n);
        assert_eq!(largest_n_digit_number, expected_largest, "Failed for bank: {bank}, n: {n}");
    }
    
    assert_eq!(true, true);
}

#[test]
fn input_test_part_one() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\3\\input.txt").unwrap();

    let sum: u32 = contents.lines().map(|line| find_largest_two_digit_number_in_bank(line) as u32).sum();

    println!("Sum of largest two digit numbers: {sum}");

    assert_eq!(true, true);
}

#[test]
fn input_test_part_two() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\3\\input.txt").unwrap();

    let mut sum: u64 = 0;

    for line in contents.lines() {
        let largest = find_largest_n_digit_number_in_bank(line, 12);
        sum += largest;
    }

    println!("Sum of largest twelve digit numbers: {sum}");

    assert_eq!(true, true);
}
