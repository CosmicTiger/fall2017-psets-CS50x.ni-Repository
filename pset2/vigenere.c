#include<stdio.h>
#include<stdlib.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>

// Autor: Luisángel Martín Marcia Palma
// PSET 2 vigenere.c

// Global variables
string p;

// Calling functions
int vigenerecipher (string k);

// Main function
int main (int argc, string argv[])
{
    // Defining variables
    string key = argv[1];
    if (argc != 2)
    {
        printf ("Usage: ./vigenere <key>");
        return 1;
    }
    for (int i = 0; i < strlen (key); i++)
    {
        if (isdigit (key[i]))
        {
            printf ("Usage: ./vigenere <key>");
            return 1;
        }
    }
    vigenerecipher (key);
    return 0;
}

// vigenere cipher function
int vigenerecipher (string k)
{
    p = get_string("plaintext: ");
    int c = 0, j = 0, m = 0;
    printf ("ciphertext: ");
    for (int i = 0, n = strlen (p); i < n; i++)
    {

        if (isupper (p[i]))
        {
            k[j] = toupper (k[j]);
            c = (p[i]+k[j]-130)%26+65;
            printf ("%c", p[i] = c);
            m++; j++;
        }
        else
        {
            if (islower (p[i]))
            {
                k[j] = tolower (k[j]);
                c = (p[i]+k[j]-194)%26+97;
                printf ("%c", p[i] = c);
                m++; j++;
            }
            else
            {
                printf ("%c", p[i]);
            }
        }
        j = (m)%strlen(k);
    }
    printf ("\n");
    return 0;
}