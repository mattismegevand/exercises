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

void itob(int n, char s[], int b)
{
    int i, sign;
    if ((sign = n) < 0)
        n = -n;
    i = 0;
    do {
        int x = n % b;
        s[i++] = (x > 10) ? x - 10 + 'A' : x + '0';
    } while ((n /= b) > 0);
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}

int main() {
    char s[80];
    itob(31, s, 2);
    printf("%s\n", s);
    itob(31, s, 8);
    printf("%s\n", s);
    itob(31, s, 10);
    printf("%s\n", s);
    itob(31, s, 16);
    printf("%s\n", s);
}
