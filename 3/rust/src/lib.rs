pub fn find_largest_two_digit_number_in_bank(bank: &str) -> u8 {
    let digit_chars = bank.chars().collect::<Vec<char>>();

    let mut largest_number_pair = 0;
    let mut first_char_digit;

    for first_char_index in 0..digit_chars.len() {
        first_char_digit = digit_chars[first_char_index];
        for second_char_index in (first_char_index + 1)..digit_chars.len() {
            let second_char = digit_chars[second_char_index];
            let current_number_pair =
                (first_char_digit.to_digit(10).unwrap() * 10) + second_char.to_digit(10).unwrap();
            if current_number_pair > largest_number_pair {
                largest_number_pair = current_number_pair;
            }
        }
    }

    largest_number_pair as u8
}

pub fn generate_n_digit_combinations(digits: &[u8], n: u8) -> Vec<u64> {
    let mut combinations: Vec<u64> = Vec::new();

    fn backtrack(
        digits: &[u8],
        n: u8,
        start: usize,
        current_combination: &mut Vec<u8>,
        combinations: &mut Vec<u64>,
    ) {
        if current_combination.len() == n as usize {
            let number = current_combination
                .iter()
                .fold(0u64, |acc, &d| acc * 10 + d as u64);
            combinations.push(number);
            return;
        }

        for i in start..digits.len() {
            current_combination.push(digits[i]);
            backtrack(digits, n, i + 1, current_combination, combinations);
            current_combination.pop();
        }
    }

    backtrack(
        digits,
        n,
        0,
        &mut Vec::with_capacity(n as usize),
        &mut combinations,
    );

    combinations
}

pub fn find_largest_n_digit_number_in_bank(bank: &str, n: u8) -> u64 {
    let digit_chars = bank.chars().collect::<Vec<char>>();
    let digits: Vec<u8> = digit_chars
        .iter()
        .map(|&c| c.to_digit(10).unwrap() as u8)
        .collect();

    let combinations = generate_n_digit_combinations(&digits, n);
    *combinations.iter().max().unwrap()
}

// 1 2 3 4 5 6
// 1 2 3
// 1 2 4
// 1 2 5
// 1 2 6
// 1 3 4
// 1 3 5
// 1 3 6
// 1 4 5
// 1 4 6
// 1 5 6
// 2 3 4
// 2 3 5
// 2 3 6
// 2 4 5
// 2 4 6
// 2 5 6
// 3 4 5
// 3 4 6
// 3 5 6
// 4 5 6