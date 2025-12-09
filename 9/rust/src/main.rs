use std::fs;

fn main() {
    let input = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\9\\input.txt").unwrap();

    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(&input);
    let green_tile_coords = aoc_day_9::create_green_tiles_between_adjacent_red_tiles(&red_tile_coords);

    let (_, max_area) = aoc_day_9::create_matrix_of_limited_areas(&red_tile_coords, &green_tile_coords);

    println!("Max area: {max_area}");
}
