#include <stdio.h>
#include <assert.h>

#include "file_utils.h"
#include "aoc_task.h"

#define TARGET_CHAR '@'

void test_paper_roll_detection()
{
    char input[] = {'.', TARGET_CHAR, '.'};
    size_t input_length = sizeof(input) / sizeof(input[0]);

    int expected_count = 1;
    int actual_count = number_of_paper_rolls(input, input_length, TARGET_CHAR);
    assert((expected_count == actual_count) && "Test failed: Expected 1 paper roll.");

    char input_multiline[] = {'.', TARGET_CHAR, '.', '\n', TARGET_CHAR, TARGET_CHAR, '.', '\n', '.', '.', TARGET_CHAR};
    input_length = sizeof(input_multiline) / sizeof(input_multiline[0]);

    expected_count = 4;
    actual_count = number_of_paper_rolls(input_multiline, input_length, TARGET_CHAR);
    assert((expected_count == actual_count) && "Test failed: Expected 4 paper rolls.");
}

void test_paper_roll_creation()
{
    char input[] = {'.', TARGET_CHAR, '.'};
    size_t input_length = sizeof(input) / sizeof(input[0]);

    int number_of_paper_rolls_count = number_of_paper_rolls(input, input_length, TARGET_CHAR);
    PaperRoll paper_rolls[number_of_paper_rolls_count];

    create_paper_rolls(input, input_length, paper_rolls, TARGET_CHAR);

    assert((paper_rolls[0].row_position == 0) && (paper_rolls[0].column_position == 1) && "Test failed: Paper roll position incorrect.");

    char input_multiline[] = {'.', TARGET_CHAR, '.', '\n', TARGET_CHAR, TARGET_CHAR, '.', '\n', '.', '.', TARGET_CHAR};
    input_length = sizeof(input_multiline) / sizeof(input_multiline[0]);

    number_of_paper_rolls_count = number_of_paper_rolls(input_multiline, input_length, TARGET_CHAR);
    PaperRoll paper_rolls_multi[number_of_paper_rolls_count];

    create_paper_rolls(input_multiline, input_length, paper_rolls_multi, TARGET_CHAR);

    assert((paper_rolls_multi[0].row_position == 0) && (paper_rolls_multi[0].column_position == 1) && "Test failed: First paper roll position incorrect.");
    assert((paper_rolls_multi[1].row_position == 1) && (paper_rolls_multi[1].column_position == 0) && "Test failed: Second paper roll position incorrect.");
    assert((paper_rolls_multi[2].row_position == 1) && (paper_rolls_multi[2].column_position == 1) && "Test failed: Third paper roll position incorrect.");
    assert((paper_rolls_multi[3].row_position == 2) && (paper_rolls_multi[3].column_position == 2) && "Test failed: Fourth paper roll position incorrect.");
}

void test_adjacent_paper_rolls()
{
    PaperRoll paper_roll = {0, 1, 0};
    PaperRoll all_paper_rolls[] = {
        {0, 1, 0},
        {0, 2, 0}};

    int all_paper_rolls_count = 1;
    int number_of_paper_rolls_count = number_of_adjacent_paper_rolls(all_paper_rolls, all_paper_rolls_count, &paper_roll);

    assert((number_of_paper_rolls_count == 0) && "Test failed: Expected 0 adjacent paper rolls.");
    assert((paper_roll.adjacent_count == 0) && "Test failed: Paper roll adjacent count incorrect.");

    all_paper_rolls_count = 2;
    number_of_paper_rolls_count = number_of_adjacent_paper_rolls(all_paper_rolls, all_paper_rolls_count, &paper_roll);

    assert((number_of_paper_rolls_count == 1) && "Test failed: Expected 1 adjacent paper roll.");
    assert((paper_roll.adjacent_count == 1) && "Test failed: Paper roll adjacent count incorrect.");

    PaperRoll fully_adjacent_rolls[] = {
        {0, 0, 0}, {0, 1, 0}, {0, 2, 0}, {1, 0, 0}, {1, 1, 0}, {1, 2, 0}, {2, 0, 0}, {2, 1, 0}, {2, 2, 0}};
    PaperRoll fully_adjacent_roll = {1, 1, 0};

    all_paper_rolls_count = 9;
    number_of_paper_rolls_count = number_of_adjacent_paper_rolls(fully_adjacent_rolls, all_paper_rolls_count, &fully_adjacent_roll);

    assert((number_of_paper_rolls_count == 8) && "Test failed: Expected 8 adjacent paper rolls.");
    assert((fully_adjacent_roll.adjacent_count == 8) && "Test failed: Fully adjacent paper roll adjacent count incorrect.");
}

void test_detection_of_paper_rolls_to_remove()
{
    PaperRoll all_paper_rolls[] = {
        {0, 1, 0},
        {0, 2, 0}};

    int all_paper_rolls_count = 2;
    int paper_roll_indexes_to_remove[all_paper_rolls_count];
    int removal_count = 0;

    detect_paper_rolls_to_remove(all_paper_rolls, all_paper_rolls_count, paper_roll_indexes_to_remove, &removal_count);

    assert((removal_count == 2) && "Test failed: Paper rolls were not removed.");
}

void test_removal_of_detected_paper_rolls()
{
    PaperRoll all_paper_rolls[] = {
        {0, 1, 0},
        {0, 2, 0}};

    int all_paper_rolls_count = sizeof(all_paper_rolls) / sizeof(all_paper_rolls[0]);

    int paper_roll_indexes_to_remove[] = {0};
    int removal_count = sizeof(paper_roll_indexes_to_remove) / sizeof(paper_roll_indexes_to_remove[0]);

    int updated_paper_rolls_count = all_paper_rolls_count - removal_count;
    PaperRoll updated_paper_rolls[updated_paper_rolls_count];

    remove_detected_paper_rolls(
        all_paper_rolls,
        all_paper_rolls_count,
        paper_roll_indexes_to_remove,
        removal_count,
        updated_paper_rolls);

    assert((updated_paper_rolls[0].row_position == 0) && (updated_paper_rolls[0].column_position == 2) && "Test failed: Updated paper roll position incorrect.");
}

void run_all_tests()
{
    test_paper_roll_detection();
    test_paper_roll_creation();
    test_adjacent_paper_rolls();
    test_detection_of_paper_rolls_to_remove();
    test_removal_of_detected_paper_rolls();

    printf("\n***\n");
    printf("All tests passed!\n");
    printf("***\n\n");
}

int run_part_one(const char *file_path)
{
    size_t buffer_size = 0;

    char *buffer = create_buffer_for_file(file_path, &buffer_size);

    if (buffer == NULL)
    {
        return -1;
    }

    int file_read_status = read_file_contents_into_buffer(file_path, buffer, buffer_size);

    if (file_read_status < 0)
    {
        free(buffer);
        return -1;
    }

    printf("Part one\n");

    int number_of_paper_rolls_count = number_of_paper_rolls(buffer, buffer_size, TARGET_CHAR);
    PaperRoll paper_rolls[number_of_paper_rolls_count];

    create_paper_rolls(buffer, buffer_size, paper_rolls, TARGET_CHAR);

    for (int i = 0; i < number_of_paper_rolls_count; ++i)
    {
        number_of_adjacent_paper_rolls(paper_rolls, number_of_paper_rolls_count, &paper_rolls[i]);
    }

    int paper_roll_indexes_to_remove[number_of_paper_rolls_count];
    int removal_count = 0;

    detect_paper_rolls_to_remove(paper_rolls, number_of_paper_rolls_count, paper_roll_indexes_to_remove, &removal_count);

    printf("Number of paper rolls to remove: %d\n", removal_count);

    free(buffer);

    return 0;
}

int run_part_two(const char *file_path)
{
    size_t buffer_size = 0;

    char *buffer = create_buffer_for_file(file_path, &buffer_size);

    if (buffer == NULL)
    {
        return -1;
    }

    int file_read_status = read_file_contents_into_buffer(file_path, buffer, buffer_size);

    if (file_read_status < 0)
    {
        free(buffer);
        return -1;
    }

    printf("Part two\n");

    int number_of_paper_rolls_count = number_of_paper_rolls(buffer, buffer_size, TARGET_CHAR);
    PaperRoll paper_rolls[number_of_paper_rolls_count];
    PaperRoll updated_paper_rolls[number_of_paper_rolls_count];

    PaperRoll *paper_rolls_ptr = paper_rolls;

    int removal_count = 0;
    int total_removal_count = 0;

    create_paper_rolls(buffer, buffer_size, paper_rolls_ptr, TARGET_CHAR);

    while (1)
    {
        for (int i = 0; i < number_of_paper_rolls_count; ++i)
        {
            number_of_adjacent_paper_rolls(paper_rolls_ptr, number_of_paper_rolls_count, &paper_rolls_ptr[i]);
        }

        int paper_roll_indexes_to_remove[number_of_paper_rolls_count];

        detect_paper_rolls_to_remove(paper_rolls_ptr, number_of_paper_rolls_count, paper_roll_indexes_to_remove, &removal_count);

        int updated_paper_rolls_count = number_of_paper_rolls_count - removal_count;

        remove_detected_paper_rolls(
            paper_rolls_ptr,
            number_of_paper_rolls_count,
            paper_roll_indexes_to_remove,
            removal_count,
            updated_paper_rolls);

        if (removal_count == 0)
        {
            break;
        }

        total_removal_count += removal_count;
        number_of_paper_rolls_count = updated_paper_rolls_count;
        paper_rolls_ptr = updated_paper_rolls;
    }

    printf("Number of paper rolls to remove: %d\n", total_removal_count);

    free(buffer);

    return 0;
}

// When debugging, "input.txt"
// When not debugging, "../input.txt"
int main()
{
    run_all_tests();

    run_part_one("../input.txt");

    run_part_two("../input.txt");

    return 0;
}