#ifndef AOC_TASK_H
#define AOC_TASK_H

#include <stdio.h>

typedef struct PaperRoll {
    unsigned int row_position;
    unsigned int column_position;
} PaperRoll;

unsigned int number_of_paper_rolls(const char *input_data, const size_t input_data_length, const char target_char) {
    unsigned int count = 0;
    for (size_t i = 0; i < input_data_length; ++i) {
        if (input_data[i] ==  target_char) {
            count++;
        }
    }
    return count;
}

void create_paper_rolls(const char *input_data, const size_t input_data_length, PaperRoll *paper_rolls, const char target_char) {
    unsigned int row = 0;
    unsigned int col = 0;
    unsigned int paper_roll_index = 0;
    
    for (size_t i = 0; i < input_data_length; ++i) {
        char current_char = input_data[i];
        if (current_char == '\n') {
            row++;
            col = 0;
        } else if (current_char == target_char) {
            paper_rolls[paper_roll_index].row_position = row;
            paper_rolls[paper_roll_index].column_position = col;
            paper_roll_index++;
            col++;
        } else {
            col++;
        }
    }
}

#endif