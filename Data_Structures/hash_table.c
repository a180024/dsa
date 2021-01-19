#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 10

struct node {
    int data;
    struct node *next;
};

struct node *head[TABLE_SIZE] = {NULL}, *c;

void insert(int key) {
    int i;
    i = key % TABLE_SIZE;
    struct node* newNode = (struct node*) malloc(sizeof(struct node));
    newNode->data = key;
    newNode->next = NULL;
    if (head[i] == NULL) {
        head[i] = newNode;
    } else {
        c = head[i];
        while (c->next != NULL) {
            c = c->next;
        }
        c->next = newNode;
    }
};

void delete(int key) {
    int i;
    i = key % TABLE_SIZE;
    c = head[i];
    struct node *prev;
    if (c == NULL) {
        printf("NO ELEMENT FOUND\n");
    } else if (c->data == key) {
        head[i] = c->next;
    } else {
        while (c != NULL && c->data != key) {
            prev = c;
            c = c->next;
        }
        if (c == NULL) {
           return;
        }
        prev->next = c->next;
    }
}

void search(int key) {
   int i;
   i = key % TABLE_SIZE;
   if (head[i] == NULL) {
       printf("SEARCH ELEMENT NOT FOUND\n");
   } else {
       for (c=head[i]; c!=NULL; c=c->next) {
           if (c->data == key) {
               printf("SEARCH ELEMENT FOUND\n");
               break;
           }
       }
       if (c == NULL) {
           printf("SEARCH ELEMENT NOT FOUND\n");
       }
   }
};

void display() {
    int i;
    for (int i=0; i < TABLE_SIZE; i++) {
        c = head[i];
        if (c != NULL) {
            for (c=head[i]; c!=NULL; c=c->next) {
                printf("%d->",c->data);
            }
        }
        printf("\n");
    }
}

int main() {
    insert(1);
    insert(2);
    insert(11);
    search(11);
    display();
    delete(11);
    display();
    delete(1);
    display();
}



