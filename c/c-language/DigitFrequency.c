#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    char c = ' ';
    while (c != '\n') {
        c = getchar();
        switch (c) {
            case '0':   digits[0]++;
                        break;
            case '1':   digits[1]++;
                        break;
            case '2':   digits[2]++;
                        break;
            case '3':   digits[3]++;
                        break;
            case '4':   digits[4]++;
                        break;
            case '5':   digits[5]++;
                        break;
            case '6':   digits[6]++;
                        break;
            case '7':   digits[7]++;
                        break;
            case '8':   digits[8]++;
                        break;
            case '9':   digits[9]++;
                        break;
        }
    }
    printf("%d", digits[0]);
    for (int i = 1; i < 10; i++){
        printf(" %d", digits[i]);
    }
    return 0;
}
