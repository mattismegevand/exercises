#include <stdio.h>
#include <assert.h>
#include <math.h>

char lower(char c) {
    if ('A' <= c && c <= 'Z')
        return c + 'a' - 'A';
    return c;
}

int hex_to_dec(char c) {
    if ('a' <= c && c <= 'f')
        return c - 'a' + 10;
    return c - '0';
}

int htoi(char s[]) {
    int i, n;
    i = 0;
    if (s[0] != '\0' && s[0] == '0' && s[1] != '\0' && lower(s[1]) == 'x')
        i = 2;
    for (n = 0; s[i] != '\0'; i++)
        n = 16 * n + hex_to_dec(lower(s[i]));
    return n;
}

int main() {
    assert(htoi("0x5c6") == htoi("5C6"));
    assert(htoi("0x5c6") == 1478);
    return 0;
}
