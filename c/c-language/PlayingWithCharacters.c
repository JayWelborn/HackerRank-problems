#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    char c;
    scanf("%c", &c);
    printf("%c\n", c);

    char s[100];
    scanf("%s", &s);
    printf(s);
    printf("\n");
    scanf("\n");

    char sen[100];
    scanf("%[^\n]%*c", &sen);
    printf(sen);
    printf("\n");
    return 0;
}
