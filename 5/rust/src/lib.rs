pub fn fresh_ids(range_start: &str, range_end: &str, ids: &[&str]) -> Vec<String> {
    let range_start_num: u64 = range_start.parse().unwrap_or(0);
    let range_end_num: u64 = range_end.parse().unwrap_or(0);

    let mut fresh_ids = Vec::new();

    for id in ids {
        let id_num: u64 = id.parse().unwrap_or(0);
        if id_num >= range_start_num && id_num <= range_end_num {
            fresh_ids.push(id.to_string());
        }
    }

    fresh_ids
}

pub fn merge_ranges(ranges: Vec<&str>) -> Vec<String> {
    // Parse ranges into (start, end) tuples
    let mut range_data = ranges
        .iter()
        .map(|range| {
            let parts: Vec<&str> = range.split('-').collect();
            let start = parts[0].parse::<u64>().unwrap_or(0);
            let end = parts[1].parse::<u64>().unwrap_or(0);
            (start, end)
        })
        .collect::<Vec<(u64, u64)>>();

    // Sort by start
    range_data.sort_by(|a, b| a.0.cmp(&b.0));

    let mut merged_ranges = Vec::new();
    if range_data.is_empty() {
        return merged_ranges;
    }

    let mut current_start = range_data[0].0;
    let mut current_end = range_data[0].1;

    for &(start, end) in &range_data[1..] {
        if start <= current_end {
            current_end = current_end.max(end);
        } else {
            merged_ranges.push(format!("{current_start}-{current_end}"));
            current_start = start;
            current_end = end;
        }
    }
    merged_ranges.push(format!("{current_start}-{current_end}"));
    merged_ranges
}