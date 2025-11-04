#include <stdio.h>

int a[4] = {-1, 2, 10, 7}; //creates an array a that holds 4 integers
int b[4]; //creates an array b that holds 4 integers

int main()
{
    for (int i = 0; i < 4; i++) {
    b[i] = a[3-i]; //assigns each element in array b to be the reverse of the corresponding element in array a
    }

    printf("%d\n", a[3]); //why %d? because we are printing an integer
    printf("%d\n", b[3]);
    printf("%d\n", b[a[1]]); //prints the element in array b at the index specified by the second element in array a (which is 2)
}



