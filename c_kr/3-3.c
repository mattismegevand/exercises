#include <stdio.h>

void expand(char s[], char t[]) {
    int i, j, c;

    i = j = 0;

    while ((c = s[i++]) != '\0') {
        if (s[i] == '-' && s[i + 1] >= c) {
            while (c < s[i+1])
                t[j++] = c++;
            i++;
        } else {
            t[j++] = c;
        }
    }

    t[j] = '\0';
}

int main() {
    char s[] = "-a-b-cA-Z0-9";
    char t[80];
    expand(s, t);
    printf("%s\n", t);
}
