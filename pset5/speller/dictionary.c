// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

#include "dictionary.h"

// Autor: Luisángel Martín Marcia Palma
// PSET 5 dictionary.c

typedef struct node
{
    bool is_word;
    struct node* children[27];
}node;

node* root;

// create global variable to count size
int dictionarySize = 0;

/**
 *  Recursive function to freeing the nodes from bottom to top
 *  idea based on heaps and stacks
 **/
void freeing(node* children)
{
    for(int i = 0; i < 27; i++)
    {
        if(children -> children[i] != NULL)
        {
            freeing(children -> children[i]);
        }
    }

    free(children);
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int index;

    // create a pointer to first node
    node* traversing = root;

    for(int i = 0; word[i] != '\0'; i++)
    {
        // if letter is apostrophe
        if(word[i] == '\'')
        {
            index = 26;
        }
        else
        {
            // convert each letter to an index, e.g a is 0
            index = tolower(word[i]) - 'a';
        }

        // traverse to next letter
        traversing = traversing -> children[index];

        // if NULL, word is misspelled
        if(traversing == NULL)
        {
            return false;
        }
    }

    // once at end of word, check if is_word is true
    if(traversing -> is_word == true)
        return true;
    else
        return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // opening the dictionary file
    FILE* dictionaryPointer = fopen(dictionary, "r");
    int index;
    char word[LENGTH+1];

    // if cannot open file, return false
    if(dictionaryPointer == NULL)
    {
        fprintf(stderr, "File does not exist!\n");
        return false;
    }

    // creating tries and initialize default value & pointer
    root = malloc(sizeof(node));
    root -> is_word = false;

    for(int j = 0; j < 27; j++)
    {
        root -> children[j] = NULL;
    }

    // building of tries from dictionary with loop
    // scan each word line by line from dictionaries
    while(fscanf(dictionaryPointer, "%s\n", word) != EOF)
    {
        // create a traversal pointer from start of Tries
        node* traversing = root;

        // for every dictionary word, iterate through trie
        for(int i = 0; word[i] != '\0'; i++)
        {
            // if letter is apostrophe
            if(word[i] == '\'')
            {
                // if letter is apostrophe
                index = 26;
            }
            else
            {
                // convert each letter to an index, e.g a is 0
                index = tolower(word[i]) - 'a';
            }

            if(traversing -> children[index] == NULL)
            {
                // if NULL, malloc new node
                node* new_node = malloc(sizeof(node));
                new_node -> is_word = false;

                for(int k = 0; k < 27; k++)
                {
                    new_node -> children[k] = NULL;
                }
                // and set children[index] to point at it
                traversing -> children[index] = new_node;
            }
            // move traversal pointer to it
            traversing = traversing -> children[index];
        }
        // at end of word, set is_word true;
        traversing -> is_word = true;
        dictionarySize++;
    }

    fclose(dictionaryPointer);

    // returning to true if it's successful
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // return the total size of the dictionary
    return dictionarySize;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node* traversing = root;
    freeing(traversing);
    return true;
}
