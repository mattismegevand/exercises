#include <stdio.h>

#define signed_range(type) \
    printf("Signed " #type " range: %lld to %lld\n", (long long) -(1LL << (sizeof(type) * 8 - 1)), (long long) ((1LL << (sizeof(type) * 8 - 1)) - 1))

#define unsigned_range(type) \
    printf("Unsigned " #type " range: 0 to %llu\n", (unsigned long long) ((1ULL << (sizeof(type) * 8)) - 1))

int main() {
    signed_range(char);
    unsigned_range(unsigned char);

    signed_range(short);
    unsigned_range(unsigned short);

    signed_range(int);
    unsigned_range(unsigned int);

    signed_range(long);
    unsigned_range(unsigned long);

    return 0;
}
