#include <stdio.h>

int binsearch(int x, int v[], int n) {
    int low, high, mid;
    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low+high)/2;
        if (v[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }
    if (low < n && v[low] == x)
        return low;
    return -1;
}

int main() {
    int v[] = {1, 2, 4, 8, 16, 32, 64};
    printf("%d", binsearch(4, v, 7));
}
