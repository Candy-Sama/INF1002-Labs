/* Write a program that creates and manipulates a list of students according to the steps 
 below. */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct grade_node {
    char surname[20];         // Surname of the student
    double grade;            // Grade of the student
    struct grade_node *next;  // Pointer to the next node in the list
};

typedef struct grade_node GRADE_NODE; // Define the GRADE_NODE structure
typedef GRADE_NODE *GRADE_NODE_PTR; // Define a pointer type to GRADE_NODE


/*Declare a pointer called head that will point to the start of the list. The list begins 
without any elements, so its initial value will be NULL. */

int main() {
    GRADE_NODE_PTR head = NULL; // Initialize the head pointer to NULL

    // Create the first student node
    GRADE_NODE_PTR student1 = (GRADE_NODE_PTR)malloc(sizeof(GRADE_NODE));
    strcpy(student1->surname, "Adams");
    student1->grade = 85.0;
    student1->next = NULL;
    
    // Add student1 to the list
    head = student1;

    // Create the second student node
    GRADE_NODE_PTR student2 = (GRADE_NODE_PTR)malloc(sizeof(GRADE_NODE));
    strcpy(student2->surname, "Pritchard");
    student2->grade = 66.5;
    student2->next = NULL;

    // Place this node at the end of the list
    student1->next = student2;

    // Create the third student node
    GRADE_NODE_PTR student3 = (GRADE_NODE_PTR)malloc(sizeof(GRADE_NODE));
    strcpy(student3->surname, "Jones");
    student3->grade = 91.5;

    // Place the node in the middle of the list
    student2->next = student3; // Link second node to third
    student3->next = NULL; // End of the list

    // Print the students info
    GRADE_NODE_PTR current = head;
    while (current != NULL) {
        printf("Student: %s, Grade: %.2f\n", current->surname, current->grade);
        current = current->next;
    }

    // Free memory
    free(student1);
    free(student2);
    free(student3);
    
    return 0;
}

