#include <stdio.h>

#define MAXLINE 80

void escape(char s[], char t[]) {
    int i, j;
    for (i = 0, j = 0; i < MAXLINE && s[i] != '\0'; i++) {
        switch (s[i]) {
            case '\n':
                t[j++] = '\\';
                t[j++] = 'n';
                break;
            case '\t':
                t[j++] = '\\';
                t[j++] = 't';
                break;
            default:
                t[j++] = s[i];
                break;
        }
    }
    t[j] = '\0';
}

void unescape(char s[], char t[]) {
    int i, j;
    for (i = 0, j = 0; i < MAXLINE - 1 && s[i] != '\0'; i++) {
        if (s[i] == '\\') {
            switch (s[i + 1]) {
                case 'n':
                    t[j++] = '\n';
                    break;
                case 't':
                    t[j++] = '\t';
                    break;
                default:
                    t[j++] = '\\';
                    t[j++] = s[i];
                    break;
            }
            i += 1;
        } else {
            t[j++] = s[i];
        }
    }
    t[i] = '\0';
}

int main() {
    char s[MAXLINE] = "test\n\tstring";
    char t[MAXLINE];
    escape(s, t);
    printf("%s\n", t);
    unescape(t, s);
    printf("%s\n", s);
}
