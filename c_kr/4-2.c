#include <assert.h>
#include <ctype.h>
#include <math.h>

double atof(char s[]) {
    double val, power, e;
    int i, sign, esign;
    for (i = 0; isspace(s[i]); i++)
        ;
    sign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        i++;
    for (val = 0.0; isdigit(s[i]); i++)
        val = 10.0 * val + (s[i] - '0');
    if (s[i] == '.')
        i++;
    for (power = 1.0; isdigit(s[i]); i++) {
        val = 10.0 * val + (s[i] - '0');
        power *= 10;
    }
    if (s[i] == 'e' || s[i] == 'E')
        i++;
    esign = (s[i] == '-') ? -1 : 1;
    if (s[i] == '+' || s[i] == '-')
        i++;
    for (e = 0.0; isdigit(s[i]); i++)
        e = 10.0 * e + (s[i] - '0');
    return sign * val / power * pow(10., esign * e);
}

int main() {
    assert(fabs(atof("123.456") - 123.456) < 1e-3);
    assert(fabs(atof("0.00123") - 0.00123) < 1e-3);

    assert(fabs(atof("1e3") - 1000.0) < 1e-3);
    assert(fabs(atof("1E3") - 1000.0) < 1e-3);
    assert(fabs(atof("1e-3") - 0.001) < 1e-3);
    assert(fabs(atof("1E-3") - 0.001) < 1e-3);
    assert(fabs(atof("3.14e2") - 314.0) < 1e-3);
    assert(fabs(atof("3.14E2") - 314.0) < 1e-3);

    assert(fabs(atof("0") - 0.0) < 1e-3);
    assert(fabs(atof("-0") - 0.0) < 1e-3);
    assert(fabs(atof("-123.456") + 123.456) < 1e-3);
    assert(fabs(atof("-1e3") + 1000.0) < 1e-3);
    return 0;
}