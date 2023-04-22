#include <stdio.h>

int main() {
    int c, nl, nt, ns;
    nl = nt = ns = 0;
    while ((c = getchar()) != EOF) {
        if (c == '\n')
            ++nl;
        else if (c == '\t')
            ++nt;
        else if (c == ' ')
            ++ns;
    }
    printf("Newlines: %d\nTabs: %d\nSpaces: %d\n", nl, nt, ns);
}
