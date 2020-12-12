#include <stdio.h>
#include <stdlib.h>

#define MAX 10
int count = 0;

// Stack Structure
typedef struct stack {
    int items[MAX];
    int top;
} st;

void createEmptyStack(st *s) {
    s->top = -1;
};

// Check if a stack is full
int isFull(st *s) {
    if (s->top == MAX-1) 
        return 1;
    else 
        return 0;
};

// Check if a stack is empty
int isEmpty(st *s) {
    if (s->top == -1) 
        return 1;
    else
        return 0;
};

// Add element to stack
void push(st *s, int element) {
    if (isFull(s)) {
        printf("STACK IS FULL");
    } else {
        s->top++;
        s->items[s->top] = element;
    }
    count++;
};

// Remove element from stack
void pop(st *s) {
    if (isEmpty(s)) {
        printf("STACK IS EMPTY");
    } else {
        printf("Item popped = %d", s->items[s->top]);
        s->top--;
    }
    count--;
};

// Print elements from stack
void printStack(st *s) {
    printf("Stack: ");
    for (int i = 0; i < count; i++) {
        printf("%d ", s->items[i]); 
    }
    printf("\n");
};

int main() {
    st *s = (st *) malloc(sizeof(st));
    createEmptyStack(s);

	push(s, 1);
    push(s, 2);
    push(s, 3);
    push(s, 4);

    printStack(s);

    pop(s);

    printf("\nAfter popping out\n");
    printStack(s);
}
