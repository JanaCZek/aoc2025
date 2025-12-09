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

pub fn create_green_tiles_between_adjacent_red_tiles(
    red_tile_coords: &[(u64, u64)],
) -> Vec<(u64, u64)> {
    let mut green_tile_coords: Vec<(u64, u64)> = Vec::new();

    for i in 0..(red_tile_coords.len() - 1) {
        create_green_connections(red_tile_coords, &mut green_tile_coords, i, i + 1);
    }

    // connect last pair to first pair
    create_green_connections(
        red_tile_coords,
        &mut green_tile_coords,
        red_tile_coords.len() - 1,
        0,
    );

    green_tile_coords
}

fn create_green_connections(
    red_tile_coords: &[(u64, u64)],
    green_tile_coords: &mut Vec<(u64, u64)>,
    first_index: usize,
    second_index: usize,
) {
    let coord_one = red_tile_coords[first_index];
    let coord_two = red_tile_coords[second_index];
    if coord_one.0 == coord_two.0 {
        let y_start = std::cmp::min(coord_one.1, coord_two.1);
        let y_end = std::cmp::max(coord_one.1, coord_two.1);
        green_tile_coords.extend((y_start + 1..y_end).map(|y| (coord_one.0, y)));
    } else if coord_one.1 == coord_two.1 {
        let x_start = std::cmp::min(coord_one.0, coord_two.0);
        let x_end = std::cmp::max(coord_one.0, coord_two.0);
        green_tile_coords.extend((x_start + 1..x_end).map(|x| (x, coord_one.1)));
    }
}

pub fn only_contains_green_or_red_tiles(
    coords_one: (u64, u64),
    coords_two: (u64, u64),
    red_tile_coords: &[(u64, u64)],
    green_tile_coords: &[(u64, u64)],
) -> bool {
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

pub fn create_matrix_of_limited_areas(
    coords: &[(u64, u64)],
    green_tile_coords: &[(u64, u64)],
) -> (Vec<Vec<u64>>, u64) {
    let mut matrix: Vec<Vec<u64>> = Vec::new();
    let mut max_area = 0;

    let disallowed_coord_ranges = create_disallowed_ranges(coords, green_tile_coords);

    for i in 0..coords.len() {
        let mut row: Vec<u64> = Vec::new();
        for j in 0..coords.len() {
            let corner_coords = get_all_corner_coords_of_rectangle(coords[i], coords[j]);
            let mut contains_disallowed = false;
            if is_rectangle_disallowed(&corner_coords, &disallowed_coord_ranges) {
                contains_disallowed = true;
            }
            let area = if contains_disallowed {
                0
            } else {
                calculate_area(coords[i], coords[j])
            };
            if area > max_area {
                max_area = area;
            }
            row.push(area);
            println!("Completed cell {} out of {}", j + 1, coords.len());
        }
        matrix.push(row);
        println!("Completed row {}/{}", i + 1, coords.len());
    }

    (matrix, max_area)
}

pub fn create_disallowed_ranges(
    red_tile_coords: &[(u64, u64)],
    green_tile_coords: &[(u64, u64)],
) -> Vec<((u64, u64), (u64, u64))> {
    let mut disallowed_ranges: Vec<((u64, u64), (u64, u64))> = Vec::new();
    let coords_sorted_by_y = {
        let mut v = red_tile_coords.to_vec();
        v.extend_from_slice(green_tile_coords);
        v.sort_by_key(|k| k.1);
        v
    };

    let max_global_x = coords_sorted_by_y
        .iter()
        .map(|coord| coord.0)
        .max()
        .unwrap_or(0);
    let min_global_x = coords_sorted_by_y
        .iter()
        .map(|coord| coord.0)
        .min()
        .unwrap_or(0);

    // Collect all y values present in the input
    let mut y_to_xs: std::collections::HashMap<u64, Vec<u64>> = std::collections::HashMap::new();
    for &(x, y) in red_tile_coords.iter().chain(green_tile_coords.iter()) {
        y_to_xs.entry(y).or_default().push(x);
    }

    let min_global_y = y_to_xs.keys().min().cloned().unwrap_or(0);
    let max_global_y = y_to_xs.keys().max().cloned().unwrap_or(0);

    for y in min_global_y..=max_global_y {
        if let Some(xs) = y_to_xs.get(&y) {
            if !xs.is_empty() {
                let min_x = *xs.iter().min().unwrap();
                let max_x = *xs.iter().max().unwrap();
                if min_x > min_global_x {
                    disallowed_ranges.push(((min_global_x, y), (min_x - 1, y)));
                }
                if max_x < max_global_x {
                    disallowed_ranges.push(((max_x + 1, y), (max_global_x, y)));
                }
            }
        } else {
            // No tiles at this y, so the whole x range is disallowed
            disallowed_ranges.push(((min_global_x, y), (max_global_x, y)));
        }
    }

    // Sort each range so that the smaller x comes first
    for range in &mut disallowed_ranges {
        if range.0.0 > range.1.0 {
            std::mem::swap(&mut range.0, &mut range.1);
        }
    }

    disallowed_ranges
}

pub fn get_all_coords_of_rectangle(
    coords_one: (u64, u64),
    coords_two: (u64, u64),
) -> Vec<(u64, u64)> {
    let x_start = std::cmp::min(coords_one.0, coords_two.0);
    let x_end = std::cmp::max(coords_one.0, coords_two.0);
    let y_start = std::cmp::min(coords_one.1, coords_two.1);
    let y_end = std::cmp::max(coords_one.1, coords_two.1);

    (x_start..=x_end)
        .flat_map(|x| (y_start..=y_end).map(move |y| (x, y)))
        .collect()
}

pub fn get_all_perimeter_coords_of_rectangle(
    coords_one: (u64, u64),
    coords_two: (u64, u64),
) -> Vec<(u64, u64)> {
    let x_start = std::cmp::min(coords_one.0, coords_two.0);
    let x_end = std::cmp::max(coords_one.0, coords_two.0);
    let y_start = std::cmp::min(coords_one.1, coords_two.1);
    let y_end = std::cmp::max(coords_one.1, coords_two.1);

    let mut perimeter_coords: Vec<(u64, u64)> = Vec::new();

    for x in x_start..=x_end {
        perimeter_coords.push((x, y_start));
        perimeter_coords.push((x, y_end));
    }
    for y in (y_start + 1)..(y_end) {
        perimeter_coords.push((x_start, y));
        perimeter_coords.push((x_end, y));
    }

    perimeter_coords
}

pub fn is_any_coord_disallowed(
    coords: &[(u64, u64)],
    disallowed_coord_ranges: &[((u64, u64), (u64, u64))],
) -> bool {
    coords.iter().any(|coord| {
        disallowed_coord_ranges
            .iter()
            .any(|range| coord.1 == range.0.1 && coord.0 >= range.0.0 && coord.0 <= range.1.0)
    })
}

#[derive(Debug, PartialEq, Eq)]
pub struct RectangleCornerCoordinates {
    pub top_left: (u64, u64),
    pub top_right: (u64, u64),
    pub bottom_left: (u64, u64),
    pub bottom_right: (u64, u64),
}
pub fn get_all_corner_coords_of_rectangle(
    coords_one: (u64, u64),
    coords_two: (u64, u64),
) -> RectangleCornerCoordinates {
    let x_start = std::cmp::min(coords_one.0, coords_two.0);
    let x_end = std::cmp::max(coords_one.0, coords_two.0);
    let y_start = std::cmp::min(coords_one.1, coords_two.1);
    let y_end = std::cmp::max(coords_one.1, coords_two.1);

    RectangleCornerCoordinates {
        top_left: (x_start, y_start),
        top_right: (x_end, y_start),
        bottom_left: (x_start, y_end),
        bottom_right: (x_end, y_end),
    }
}

#[derive(Debug, PartialEq, Eq)]
pub struct HorizontalRange {
    pub start: (u64, u64),
    pub end: (u64, u64),
}

#[derive(Debug, PartialEq, Eq)]
pub struct VerticalRange {
    pub start: (u64, u64),
    pub end: (u64, u64),
}

pub fn get_ranges_from_rectangle(
    rect: &RectangleCornerCoordinates,
) -> (
    HorizontalRange,
    HorizontalRange,
    VerticalRange,
    VerticalRange,
) {
    let top_horizontal = HorizontalRange {
        start: (rect.top_left.0, rect.top_left.1),
        end: (rect.top_right.0, rect.top_right.1),
    };
    let bottom_horizontal = HorizontalRange {
        start: (rect.bottom_left.0, rect.bottom_left.1),
        end: (rect.bottom_right.0, rect.bottom_right.1),
    };
    let left_vertical = VerticalRange {
        start: (rect.top_left.0, rect.top_left.1),
        end: (rect.bottom_left.0, rect.bottom_left.1),
    };
    let right_vertical = VerticalRange {
        start: (rect.top_right.0, rect.top_right.1),
        end: (rect.bottom_right.0, rect.bottom_right.1),
    };

    (
        top_horizontal,
        bottom_horizontal,
        left_vertical,
        right_vertical,
    )
}

pub fn is_horizontal_range_disallowed(
    range: &HorizontalRange,
    disallowed_ranges: &Vec<((u64, u64), (u64, u64))>,
) -> bool {
    let ranges_on_line = disallowed_ranges
        .iter()
        .filter(|r| r.0.1 == range.start.1)
        .collect::<Vec<&((u64, u64), (u64, u64))>>();

    for disallowed_range in ranges_on_line {
        if (range.start.0 >= disallowed_range.0.0 && range.start.0 <= disallowed_range.1.0)
            || (range.end.0 >= disallowed_range.0.0 && range.end.0 <= disallowed_range.1.0)
        {
            return true;
        }
    }
    false
}

pub fn is_vertical_range_disallowed(
    range: &VerticalRange,
    disallowed_ranges: &Vec<((u64, u64), (u64, u64))>,
) -> bool {
    // println!("Disallowed: {disallowed_ranges:?}");

    let ranges = [range.start.1..=range.end.1]
        .iter()
        .flat_map(|line| {
            disallowed_ranges
                .iter()
                .filter(|r| r.0.1 >= *line.start() && r.0.1 <= *line.end())
        })
        .collect::<Vec<_>>();

    // println!("Vertical range: {:?}, Disallowed ranges on line: {:?}", range, ranges);

    let y_coord = range.start.0;

    let filtered_ranges = ranges
        .into_iter()
        .filter(|r| r.0.0 <= y_coord && r.1.0 >= y_coord)
        .collect::<Vec<_>>();

    // println!("Filtered ranges: {:?}", filtered_ranges);

    !filtered_ranges.is_empty()
}

pub fn is_rectangle_disallowed(
    rect: &RectangleCornerCoordinates,
    disallowed_ranges: &Vec<((u64, u64), (u64, u64))>,
) -> bool {
    let (top_horizontal, bottom_horizontal, left_vertical, right_vertical) =
        get_ranges_from_rectangle(rect);

    let top_disallowed = is_horizontal_range_disallowed(&top_horizontal, disallowed_ranges);
    let bottom_disallowed = is_horizontal_range_disallowed(&bottom_horizontal, disallowed_ranges);
    let left_disallowed = is_vertical_range_disallowed(&left_vertical, disallowed_ranges);
    let right_disallowed = is_vertical_range_disallowed(&right_vertical, disallowed_ranges);

    // println!(
    //     "Top disallowed: {top_disallowed}, Bottom disallowed: {bottom_disallowed}, Left disallowed: {left_disallowed}, Right disallowed: {right_disallowed}"
    // );

    top_disallowed || bottom_disallowed || left_disallowed || right_disallowed
}
