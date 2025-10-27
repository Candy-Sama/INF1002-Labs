#include <stdio.h>

int main() {
    int a = -1, b = 2;
    float x = 0.1, y = 1.5;
    char c = 'p';

    // Exercise 1
    printf("Question A: %d\n", a/b); // Print the result of a divided by b
    printf("Question B: %d\n", a * b); // Print the result of a multiplied by b
    printf("Question C: %d\n", (b*3)%4); // Print the result of (b*3)%4
    printf("Question D: %f\n", x * a); // Print the result of x multiplied by a
    printf("Question E: %f\n", x * y); // Print the result of x multiplied by y
    printf("Question F: %f\n", y / x); // Print the result of y / x
    printf("Question G: %c\n", c - 3); // Print the character that is 3 positions before c in the ASCII table

    // Exercise 2
    printf("%4d", a); // Print a with a minimum width of 4
    printf("%4d", b); // Print b with a minimum width of 4
    printf("a/0b = %d", a / b); // Print the result of a divided by b
    printf("%x", b); // Print b in hexadecimal format
    printf("%.2f", y); // Print y with 2 decimal places
    printf("%10.1f", x); // Print x with a minimum width of 10 and 1 decimal place

    return 0; // To end the program successfully
}