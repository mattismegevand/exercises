#include <stdio.h>

int main() {
    int c, p;
    while ((c = getchar()) != EOF) {
        if (c == ' ' && p == ' ')
            continue;
        putchar(c);
        p = c;
    }
}
