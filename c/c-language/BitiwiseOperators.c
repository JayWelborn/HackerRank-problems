#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
    int andmax = 0, ormax = 0, xormax = 0;
    for (int b = 1; b <= n; b++) {
        for (int a = 1; a < b; a++) {
            int and = a&b, or = a|b, xor = a^b;
            if (and > andmax && and < k) {
                andmax = and;
            }
            if (or > ormax && or < k) {
                ormax = or;
            }
            if (xor > xormax && xor < k) {
                xormax = xor;
            }
        }
    }
    printf("%d\n%d\n%d\n", andmax, ormax, xormax);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
