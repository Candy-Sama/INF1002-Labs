#include <stdio.h>
#include <string.h>

char *a = "abcdef"; //creates a pointer to a string literal "abcdef"
char b[7]; //creates a character array b that can hold 7 characters

int main()
{
    strcpy(b, a); //copies the string pointed to by a into the array b
    for (int i = 0; i < 3; i++) {
        b[i] = b[i] + 1; //increments the ASCII value of each of the first three characters in array b by 1
    }

    printf("%c\n", a[0]); //prints the string pointed to by a
    printf("%c\n", b[0]); //prints the modified string in array b
    printf("%c\n", b[4]); //prints the fifth character in array b
    printf("%d\n", strlen(a)); //prints the length of the string pointed to by a
    printf("%d\n", strlen(b)); //prints the length of the string pointed to by b
    printf("%d\n", strcmp(a, b)); //compares the strings pointed to by a and b and prints the result of the comparison
}



