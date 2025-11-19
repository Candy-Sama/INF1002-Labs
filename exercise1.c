// EXERCISE-1: USER-DEFINED DATA TYPES 
// Use  typedef  to  create  each  of  the  following  data  types,  using  macros  and  struct  where 
// appropriate: 
// a) A type, INTL_MONEY_VALUE, which can store a floating-point number to represent a 
// money value plus a 3-character string (e.g. SGD, USD, etc) to represent its currency. 
// b) A type, INTL_MONEY_VALUE_PTR, being a pointer to the international money value type 
// above. 
 
// TEST YOUR TYPES BY PUTTING THEM INTO A PROGRAM, DECLARING A FEW VARIABLES OF EACH 
// TYPE, AND CHECKING THAT IT COMPILES. 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CURRENCY_CODE_LENGTH 4  // 3 characters + null terminator
#define MAX_MONEY_VALUES 100 // Maximum number of money values
#define INPUT_BUFFER_SIZE 100 // Maximum input buffer size


typedef struct { // Define the INTL_MONEY_VALUE structure
    float amount;
    char currency[CURRENCY_CODE_LENGTH];
} INTL_MONEY_VALUE;

typedef INTL_MONEY_VALUE* INTL_MONEY_VALUE_PTR;

int main() 
{
    // Declare a few variables of INTL_MONEY_VALUE type
    INTL_MONEY_VALUE value1;
    INTL_MONEY_VALUE value2;

    // Initialize the first money value
    value1.amount = 100.50;
    strncpy(value1.currency, "USD", CURRENCY_CODE_LENGTH);

    // Initialize the second money value
    value2.amount = 200.75;
    strncpy(value2.currency, "EUR", CURRENCY_CODE_LENGTH);

    // Print the money values
    printf("Money Value 1: %.2f %s\n", value1.amount, value1.currency);
    printf("Money Value 2: %.2f %s\n", value2.amount, value2.currency);

    // Declare a pointer to INTL_MONEY_VALUE
    INTL_MONEY_VALUE_PTR ptrValue;

    // Allocate memory for the pointer
    ptrValue = (INTL_MONEY_VALUE_PTR)malloc(sizeof(INTL_MONEY_VALUE));
    if (ptrValue == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1; // Exit if memory allocation fails
    }

    // Initialize the money value via pointer
    ptrValue->amount = 300.00;
    strncpy(ptrValue->currency, "SGD", CURRENCY_CODE_LENGTH);

    // Print the money value via pointer
    printf("Money Value via Pointer: %.2f %s\n", ptrValue->amount, ptrValue->currency);

    // Free allocated memory
    free(ptrValue);

    return 0;
}