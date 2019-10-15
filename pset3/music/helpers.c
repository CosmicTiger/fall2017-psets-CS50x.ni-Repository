// Helper functions for music

#include <cs50.h>
#include <string.h>
#include <math.h>

#include "helpers.h"

// Autor: Luisángel Martín Marcia Palma
// PSET 3 music helpers.c

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int numerator = atoi(strtok(fraction, "/"));
    int denominator = atoi(strtok(NULL, "/"));

    numerator = (numerator * 8)/denominator;

    return numerator;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    const string NOTES[] = {"C", "C#", "D", "D#", "E", "F",
                        "F#", "G", "G#", "A", "A#", "B"
                       };

    char actual_note[2] = {note[0], '\0'};
    int semitones = 0;
    while(strcmp(NOTES[semitones], actual_note))
    {
        semitones++;
    }

    semitones -= 9;

    if(note[1] == '#')
    {
        semitones += (note[2] - '4') * 12;
        semitones++;
    }
    else if(note[1] == 'b')
    {
        semitones += (note[2] - '4') * 12;
        semitones--;
    }
    else
    {
        semitones += (note[1]-'4') * 12;
    }

    return round(pow(2, (float) semitones / 12) * 440);
}

// Determines whether a string represents a rest
bool is_rest(string s)
{

    if(!strcmp(s, ""))
    {
        return true;
    }
    else
    {
        return false;
    }

}
