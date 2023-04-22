#include <stdio.h>

#define MAXLINE 1000

int my_getline(char line[], int maxline);
void reverse(char line[], int length);

int main() {
    int len;
    char line[MAXLINE];

    while ((len = my_getline(line, MAXLINE)) > 0) {
        reverse(line, len);
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

void reverse(char line[], int length) {
    char tmp;
    for (int i = 0, j = length - 1; i != j; ++i, --j) {
        tmp = line[i];
        line[i] = line[j];
        line[j] = tmp;
    }
}
