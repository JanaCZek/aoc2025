pub fn generate_range(start: &str, end: &str) -> Vec<String> {
    let start_num: u64 = start.parse().unwrap();
    let end_num: u64 = end.parse().unwrap();

    (start_num..=end_num).map(|num| num.to_string()).collect()
}

pub fn has_duplicate_digits(input: &str) -> bool {
    let first_half = &input[..input.len() / 2];
    let second_half = &input[input.len() / 2..];

    first_half == second_half
}

pub fn duplicate_numbers_in_range(start: &str, end: &str) -> Vec<u64> {
    let range = generate_range(start, end);
    range
        .into_iter()
        .filter(|num_str| has_duplicate_digits(num_str))
        .map(|num_str| num_str.parse::<u64>().unwrap())
        .collect()
}