#include <stdio.h>

#define TAB_STOP 8

int main() {
    int i = 0;
    char c;
    while ((c = getchar()) != EOF) {
        if (c == '\t') {
            int n = TAB_STOP - (i % TAB_STOP);
            while (n > 0) {
                putchar(' ');
                ++i;
                --n;
            }
        } else if (c == '\n') {
            putchar('\n');
            i = 0;
        } else {
            putchar(c);
            ++i;
        }
    }
    return 0;
}
