use std::fs;

use aoc_day_3::find_largest_two_digit_number_in_bank;


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
fn input_test_part_one() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\3\\input.txt").unwrap();

    let sum: u32 = contents.lines().map(|line| find_largest_two_digit_number_in_bank(line) as u32).sum();

    println!("Sum of largest two digit numbers: {sum}");

    assert_eq!(true, true);
}

#[test]
fn input_test_part_two() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\3\\input.txt").unwrap();

    assert_eq!(true, true);
}
