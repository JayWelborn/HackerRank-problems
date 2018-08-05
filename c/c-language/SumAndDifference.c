#include <stdio.h>

int main()
{
	int firstint, secondint;
    float firstfloat, secondfloat;
    
    scanf("%d %d", &firstint, &secondint);
    scanf("%f %f", &firstfloat, &secondfloat);
    
    printf("%d %d\n", firstint + secondint, firstint - secondint);
    printf("%.1f %.1f\n", firstfloat + secondfloat, firstfloat - secondfloat);
    
    return 0;
}
