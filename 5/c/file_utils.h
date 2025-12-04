#ifndef FILE_UTILS_H
#define FILE_UTILS_H

#include <stdlib.h>
#include <stdio.h>

int file_character_count(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        return -1;
    }
    int count = 0;
    while (fgetc(file) != EOF) {
        count++;
    }
    fclose(file);
    return count;
}

char* create_buffer_for_file(const char *filename, size_t *out_size) {
    int size = file_character_count(filename);
    if (size < 0) {
        return NULL;
    }
    char *buffer = (char *)malloc(size + 1);
    if (buffer == NULL) {
        return NULL;
    }
    *out_size = size;
    return buffer;
}

int read_file_contents_into_buffer(const char *filename, char *buffer, size_t buffer_size) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        return -1;
    }
    size_t total_read = 0;
    int ch;
    while ((ch = fgetc(file)) != EOF && total_read < buffer_size - 1) {
        buffer[total_read++] = (char)ch;
    }
    buffer[total_read] = '\0';
    fclose(file);

    return (int)total_read;
}

#endif