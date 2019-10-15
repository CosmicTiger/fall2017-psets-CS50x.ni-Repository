#include<stdio.h>
#include<stdlib.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>

// Author: Luisángel Martín Marcia Palma
// PSET 2 caesar.c

// Global variables
string p;

// Calling functions
int caesarcypher(int k);

int main (int argc, string argv[])
{
    //argv[0] --> nombre de programa
    if (argc != 2)
    {
        printf ("Usage: ./caesar key");
        return 1;
    }

    // Defining variables
    int key = atoi (argv[1]);
    caesarcypher(key);
    return 0;
}

// caesarcypher function
int caesarcypher(int k)
{
    p = get_string("plaintext:");
    int c = 0;
    printf ("ciphertext:");
    for (int i = 0, n = strlen (p); i < n; i++)
    {
        if (isupper (p[i]))
        {
            c = (p[i]+k-65)%26+65;
            printf ("%c", p[i] = c);
        }
        else
        if (islower (p[i]))
        {
            c = (p[i]+k-97)%26+97;
            printf ("%c", p[i] = c);
        }
        else
            printf ("%c", p[i]);

    }
    printf ("\n");
    return 0;
}