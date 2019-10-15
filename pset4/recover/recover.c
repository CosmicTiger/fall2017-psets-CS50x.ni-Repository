#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 512

// Autor: Luisángel Martín Marcia Palma
// PSET 4 recover.c

int main(int argc, string argv[])
{
    // if to avoid dummies
    if(argc != 2)
    {
        printf("Sorry, you haven't provide a key\n");
        return 1;
    }

    // we open the file card to be able to process all the jpgs files
    FILE *input = fopen("card.raw", "r");

    // if the input file (card) turns out to be NULL then just a message of error
    if(input == NULL)
    {
        printf("Could not open card.raw \n");
        return 2;
    }

    // we create a buffer to begin the creation of the images
    unsigned char buffer[BUFFER_SIZE];

    // we counts each one of the files we can extract from card
    int filecount = 0;

    // we initialize a file in null for conventional issues
    FILE *picture = NULL;

    // we count the jpgs we are founding in all the proccess of extraction
    int jpg_found = 0;

    // while the file card is read then we begin to build the file through our variable picture
    while(fread(buffer, BUFFER_SIZE, 1, input) == 1)
    {
        if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xe0) == 0xe0)
        {
           if(jpg_found == 1)
           {
               fclose(picture);
           }
           else
           {
               jpg_found = 1;
           }

           char filename[8];
           sprintf(filename, "%03d.jpg", filecount);
           picture = fopen(filename, "a");
           filecount++;
        }

        if(jpg_found == 1)
        {
            fwrite(&buffer, BUFFER_SIZE, 1, picture);
        }
    }

    // we close the files from input and picture to free also the buffers
    fclose(input);
    fclose(picture);

    return 0;
}