#include <stdio.h>

#define MAXLINE 1000

int my_getline(char line[], int maxline);
void trim_line(char line[], int length);

int main() {
    int len;
    char line[MAXLINE];

    while ((len = my_getline(line, MAXLINE)) > 0) {
        trim_line(line, len);
        printf("%s", line);
    }

    return 0;
}

int my_getline(char s[], int lim) {
    int c, i;
    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

void trim_line(char line[], int length) {
    int i = length - 1;
    while (line[i] == '\0' || line[i] == ' ' || line[i] == '\t')
        --i;
    line[i + 1] = '\0';
}
