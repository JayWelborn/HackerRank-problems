#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int i, int j) {
    return i > j ? i : j;
}

int main() 
{
    int n;
    scanf("%d", &n);
  	for (int i = -n + 1; i < n; i++) {
        for (int j = -n + 1; j < n; j++) {
            printf("%d ", max(abs(i), abs(j)) + 1);
        }
        printf("\n");
    }
    return 0;
}
