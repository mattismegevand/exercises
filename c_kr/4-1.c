#include <assert.h>
#include <stdio.h>

int strindex(char *s, char *t) {
    int slen, tlen, i, j, k;
    for (slen = 0; s[slen] != '\0'; slen++)
        ;
    for (tlen = 0; t[tlen] != '\0'; tlen++)
        ;
    for (i = slen - 1; i >= 0; i--) {
        for (j = 0, k = i; k < slen && t[j] != '\0' && s[k] == t[j]; j++, k++)
            ;
        if (t[j] == '\0')
            return i;
    }
    return -1;
}

int main() {
    assert(strindex("hello world", "world") == 6);
    assert(strindex("hello world", "hello") == 0);
    assert(strindex("hello world", "o w") == 4);
    assert(strindex("hello world", "x") == -1);
    assert(strindex("abc abc abc", "abc") == 8);
    assert(strindex("abc abc abc", "bca") == -1);
    assert(strindex("", "abc") == -1);
    return 0;
}