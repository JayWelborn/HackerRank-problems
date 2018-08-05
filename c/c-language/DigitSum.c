#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    int ones = n % 10;
    int tens = (n % 100 - ones) / 10;
    int hundreds = (n % 1000 - n % 100) / 100;
    int thousands = (n % 10000 - n % 1000) / 1000;
    int tenthousands = (n - n % 10000) / 10000;
    printf("%d", ones + tens + hundreds + thousands + tenthousands);
    return 0;
}
