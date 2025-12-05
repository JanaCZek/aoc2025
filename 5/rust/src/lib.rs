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