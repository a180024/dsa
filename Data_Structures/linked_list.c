// Linked list implementation in C
// Use double pointer to modify pointer

#include <stdio.h>
#include <stdlib.h>

// Creating a node
struct node {
  int value;
  struct node *next;
};

// Insert at beginning
void insertAtBeginning(struct node** head, int value) {
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node->value = value;
    new_node->next = (*head);
    (*head) = new_node;
}

// Insert in the middle
void insertAfter(struct node* node, int value) {
    if (node == NULL) {
        return;
    }

    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    new_node->value = value;
    new_node->next = node->next;
    node->next = new_node;
}

// Insert at end
void insertAtEnd(struct node** head, int value) {
    struct node* new_node = (struct node*) malloc(sizeof(struct node));
    struct node* last = *head;

    new_node->next = NULL;
    new_node->value = value;

    // Check if head is empty
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    
    while (last->next != NULL) {
        last = last->next;
    }

    last->next = new_node;
    return;
}

// Delete node
void deleteNode(struct node** head, int key) {
    struct node *temp = *head, *prev;

    // deleting first node
    if (temp != NULL && temp->value == key) {
        *head = temp->next;
        free(temp);
        return;
    }

    while (temp != NULL && temp->value != key) {
        prev = temp; 
        temp = temp->next;
    }

    // key is not present
    if (temp == NULL) return;

    prev->next = temp->next;
    free(temp);
}

// print the linked list value
void printList(struct node *p) {
  while (p != NULL) {
    printf("%d ", p->value);
    p = p->next;
  }
}

int main() {
    struct node* head = NULL;

    insertAtEnd(&head, 1);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 3);
    insertAtEnd(&head, 4);
    insertAfter(head->next, 5);

    printf("Linked list: ");
    printList(head);

    printf("\nAfter deleting an element: ");
    deleteNode(&head, 3);
    printList(head);

}
