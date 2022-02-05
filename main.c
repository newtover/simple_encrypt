#include <stdio.h>
#include <stdlib.h>

#include <unistd.h>
#include <fcntl.h>
#include "external/nacl/xor.h"


int main(int argc, char *argv[])
{
    int size_read;
    int MEMORY_STEP = 100000;
    int allocated_size = MEMORY_STEP;
    int actual_size = 0;

    unsigned char* file_contents = malloc(allocated_size);
    unsigned char* new_p;
    unsigned char key[] = {
        57, 76, 27, 181, 204, 115, 103, 45, 30, 13,
        230, 238, 180, 64, 82, 163, 129, 7, 197, 157,
        99, 174, 158, 38, 82, 80, 185, 164, 196, 213,
        119, 100, 203, 9, 247, 113, 48, 35, 27, 94
    };

    do {
        size_read = read(STDIN_FILENO, file_contents + actual_size, MEMORY_STEP);
        if (size_read == MEMORY_STEP) {
            allocated_size += MEMORY_STEP;
            actual_size += size_read;
            new_p = (unsigned char*) realloc(file_contents, allocated_size);
            if (new_p == NULL) {
                fprintf(stderr, "Error: can't reallocate memory");
                free(file_contents);
                exit(2);
            } else {
                file_contents = new_p;
                continue;
            }
        } else {
            actual_size += size_read;
            break;
        }
    } while(1);

    // fprintf(stderr, "size: %d\n", actual_size);

    unsigned char* encrypted = malloc(actual_size);
    crypto_stream_xor(encrypted, file_contents, actual_size, key+32, key);

    write(STDOUT_FILENO, encrypted, actual_size);

    free(file_contents);
    free(encrypted);

    exit(EXIT_SUCCESS);
}
