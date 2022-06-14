#include <stdlib.h>

int main()
{
    int *p;
    p = (int *)malloc(5 * sizeof(int));
    for (int i = 0; i < 10; i++)
    {
        printf("%d", *p[i]);
    }
}