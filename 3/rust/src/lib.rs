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
