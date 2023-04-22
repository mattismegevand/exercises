#include <stdio.h>
#include <string.h>

void reverse(char s[]) {
    char c, i, j;

    for (i = 0, j = strlen(s) - 1; i < j; i++, j--) {
        c = s[i];
        s[i] = s[j];
        s[j] = c;
    }
}

void itoa(int n, char s[], int p)
{
    int i, sign;
    if ((sign = n) < 0)
        n = -n;
    i = 0;
    do {
        s[i++] = n % 10 + '0';
    } while ((n /= 10) > 0);
    if (sign < 0)
        s[i++] = '-';
    while (i < p)
        s[i++] = ' ';
    s[i] = '\0';
    reverse(s);
}

int main() {
    char s[80];
    itoa(31, s, 5);
    printf("%s\n", s);
}
