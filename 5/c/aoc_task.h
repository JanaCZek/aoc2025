#ifndef AOC_TASK_H
#define AOC_TASK_H

#include <stdio.h>

struct PaperRoll {
    unsigned int row_position;
    unsigned int column_position;
} typedef PaperRoll;

unsigned int number_of_paper_rolls(const char *input_data, const size_t input_data_length, const char target_char) {
    unsigned int count = 0;
    for (size_t i = 0; i < input_data_length; ++i) {
        if (input_data[i] ==  target_char) {
            count++;
        }
    }
    return count;
}

void create_paper_rolls(const char *input_data, const size_t input_data_length, PaperRoll *paper_rolls) {
    unsigned int row = 0;
    unsigned int col = 0;
    
    for (size_t i = 0; i < input_data_length; ++i) {
        char current_char = input_data[i];
        if (current_char == '\n') {
            row++;
            col = 0;
        } else if (current_char == '@') {
            paper_rolls[row].row_position = row;
            paper_rolls[row].column_position = col;
            col++;
        } else {
            col++;
        }
    }
}

#endif