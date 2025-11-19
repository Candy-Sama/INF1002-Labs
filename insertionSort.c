/*******************************************************************************
Task Description: 
    One way to sort a collection of items is called insertion sort. The idea is 
    to start with an empty list, then insert items one at a time into it, placing 
    them in their correct position in the order each time. Your task is to 
    implement this algorithm using a linked list in a program insertionSort, so 
    that the program can sort an arbitrary number of words entered by the user.

    Every node in the list should store one word, composed entirely of lower-case 
    characters. The word may also contain apostrophes and hyphens, but not spaces, 
    quotes, or any other characters that do not normally appear in the middle of 
    English words. The word may be up to 32 characters long.

    The program should repeatedly ask the user to enter a word. The program should 
    automatically convert upper-case letters into lower-case ones, but reject words 
    containing characters other than letters, apostrophes, and hyphens.

    Each new word should be inserted into the list into its correct position in 
    alphabetical order. For example, if the list currently contains the words 
    "cat", "dog", and "monkey", and the user enters the word "elephant", the new 
    word should be inserted between "dog" and "monkey". You can use strcmp() to 
    determine whether a word comes before or after another in the alphabet (hyphens 
    and apostrophes will be sorted according to their ASCII values).

    The program stops asking for words when the user enters the special text 
    "***". The program should then print out the words, in order, one per line.

    Finally, the program should de-allocate all the memory that is has created and terminate.
    Note:
    1.	Use #define and comments as usual.
    2.	Check for memory allocation failures and report an error if they occur but 
        continue to execute the program.
    3.	There is no white space in the print after the colons (:).
    4.	Don’t use sys.argv[] for user inputs. Use other functions such as 
        scanf(), fgets(), fgetc(), etc.,

Some sample output is shown below, with the user input shown in red:
Example – 1:
    Please enter a word: 
    cat
    Please enter a word: 
    dog
    Please enter a word: 
    monkey
    Please enter a word: 
    elephant
    Please enter a word: 
    ***
    All the entered words in order:
    cat
    dog
    elephant
    monkey

Example – 2:
    Please enter a word:
    hello
    Please enter a word:
    good-bye
    Please enter a word:
    it's
    Please enter a word:
    invalid word
    Invalid word.
    Please enter a word:
    valid
    Please enter a word:
    "quote"
    Invalid word.
    Please enter a word:
    another
    Please enter a word:
    ***
    All the entered words in order:
    another
    good-bye
    hello
    it's
    valid
*******************************************************************************/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_WORD_LENGTH 32
struct word_node 
{
    char word[MAX_WORD_LENGTH + 1]; // Word stored in the node
    struct word_node *next;          // Pointer to the next node in the list
};
typedef struct word_node WORD_NODE;       // Define the WORD_NODE structure
typedef WORD_NODE *WORD_NODE_PTR;         // Define a pointer type to WORD_NODE

int main() 
{
    WORD_NODE_PTR head = NULL; // Initialize the head pointer to NULL

    char input[MAX_WORD_LENGTH + 10]; // Buffer for user input

    while (1) 
    {
        printf("Please enter a word:\n");
        if (fgets(input, sizeof(input), stdin) == NULL) 
        {
            fprintf(stderr, "Error reading input.\n");
            continue;
        }

        // Remove newline character from input
        input[strcspn(input, "\n")] = 0;

        // Check for termination condition
        if (strcmp(input, "***") == 0) 
        {
            break;
        }

        // Validate and convert input to lowercase
        int valid = 1;
        for (int i = 0; input[i] != '\0'; i++) 
        {
            if (isalpha(input[i])) 
            {
                input[i] = tolower(input[i]);
            } 
            else if (input[i] != '\'' && input[i] != '-') 
            {
                valid = 0;
                break;
            }
        }

        if (!valid) 
        {
            printf("Invalid word.\n");
            continue;
        }

        // Create a new node for the word
        WORD_NODE_PTR new_node = (WORD_NODE_PTR)malloc(sizeof(WORD_NODE));
        if (new_node == NULL) 
        {
            fprintf(stderr, "Memory allocation failed.\n");
            continue;
        }
        strcpy(new_node->word, input);
        new_node->next = NULL;

        // Insert the new node into the sorted list
        if (head == NULL || strcmp(new_node->word, head->word) < 0)  // If list is empty OR new word comes BEFORE the first word
        {
            new_node->next = head; // New word becomes first node
            head = new_node; // Update head to new node
        } 
        else // Insert in the middle or end 
        {
            WORD_NODE_PTR current = head; // Start from the head

             // Keep moving until we find where new word should go
            while (current->next != NULL && strcmp(current->next->word, new_node->word) < 0)
            {
                current = current->next; // Move to the next node
            }
            new_node->next = current->next; // Link new node to the next node
            current->next = new_node; // Link current node to new node
        }
    }

    // Print all the entered words in order
    printf("All the entered words in order:\n");
    WORD_NODE_PTR current = head;
    while (current != NULL) 
    {
        printf("%s\n", current->word);
        current = current->next;
    }

    // De-allocate all the memory
    current = head;
    while (current != NULL) 
    {
        WORD_NODE_PTR temp = current;
        current = current->next;
        free(temp);
    }

    return 0;
}
