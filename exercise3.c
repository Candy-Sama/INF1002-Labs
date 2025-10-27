/* Exercise 3 
Create a new program called “bmi” that asks the user to type in his or her weight in 
kilograms and height in metres, then calculates and displays the user’s BMI to one decimal 
place. The application should also evaluate whether the user is underweight or overweight 
according to the following table:
*/

#include <stdio.h>

int main() {
    float weight, height, bmi;

    // Prompt user for weight in kilograms
    printf("Enter your weight in kilograms: ");
    scanf("%f", &weight);

    // Prompt user for height in metres
    printf("Enter your height in metres: ");
    scanf("%f", &height);

    // Calculate BMI
    bmi = weight / (height * height);

    // Display BMI to one decimal place
    printf("Your BMI is: %.1f\n", bmi);

    // Evaluate and display weight category
    if (bmi < 18.5) {
        printf("You are underweight.\n");
    } else if (bmi >= 18.5 && bmi < 24.9) {
        printf("That is within the normal range.\n");
    } else {
        printf("You are overweight.\n");
    }

    return 0; // To end the program successfully
}