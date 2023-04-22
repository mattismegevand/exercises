#include <stdio.h>

#define IN 1
#define OUT 0
#define N_WORDS 10

int main() {
    int c, state, length;
    int words_lengths[N_WORDS];

    state = OUT;
    length = 0;

    for (int i = 0; i < 10; ++i)
        words_lengths[i] = 0;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            state = OUT;
            if (length > 0 && length < N_WORDS)
                ++words_lengths[length];
            length = 0;
        } else if (state == OUT) {
            state = IN;
        } 
        if (state == IN)
            ++length;
    }

    for (int i = 0; i < N_WORDS; ++i) {
        printf("\n%3d ", i);
        for (int j = 0; j < words_lengths[i]; ++j)
            putchar('-');
    }
    putchar('\n');
}
