use std::{collections::HashSet, fs};

use aoc_day_5::{fresh_ids, merge_ranges};

// Run tests with output
// cargo test -- --nocapture

#[test]
fn detects_fresh_ids() {
    let input = vec![("1", "10", vec!["1", "5", "10", "15"], vec!["1", "5", "10"])];

    for (range_start, range_end, ids, expected) in input {
        let result = fresh_ids(range_start, range_end, &ids);
        assert_eq!(result, expected);
    }
}

#[test]
fn detects_fresh_ids_small_input() {
    let ranges = vec!["3-5", "10-14", "16-20", "12-18"];
    let ids = vec!["1", "5", "8", "11", "17", "32"];

    let mut fresh_ids_collected = HashSet::new();

    for range in ranges {
        let parts: Vec<&str> = range.split('-').collect();
        let range_start = parts[0];
        let range_end = parts[1];

        let fresh_ids_in_range = fresh_ids(range_start, range_end, &ids);
        fresh_ids_collected.extend(fresh_ids_in_range);
    }

    assert_eq!(fresh_ids_collected.len(), 3);
}

#[test]
fn merging_ranges() {
    let inputs = vec![
        (vec!["1-5", "6-10"], vec!["1-5", "6-10"]),
        (vec!["1-3", "2-5", "6-8"], vec!["1-5", "6-8"]),
        (vec!["10-15", "12-20", "18-25"], vec!["10-25"]),
    ];

    for (ranges, expected) in inputs {
        let result = merge_ranges(ranges);
        assert_eq!(result, expected);
    }
}

#[test]
fn input_test_part_one() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\5\\input.txt").unwrap();

    let mut ranges = Vec::new();
    let mut ids = Vec::new();
    for line in contents.lines() {
        if line.contains('-')
        {
            ranges.push(line);
        } 
        else if !line.is_empty()
        {
            ids.push(line);
        }
    }

    let mut fresh_ids_collected = HashSet::new();

    for range in ranges {
        let parts: Vec<&str> = range.split('-').collect();
        let range_start = parts[0];
        let range_end = parts[1];

        let fresh_ids_in_range = fresh_ids(range_start, range_end, &ids);
        fresh_ids_collected.extend(fresh_ids_in_range);
    }

    println!("Fresh IDs collected: {:?}", fresh_ids_collected.len());

    assert_eq!(true, true);
}

#[test]
fn input_test_part_two() {
    let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\5\\input.txt").unwrap();

    let mut ranges = Vec::new();
    for line in contents.lines() {
        if line.contains('-')
        {
            ranges.push(line);
        }
    }

    let merged_ranges = merge_ranges(ranges);

    let mut total_count = 0;
    for range in merged_ranges {
        let parts: Vec<&str> = range.split('-').collect();
        let range_start: u64 = parts[0].parse().unwrap_or(0);
        let range_end: u64 = parts[1].parse().unwrap_or(0);
        total_count += range_end - range_start + 1;
    }

    println!("Total count of IDs in merged ranges: {total_count}");

    assert_eq!(true, true);
}
