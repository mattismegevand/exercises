#include <stdio.h>

#define MAXCOLS 80

int last_blank(char line[], int len) {
    int lb = -1;
    for (int i = 0; i < len; ++i)
        if (line[i] == ' ' || line[i] == '\t' || line[i] == '\n')
            lb = i;
    return lb;
}

int main() {
    int i, j, k;
    char c;
    char line[MAXCOLS];

    i = 0;
    while ((c = getchar()) != EOF) {
        line[i] = c;
        ++i;

        if (i >= MAXCOLS || c == '\n') {
            int lb = last_blank(line, i);
            if (lb == -1) {
                for (j = 0; j < i; j++)
                    putchar(line[j]);
                if (c != '\n') putchar('\n');
                i = 0;
            } else {
                for (j = 0; j < lb; j++)
                    putchar(line[j]);
                putchar('\n');
                for (j = 0, k = lb + 1; k < i; ++j, ++k)
                    line[j] = line[k];
                i = j;
            }
        }
    }
    if (i > 0)
        for (j = 0; j < i; j++)
            putchar(line[j]);
    return 0;
}
