#include <stdio.h>

#define IN 1
#define OUT 0
#define N_CHARS 128

int main() {
    int c;
    int freq[N_CHARS];

    for (int i = 0; i < N_CHARS; ++i)
        freq[i] = 0;

    while ((c = getchar()) != EOF)
        ++freq[c];

    for (int i = 0; i < N_CHARS; ++i) {
        printf("\n%3d", i);
        for (int j = 0; j < freq[i]; ++j)
            putchar('-');
    }
    putchar('\n');
}
