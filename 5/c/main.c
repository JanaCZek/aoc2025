#include <stdio.h>
#include <assert.h>

#include "file_utils.h"
#include "aoc_task.h"

#define TARGET_CHAR '@'

void test_paper_roll_detection() {
    char input[] = {'.', TARGET_CHAR, '.' };
    size_t input_length = sizeof(input) / sizeof(input[0]);

    unsigned int expected_count = 1;
    unsigned int actual_count = number_of_paper_rolls(input, input_length, TARGET_CHAR);
    assert((expected_count == actual_count) && "Test failed: Expected 1 paper roll.");

    char input_multiline[] = {'.', TARGET_CHAR, '.', '\n', TARGET_CHAR, TARGET_CHAR, '.', '\n', '.', '.', TARGET_CHAR};
    input_length = sizeof(input_multiline) / sizeof(input_multiline[0]);

    expected_count = 4;
    actual_count = number_of_paper_rolls(input_multiline, input_length, TARGET_CHAR);
    assert((expected_count == actual_count) && "Test failed: Expected 4 paper rolls.");
}

void test_paper_roll_creation() {
    char input[] = {'.', TARGET_CHAR, '.' };
    size_t input_length = sizeof(input) / sizeof(input[0]);

    unsigned int number_of_paper_rolls_count = number_of_paper_rolls(input, input_length, TARGET_CHAR);
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

void run_all_tests() {

    test_paper_roll_detection();
    test_paper_roll_creation();

    printf("\n***\n");
    printf("All tests passed!\n");
    printf("***\n\n");
}

int main() {

    run_all_tests();

    return 0;

    size_t buffer_size = 0;
    char *buffer = create_buffer_for_file("../input_small.txt", &buffer_size);

    if (buffer == NULL) {
        return -1;
    }

    int file_read_status = read_file_contents_into_buffer("../input_small.txt", buffer, buffer_size);
    
    free(buffer);

    return 0;
}