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
    let width = if coords_one.0 > coords_two.0 {
        coords_one.0 - coords_two.0
    } else {
        coords_two.0 - coords_one.0
    };

    let height = if coords_one.1 > coords_two.1 {
        coords_one.1 - coords_two.1
    } else {
        coords_two.1 - coords_one.1
    };

    (width + 1) * (height + 1)
}

pub fn create_matrix_of_areas(coords: &Vec<(u64, u64)>) -> (Vec<Vec<u64>>, u64) {
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