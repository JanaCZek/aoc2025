pub fn parse_strings_to_coordinates(input: &str) -> Vec<(u64, u64)> {
    
    input
        .lines()
        .map(|line| {
            let mut parts = line.split(',');
            let x = parts
                .next()
                .and_then(|s| s.trim().parse::<u64>().ok())
                .unwrap_or(0);
            let y = parts
                .next()
                .and_then(|s| s.trim().parse::<u64>().ok())
                .unwrap_or(0);
            (x, y)
        })
        .collect()
}

pub fn calculate_area(coords_one: (u64, u64), coords_two: (u64, u64)) -> u64 {
    let width = coords_one.0.abs_diff(coords_two.0);
    let height = coords_one.1.abs_diff(coords_two.1);

    (width + 1) * (height + 1)
}

pub fn create_matrix_of_areas(coords: &[(u64, u64)]) -> (Vec<Vec<u64>>, u64) {
    let mut matrix: Vec<Vec<u64>> = Vec::new();
    let mut max_area = 0;

    for i in 0..coords.len() {
        let mut row: Vec<u64> = Vec::new();
        for j in 0..coords.len() {
            let area = calculate_area(coords[i], coords[j]);
            if area > max_area {
                max_area = area;
            }
            row.push(area);
        }
        matrix.push(row);
    }

    (matrix, max_area)
}

pub fn create_green_tiles(red_tile_coords: &[(u64, u64)]) -> Vec<(u64, u64)> {
    let mut green_tile_coords: Vec<(u64, u64)> = Vec::new();
    for i in 0..red_tile_coords.len() {
        for j in 0..red_tile_coords.len() {
            if red_tile_coords[i].0 == red_tile_coords[j].0 {
                // Same x coordinate, connect y coordinates
                let y_start = std::cmp::min(red_tile_coords[i].1, red_tile_coords[j].1);
                let y_end = std::cmp::max(red_tile_coords[i].1, red_tile_coords[j].1);
                green_tile_coords.extend((y_start + 1..y_end).map(|y| (red_tile_coords[i].0, y)));
            } else if red_tile_coords[i].1 == red_tile_coords[j].1 {
                // Same y coordinate, connect x coordinates
                let x_start = std::cmp::min(red_tile_coords[i].0, red_tile_coords[j].0);
                let x_end = std::cmp::max(red_tile_coords[i].0, red_tile_coords[j].0);
                green_tile_coords.extend((x_start + 1..x_end).map(|x| (x, red_tile_coords[i].1)));
            }            
        }
    }
    green_tile_coords
}

pub fn only_contains_green_or_red_tiles(coords_one: (u64, u64), coords_two: (u64, u64), red_tile_coords: &[(u64, u64)], green_tile_coords: &[(u64, u64)]) -> bool {
    let x_start = std::cmp::min(coords_one.0, coords_two.0);
    let x_end = std::cmp::max(coords_one.0, coords_two.0);
    let y_start = std::cmp::min(coords_one.1, coords_two.1);
    let y_end = std::cmp::max(coords_one.1, coords_two.1);

    // println!("Checking area from ({},{}) to ({},{})", x_start, y_start, x_end, y_end);
    // println!("Red tiles: {:?}", red_tile_coords);
    // println!("Green tiles: {:?}", green_tile_coords);

    for x in x_start..=x_end {
        for y in y_start..=y_end {
            let coord = (x, y);
            if !red_tile_coords.contains(&coord) && !green_tile_coords.contains(&coord) {
                return false;
            }
        }
    }
    true
}

pub fn create_matrix_of_limited_areas(coords: &[(u64, u64)], green_tile_coords: &[(u64, u64)]) -> (Vec<Vec<u64>>, u64) {
    let mut matrix: Vec<Vec<u64>> = Vec::new();
    let mut max_area = 0;

    let disallowed_coords = create_disallowed_coordinates(coords, green_tile_coords);

    for i in 0..coords.len() {
        let mut row: Vec<u64> = Vec::new();
        for j in 0..coords.len() {
            let all_coords = get_all_coords_of_rectangle(coords[i], coords[j]);
            // If any of the coords in the rectangle are disallowed, area is 0
            let mut contains_disallowed = false;
            for coord in &all_coords {
                if disallowed_coords.contains(coord) {
                    contains_disallowed = true;
                    break;
                }
            }
            let area = if contains_disallowed { 0 } else { calculate_area(coords[i], coords[j]) };
            if area > max_area {
                max_area = area;
            }
            row.push(area);
        }
        matrix.push(row);
    }

    (matrix, max_area)
}

pub fn create_disallowed_coordinates(red_tile_coords: &[(u64, u64)], green_tile_coords: &[(u64, u64)]) -> Vec<(u64, u64)> {
    let mut disallowed_coords: Vec<(u64, u64)> = Vec::new();
    let coords_sorted_by_y = {
        let mut v = red_tile_coords.to_vec();
        v.extend_from_slice(green_tile_coords);
        v.sort_by_key(|k| k.1);
        v
    };

    let max_global_x = coords_sorted_by_y.iter().map(|coord| coord.0).max().unwrap_or(0);
    let min_global_x = coords_sorted_by_y.iter().map(|coord| coord.0).min().unwrap_or(0);

    let mut current_y = None;
    let mut x_coords_at_current_y: Vec<u64> = Vec::new();
    for coord in coords_sorted_by_y {
        if Some(coord.1) != current_y {
            if let Some(y) = current_y {
                if !x_coords_at_current_y.is_empty() {
                    let min_x = *x_coords_at_current_y.iter().min().unwrap();
                    let max_x = *x_coords_at_current_y.iter().max().unwrap();
                    disallowed_coords.extend((min_global_x..min_x).map(|x| (x, y)));
                    disallowed_coords.extend(((max_x + 1)..=max_global_x).map(|x| (x, y)));
                }
            }
            current_y = Some(coord.1);
            x_coords_at_current_y.clear();
        }
        x_coords_at_current_y.push(coord.0);
    }

    disallowed_coords
}

pub fn create_disallowed_ranges(red_tile_coords: &[(u64, u64)], green_tile_coords: &[(u64, u64)]) -> Vec<((u64, u64), (u64, u64))> {
    let mut disallowed_ranges: Vec<((u64, u64), (u64, u64))> = Vec::new();
    let coords_sorted_by_y = {
        let mut v = red_tile_coords.to_vec();
        v.extend_from_slice(green_tile_coords);
        v.sort_by_key(|k| k.1);
        v
    };

    let max_global_x = coords_sorted_by_y.iter().map(|coord| coord.0).max().unwrap_or(0);
    let min_global_x = coords_sorted_by_y.iter().map(|coord| coord.0).min().unwrap_or(0);

    let mut current_y = None;
    let mut x_coords_at_current_y: Vec<u64> = Vec::new();
    for coord in coords_sorted_by_y {
        if Some(coord.1) != current_y {
            if let Some(y) = current_y {
                if !x_coords_at_current_y.is_empty() {
                    let min_x = *x_coords_at_current_y.iter().min().unwrap();
                    let max_x = *x_coords_at_current_y.iter().max().unwrap();
                    if min_x > min_global_x {
                        disallowed_ranges.push(((min_global_x, y), (min_x - 1, y)));
                    }
                    if max_x < max_global_x {
                        disallowed_ranges.push(((max_x + 1, y), (max_global_x, y)));
                    }
                }
            }
            current_y = Some(coord.1);
            x_coords_at_current_y.clear();
        }
        x_coords_at_current_y.push(coord.0);
    }

    // Sort each range so that the smaller x comes first
    for range in &mut disallowed_ranges {
        if range.0 .0 > range.1 .0 {
            std::mem::swap(&mut range.0, &mut range.1);
        }
    }

    disallowed_ranges
}

pub fn get_all_coords_of_rectangle(coords_one: (u64, u64), coords_two: (u64, u64)) -> Vec<(u64, u64)> {
    let x_start = std::cmp::min(coords_one.0, coords_two.0);
    let x_end = std::cmp::max(coords_one.0, coords_two.0);
    let y_start = std::cmp::min(coords_one.1, coords_two.1);
    let y_end = std::cmp::max(coords_one.1, coords_two.1);

    (x_start..=x_end)
        .flat_map(|x| (y_start..=y_end).map(move |y| (x, y)))
        .collect()
}

pub fn is_any_coord_disallowed(coords: &[(u64, u64)], disallowed_coord_ranges: &[((u64, u64), (u64, u64))]) -> bool {
    coords.iter().any(|coord| {
        disallowed_coord_ranges.iter().any(|range| {
            coord.1 == range.0 .1 && coord.0 >= range.0 .0 && coord.0 <= range.1 .0
        })
    })
}