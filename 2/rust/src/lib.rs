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

pub fn chunks_up_to_half_point(input: &str) -> Vec<&str> {
    let half_len = input.len() / 2;
    let mut chunks = Vec::new();
    for i in 1..=half_len {
        chunks.push(&input[..i]);
    }
    chunks
}

pub fn split_input_by_chunk_size(input: &str, chunk_size: usize) -> Vec<&str> {
    input
        .as_bytes()
        .chunks(chunk_size)
        .map(|chunk| std::str::from_utf8(chunk).unwrap())
        .collect()
}

pub fn multiple_duplicate_numbers_in_range(start: &str, end: &str) -> Vec<u64> {
    let range = generate_range(start, end);
    let mut duplicates = Vec::new();
    
    for num_str in range {
        let pattern_chunks = chunks_up_to_half_point(&num_str);
        for pattern in pattern_chunks {
            let chunk_size = pattern.len();
            let split_chunks = split_input_by_chunk_size(&num_str, chunk_size);
            let all_match = split_chunks.iter().all(|&chunk| chunk == pattern);
            if all_match {
                duplicates.push(num_str.parse::<u64>().unwrap());
            }
        }
    }

    duplicates.dedup();
    duplicates
}