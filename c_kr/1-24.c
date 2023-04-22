#include <stdio.h>

#define STACK_SIZE 100

char stack[STACK_SIZE];
int stack_pos = -1;

void push(char c) {
    if (stack_pos >= STACK_SIZE)
        return;
    stack[stack_pos] = c;
    ++stack_pos;
}

char pop(void) {
    if (stack_pos < 0)
        return NULL;
    char c = stack[stack_pos];
    --stack_pos;
    return c;
}

int main() {
    char c;
    while ((c = getchar()) != EOF) {
        if (c == '(' || c == '[' || c == '{')
            push(c);
        else if (c == ')' || c == ']' || c == '}') {
            char p = pop();
            if ((p == '(' && c != ')') || (p == '[' && c != ']') || (p == '{' && c != '}')) {
                printf("ERROR");
                return 1;
            }
        }
    }
    printf("OK");
    return 0;
}
