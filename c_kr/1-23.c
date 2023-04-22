#include <stdio.h>

#define CODE 0
#define STRING 1
#define CHAR 2
#define COMMENT 3

int main() {
    int state = CODE;
    char c, p;

    while ((c = getchar()) != EOF) {
        if (state == CODE && ((p == '/' && c == '/') || (p == '/' && c == '*'))) {
            state = COMMENT;
        } else if (state == COMMENT && (c == '\n' || (p == '*' && c == '/'))) {
            state = CODE;
        } else if (c == '"' || c == '\'') {
            if (state == CODE)
                state = (c == '"') ? STRING : CHAR;
            else if (state == STRING && c == '"')
                state = CODE;
            else if (state == CHAR && c == '\'')
                state = CODE;
        }
        if (c != '/' && state != COMMENT) {
            if (p == '/')
                putchar(p);
            putchar(c);
        }
        p = c;
    }
    return 0;
}
