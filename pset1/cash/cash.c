#include<stdio.h>
#include<cs50.h>
#include<math.h>

// Autor: Luisángel Martín Marcia Palma
// PSET 1 cash.c antes greedy.c

// Llamando función greedy
float greedy (float k);

// Función principal
int main (void)
{
    // Definiendo variables
    float chngrqst;

    // Solicitando datos de entrada
    // Condición para que no ingrese datos negativos
    do
    {
        chngrqst = get_float("O Hai! How much change is owed?\n");
    }while (chngrqst<0);

    greedy(chngrqst);

    return 0;
}

// Función Greedy
float greedy (float k)
{
    // Definiendo variables
    int change = round(k * 100);
    int counter = 0;

    // Sentencias de la funcion
    while(change >= 25)
    {
        change -= 25;
        counter++;
    }
    while(change >= 10)
    {
        change -= 10;
        counter++;
    }
    while(change >= 5)
    {
        change -= 5;
        counter++;
    }
    while(change >= 1)
    {
        change -= 1;
        counter++;
    }

    // Imprimiendo el resultado al usuario
    printf ("Change is: %d", counter);
    return 0;
}
//Encontré por dónde era el error que dice lipe, a copiar el código a como lo dejé ahorita y cruzarme al