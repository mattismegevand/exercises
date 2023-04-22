#include <stdio.h>

#define TAB_STOP 8

int main() {
    int i = 0, n = 0;
    char c;
    while ((c = getchar()) != EOF) {
        printf(" %d %d %c\n", i, n, c);
        if (c == ' ') {
            ++n;
        } else if (c == '\n') {
            putchar('\n');
            i = n = 0;
        } else {
            while (n > 0) {
                int tab = TAB_STOP - (i % TAB_STOP);
                if (n >= tab) {
                    putchar('#');
                    i += tab;
                    n -= tab;
                } else {
                    for ( ; n > 0; --n, ++i)
                        putchar(' ');
                }
            }
            putchar(c);
            ++i;
        }
    }
    return 0;
}
