#include <stdio.h>
#include <assert.h>

#include "file_utils.h"
#include "aoc_task.h"

void test_paper_roll_detection() {
    char input[] = {'.', '@', '.' };
    size_t input_length = sizeof(input) / sizeof(input[0]);

    unsigned int expected_count = 1;
    unsigned int actual_count = number_of_paper_rolls(input, input_length, '@');
    assert((expected_count == actual_count) && "Test failed: Expected 1 paper roll.");
}

void run_all_tests() {
    test_paper_roll_detection();
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