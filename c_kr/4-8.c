#include <stdio.h>

#define BUFSIZE 100

int buf = '\0';

int getch(void) {
    if (buf == '\0')
        return getchar();
    int c = buf;
    buf = '\0';
    return c;
}

void ungetch(int c) {
    buf = c;
}

int main(void) {
    ungetch('a');
    printf("%c\n", getch());
    return 0;
}