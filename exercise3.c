#include <stdio.h>
#include <string.h>

/*
    Write a program that asks the user to type in a sentence of up to 255 characters in length. 
    Your program will then divide the sentence into its individual words (indicated by a space 
    character or punctuation mark) and print them line by line. Each line will include the word and 
    the number of characters in it, as shown below:

    Enter a sentence, up to 255 characters:
    The cat sat on the mat.

    The 3
    cat 3
    sat 3
    on 2
    the 3
    mat 3

    For an extra exercise, choose a secret “magic word” to be recognised by your program. If the 
    sentence contains the magic word, add the text “You said the magic word!” at the end of the 
    table. 
    
    Hints: 
    • Use fgets(buffer, n, stdin) to read a line of text that includes spaces, where 
    buffer is the array into which you want to place the characters and n is the maximum 
    number of characters to read. 
    • You can use the functions defined in ctype.h to test whether a character is a letter, 
    a space, or a punctuation mark.
*/

int main() 
{
    char sentence[256];
    char word[256];
    int i = 0, j = 0;
    int found_magic_word = 0;
    const char magic_word[] = "magic";

    printf("Enter a sentence, up to 255 characters:\n");
    fgets(sentence, sizeof(sentence), stdin); // Read the input sentence

    while (1) {
        // Skip non-letter characters
        while (sentence[i] != '\0' && !((sentence[i] >= 'A' && sentence[i] <= 'Z') || (sentence[i] >= 'a' && sentence[i] <= 'z'))) {
            i++;
        }
        if (sentence[i] == '\0') {
            break; // End of sentence
        }

        // Extract the word
        j = 0;
        while (sentence[i] != '\0' && ((sentence[i] >= 'A' && sentence[i] <= 'Z') || (sentence[i] >= 'a' && sentence[i] <= 'z'))) {
            word[j++] = sentence[i++];
        }
        word[j] = '\0'; // Null-terminate the word

        // Print the word and its length
        printf("%s %d\n", word, j);

        // Check for magic word
        if (strcmp(word, magic_word) == 0) {
            found_magic_word = 1;
        }
    }

    if (found_magic_word) {
        printf("You said the magic word!\n");
    }

    return 0;
}

