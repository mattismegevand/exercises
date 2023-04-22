#include <stdio.h>
#include <assert.h>

char lower(char c) {
    return ('A' <= c && c <= 'Z') ? c + 'a' - 'A' : c;
}

int main() {
    assert(lower('C') == 'c');
    assert(lower('b') == 'b');
}
