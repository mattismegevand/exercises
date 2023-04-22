#include <stdio.h>

#define MAXLINE 80

int main() {
    int i, lim = MAXLINE;
    char c, s[MAXLINE];
    while (i < lim-1) {
        c = getchar();
        if (c == '\n')
            break;
        if (c == EOF)
            break;
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    printf("s: %s", s);
    return 0;
}
