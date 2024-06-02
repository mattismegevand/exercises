#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFSIZE 100
#define MAXOP 100
#define MAXVAL 100
#define NUMBER '0'
#define IDENTIFIER '1'
#define VARIABLE '2'

char buf[BUFSIZE];
int bufp = 0;

int getch(void) {
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) {
    if (bufp >= BUFSIZE)
        printf("ungetch: too many characters\n");
    else
        buf[bufp++] = c;
}

int getop(char s[]) {
    int i, c;
    while ((s[0] = c = getch()) == ' ' || c == '\t')
        ;
    s[1] = '\0';
    if (!isdigit(c) && c != '.' && c != '-')
        return ('a' <= c && c <= 'z') ? VARIABLE : c;
    i = 0;
    if (isalpha(c)) {
        while (isalpha(s[++i] = c = getch()))
            ;
        s[i] = '\0';
        if (c != EOF)
            ungetch(c);
        return IDENTIFIER;
    } else {
        if (isdigit(c) || c == '-')
            while (isdigit(s[++i] = c = getch()))
                ;
        if (c == '.')
            while (isdigit(s[++i] = c = getch()))
                ;
        s[i] = '\0';
        if (c != EOF)
            ungetch(c);
        return NUMBER;
    }
}

int sp = 0;
double val[MAXVAL];

void push(double f) {
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf("error: stack full, can't push %g\n", f);
}
double pop(void) {
    if (sp > 0)
        return val[--sp];
    else {
        printf("error: stack empty\n");
        return 0.0;
    }
}

int main(void) {
    int type, current_var;
    double op2, tmp;
    double variable[26] = {0};
    char s[MAXOP];
    current_var = -1;
    while ((type = getop(s)) != EOF) {
        switch (type) {
            case NUMBER:
                push(atof(s));
                break;
            case IDENTIFIER:
                if (strcmp(s, "sin") == 0) {
                    push(sin(pop()));
                } else if (strcmp(s, "cos") == 0) {
                    push(cos(pop()));
                } else if (strcmp(s, "exp") == 0) {
                    push(exp(pop()));
                } else if (strcmp(s, "pow") == 0) {
                    op2 = pop();
                    push(pow(pop(), op2));
                } else {
                    printf("error: unknown identifier %s\n", s);
                }
                break;
            case VARIABLE:
                current_var = s[0] - 'a';
                break;
            case '+':
                push(pop() + pop());
                break;
            case '*':
                push(pop() * pop());
                break;
            case '-':
                op2 = pop();
                push(pop() - op2);
                break;
            case '/':
                op2 = pop();
                if (op2 != 0.0)
                    push(pop() / op2);
                else
                    printf("error: zero divisor\n");
                break;
            case '%':
                op2 = pop();
                push((int)pop() % (int)op2);
                break;
            case '?':
                tmp = pop();
                printf("\t%.8g\n", tmp);
                push(tmp);
                break;
            case '#':
                tmp = pop();
                push(tmp);
                push(tmp);
                break;
            case '~':
                op2 = pop();
                tmp = pop();
                push(op2);
                push(tmp);
                break;
            case '!':
                sp = 0;
                break;
            case '$':
                push(variable[current_var]);
                break;
            case '=':
                if (current_var == -1)
                    printf("error: no variable name\n");
                else
                    variable[current_var] = pop();
                break;
            case '\n':
                printf("\t%.8g\n", pop());
                break;
            default:
                printf("error: unknown command %s\n", s);
                break;
        }
    }
    return 0;
}