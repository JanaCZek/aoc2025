use aoc_day_9::{
    HorizontalRange, RectangleCornerCoordinates, VerticalRange, get_all_corner_coords_of_rectangle,
};

// Run tests with output
// cargo test -- --nocapture

#[test]
fn test_parses_string_to_coordinates() {
    let input = "7,1\n3,4\n5,6";
    let expected = vec![(7, 1), (3, 4), (5, 6)];

    let result = aoc_day_9::parse_strings_to_coordinates(input);

    assert_eq!(result, expected);
}

#[test]
fn test_calculates_area_of_two_coordinates() {
    let coords = [(2, 5), (11, 1)];
    let expected_area = 50;

    let result = aoc_day_9::calculate_area(coords[0], coords[1]);

    assert_eq!(result, expected_area);
}

#[test]
fn test_creates_matrix_of_areas() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";
    let expected_max_area = 50;

    let coords = aoc_day_9::parse_strings_to_coordinates(input);
    let (_, result_max_area) = aoc_day_9::create_matrix_of_areas(&coords);

    assert_eq!(result_max_area, expected_max_area);
}

#[test]
fn test_creates_green_tiles() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";

    let should_contain = vec![(8, 1), (7, 2), (7, 3)];
    let coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&coords);
    let green_tile_connected_coords = aoc_day_9::create_green_tiles(&green_tile_coords);

    let mut all_green_tiles = green_tile_coords.clone();
    all_green_tiles.extend(green_tile_connected_coords);
    let green_tile_coords = all_green_tiles;

    for coord in should_contain {
        assert!(green_tile_coords.contains(&coord));
    }

    let should_not_contain = vec![(0, 0)];
    for coord in should_not_contain {
        assert!(!green_tile_coords.contains(&coord));
    }
}

#[test]
fn test_only_contains_green_or_red_tiles() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";
    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);
    let green_tile_connected_coords = aoc_day_9::create_green_tiles(&green_tile_coords);

    let mut all_green_tiles = green_tile_coords.clone();
    all_green_tiles.extend(green_tile_connected_coords);
    let green_tile_coords = all_green_tiles;

    let coords_one = (11, 1);
    let coords_two = (7, 3);

    let result = aoc_day_9::only_contains_green_or_red_tiles(
        coords_one,
        coords_two,
        &red_tile_coords,
        &green_tile_coords,
    );

    assert!(result);
}

#[test]
fn test_matrix_of_only_contains_green_or_red_tiles() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";

    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);

    let (_, max_area) =
        aoc_day_9::create_matrix_of_limited_areas(&red_tile_coords, &green_tile_coords);

    assert_eq!(max_area, 24);
}

#[test]
fn test_gets_all_coords_of_rectangle() {
    let coords_one = (2, 3);
    let coords_two = (4, 5);

    let expected_coords = vec![
        (2, 3),
        (3, 3),
        (4, 3),
        (2, 4),
        (3, 4),
        (4, 4),
        (2, 5),
        (3, 5),
        (4, 5),
    ];

    let result = aoc_day_9::get_all_coords_of_rectangle(coords_one, coords_two);

    assert_eq!(result.len(), expected_coords.len());
    for coord in expected_coords {
        assert!(result.contains(&coord));
    }
}

#[test]
fn test_creates_disallowed_coordinate_ranges() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";

    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);

    let should_contain = vec![((2, 1), (6, 1)), ((2, 6), (8, 6)), ((2, 7), (8, 7))];
    let should_not_contain = vec![((1, 3), (2, 3))];

    let disallowed_coord_ranges =
        aoc_day_9::create_disallowed_ranges(&red_tile_coords, &green_tile_coords);

    println!("Disallowed coord ranges: {disallowed_coord_ranges:?}");

    for coord in should_contain {
        assert!(disallowed_coord_ranges.contains(&coord));
    }

    for coord in should_not_contain {
        assert!(!disallowed_coord_ranges.contains(&coord));
    }
}

#[test]
fn test_is_any_coord_disallowed() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";

    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);

    let disallowed_coord_ranges =
        aoc_day_9::create_disallowed_ranges(&red_tile_coords, &green_tile_coords);

    let all_cords = aoc_day_9::get_all_coords_of_rectangle((11, 1), (2, 3));

    let result = aoc_day_9::is_any_coord_disallowed(&all_cords, &disallowed_coord_ranges);
    assert!(result);

    let all_cords = aoc_day_9::get_all_coords_of_rectangle((9, 5), (2, 3));

    let result = aoc_day_9::is_any_coord_disallowed(&all_cords, &disallowed_coord_ranges);
    assert!(!result);
}

#[test]
fn test_gets_all_perimeter_coords_of_rectangle() {
    let coords_one = (2, 3);
    let coords_two = (4, 4);

    let expected_coords = vec![(2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (4, 4)];

    let result = aoc_day_9::get_all_perimeter_coords_of_rectangle(coords_one, coords_two);

    assert_eq!(result.len(), expected_coords.len());
    for coord in expected_coords {
        assert!(result.contains(&coord));
    }

    let expected_coords = vec![(2, 3), (3, 3), (4, 3), (2, 4), (3, 4), (4, 4)];

    let result = aoc_day_9::get_all_perimeter_coords_of_rectangle(coords_two, coords_one);

    assert_eq!(result.len(), expected_coords.len());
    for coord in expected_coords {
        assert!(result.contains(&coord));
    }
}

#[test]
fn test_gets_all_corner_coords_of_rectangle() {
    let coords_one = (2, 3);
    let coords_two = (4, 5);

    let expected_coords = RectangleCornerCoordinates {
        top_left: (2, 3),
        top_right: (4, 3),
        bottom_left: (2, 5),
        bottom_right: (4, 5),
    };

    let result = aoc_day_9::get_all_corner_coords_of_rectangle(coords_one, coords_two);

    assert_eq!(result, expected_coords);
}

#[test]
fn test_gets_all_ranges_from_rectange() {
    let rectangle = RectangleCornerCoordinates {
        top_left: (2, 3),
        top_right: (4, 3),
        bottom_left: (2, 5),
        bottom_right: (4, 5),
    };

    let expected_ranges = (
        HorizontalRange {
            start: (2, 3),
            end: (4, 3),
        },
        HorizontalRange {
            start: (2, 5),
            end: (4, 5),
        },
        VerticalRange {
            start: (2, 3),
            end: (2, 5),
        },
        VerticalRange {
            start: (4, 3),
            end: (4, 5),
        },
    );

    let result = aoc_day_9::get_ranges_from_rectangle(&rectangle);

    assert_eq!(result, expected_ranges);
}

#[test]
fn test_detects_disallowed_horizontal_ranges() {
    let disallowed_ranges = vec![((2, 1), (6, 1))];

    let disallowed = vec![
        HorizontalRange {
            start: (2, 1),
            end: (6, 1),
        },
        HorizontalRange {
            start: (2, 1),
            end: (5, 1),
        },
        HorizontalRange {
            start: (3, 1),
            end: (6, 1),
        },
        HorizontalRange {
            start: (3, 1),
            end: (5, 1),
        },
        HorizontalRange {
            start: (2, 1),
            end: (7, 1),
        },
    ];

    let allowed = vec![HorizontalRange {
        start: (0, 1),
        end: (1, 1),
    }];

    for range in disallowed {
        let result = aoc_day_9::is_horizontal_range_disallowed(&range, &disallowed_ranges);
        assert!(result, "Range {range:?} was expected to be disallowed");
    }

    for range in allowed {
        let result = aoc_day_9::is_horizontal_range_disallowed(&range, &disallowed_ranges);
        assert!(!result, "Range {range:?} was expected to be allowed");
    }
}

#[test]
fn test_detects_disallowed_vertical_ranges() {
    let disallowed_ranges = vec![((2, 2), (6, 2)), ((1, 3), (4, 3))];

    let disallowed = vec![
        VerticalRange {
            start: (2, 2),
            end: (2, 3),
        },
        VerticalRange {
            start: (1, 2),
            end: (1, 3),
        },
        VerticalRange {
            start: (5, 2),
            end: (5, 3),
        },
        VerticalRange {
            start: (6, 2),
            end: (6, 3),
        },
    ];

    let allowed = vec![VerticalRange {
        start: (7, 2),
        end: (7, 3),
    }];

    for range in disallowed {
        let result = aoc_day_9::is_vertical_range_disallowed(&range, &disallowed_ranges);
        assert!(result);
    }

    for range in allowed {
        let result = aoc_day_9::is_vertical_range_disallowed(&range, &disallowed_ranges);
        assert!(!result);
    }
}

#[test]
fn test_is_rectangle_disallowed() {
    let input = "7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3";

    let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(input);
    let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);

    let disallowed_coord_ranges =
        aoc_day_9::create_disallowed_ranges(&red_tile_coords, &green_tile_coords);

    let disallowed_rectangles = vec![
        get_all_corner_coords_of_rectangle((11, 1), (2, 3)),
        get_all_corner_coords_of_rectangle((2, 5), (9, 7)),
    ];

    let allowed_rectangles = vec![get_all_corner_coords_of_rectangle((7, 3), (11, 1))];

    for rectangle in disallowed_rectangles {
        let result = aoc_day_9::is_rectangle_disallowed(&rectangle, &disallowed_coord_ranges);
        // assert!(result, "Rectangle {rectangle:?} was expected to be disallowed");
    }

    for rectangle in allowed_rectangles {
        let result = aoc_day_9::is_rectangle_disallowed(&rectangle, &disallowed_coord_ranges);
        // assert!(!result, "Rectangle {rectangle:?} was expected to be allowed");
    }
}

// #[test]
// fn input_test_part_one() {
//     let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\9\\input.txt").unwrap();

//     let mut coords = aoc_day_9::parse_strings_to_coordinates(&contents);
//     let (matrix, max_area) = aoc_day_9::create_matrix_of_areas(&coords);

//     println!("Max area: {}", max_area);
//     assert_eq!(true, true);
// }

// #[test]
// fn input_test_part_two() {
//     let contents = fs::read_to_string("C:\\Projects\\playground\\aoc2025\\9\\input.txt").unwrap();

//     let red_tile_coords = aoc_day_9::parse_strings_to_coordinates(&contents);
//     let green_tile_coords = aoc_day_9::create_green_tiles(&red_tile_coords);

//     let (_, max_area) = aoc_day_9::create_matrix_of_limited_areas(&red_tile_coords, &green_tile_coords);

//     println!("Max area: {}", max_area);
//     assert_eq!(true, true);
// }
