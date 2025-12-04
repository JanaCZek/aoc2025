#ifndef AOC_TASK_H
#define AOC_TASK_H

#include <stdio.h>

#define ADJACENT_FLAT_POSITIONS_COUNT 9
#define ADJACENT_THRESHOLD 4

typedef struct PaperRoll {
    int row_position;
    int column_position;
    int adjacent_count;
} PaperRoll;

int number_of_paper_rolls(const char *input_data, const size_t input_data_length, const char target_char) {
    int count = 0;
    for (size_t i = 0; i < input_data_length; ++i) {
        if (input_data[i] ==  target_char) {
            count++;
        }
    }
    return count;
}

void create_paper_rolls(const char *input_data, const size_t input_data_length, PaperRoll *paper_rolls, const char target_char) {
    int row = 0;
    int col = 0;
    int paper_roll_index = 0;
    
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

int number_of_adjacent_paper_rolls(PaperRoll *all_paper_rolls, int all_paper_rolls_count, PaperRoll* paper_roll) {
    PaperRoll paper_rolls_of_interest[ADJACENT_FLAT_POSITIONS_COUNT] = {
        {paper_roll->row_position - 1, paper_roll->column_position - 1, 0},
        {paper_roll->row_position - 1, paper_roll->column_position, 0},
        {paper_roll->row_position - 1, paper_roll->column_position + 1, 0},
        {paper_roll->row_position,     paper_roll->column_position - 1, 0},
        {paper_roll->row_position,     paper_roll->column_position + 1, 0},
        {paper_roll->row_position + 1, paper_roll->column_position - 1, 0},
        {paper_roll->row_position + 1, paper_roll->column_position, 0},
        {paper_roll->row_position + 1, paper_roll->column_position + 1, 0}
    };

    int adjacent_count = 0;
    for (int i = 0; i < all_paper_rolls_count; ++i) {
        for (int j = 0; j < ADJACENT_FLAT_POSITIONS_COUNT; ++j) {
            if (all_paper_rolls[i].row_position == paper_rolls_of_interest[j].row_position &&
                all_paper_rolls[i].column_position == paper_rolls_of_interest[j].column_position) {
                adjacent_count++;
                break;
            }
        }
    }

    paper_roll->adjacent_count = adjacent_count;

    return adjacent_count;
}

void detect_paper_rolls_to_remove(PaperRoll *all_paper_rolls, int all_paper_rolls_count, int* paper_roll_indexes_to_remove, int* removal_count) {
    int count = 0;
    for (int i = 0; i < all_paper_rolls_count; ++i) {
        if (all_paper_rolls[i].adjacent_count < ADJACENT_THRESHOLD) {
            paper_roll_indexes_to_remove[count] = i;
            count++;
        }
    }
    *removal_count = count;
}

#endif