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
                for y in y_start + 1..y_end {
                    let coord = (red_tile_coords[i].0, y);
                    if !red_tile_coords.contains(&coord) && !green_tile_coords.contains(&coord) {
                        green_tile_coords.push(coord);
                    }
                }
            } else if red_tile_coords[i].1 == red_tile_coords[j].1 {
                // Same y coordinate, connect x coordinates
                let x_start = std::cmp::min(red_tile_coords[i].0, red_tile_coords[j].0);
                let x_end = std::cmp::max(red_tile_coords[i].0, red_tile_coords[j].0);
                for x in x_start + 1..x_end {
                    let coord = (x, red_tile_coords[i].1);
                    if !red_tile_coords.contains(&coord) && !green_tile_coords.contains(&coord) {
                        green_tile_coords.push(coord);
                    }
                }
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
    println!("Creating matrix of limited areas...");

    for i in 0..coords.len() {
        let mut row: Vec<u64> = Vec::new();
        for j in 0..coords.len() {
            if !only_contains_green_or_red_tiles(coords[i], coords[j], coords, green_tile_coords) {
                row.push(0);
                continue;
            }
            let area = calculate_area(coords[i], coords[j]);
            if area > max_area {
                max_area = area;
                println!("New max area: {} between {:?} and {:?}", max_area, coords[i], coords[j]);
            }
            row.push(area);
        }
        matrix.push(row);
    }

    (matrix, max_area)
}