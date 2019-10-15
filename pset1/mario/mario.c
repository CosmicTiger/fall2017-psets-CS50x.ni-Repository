#include<stdio.h>
#include<cs50.h>

// Autor: Luisángel Martín Marcia Palma
// PSET 1 mario.c

// Llamando función
int piramid (int cant);

// Función principal
int main (void)
{
    int height = 0;

    do
    {
        height = get_int("Height:");
        // Condición que impide que el usuario me digite valores negativos y mayores a 23 los cuales sugiere el pset
    }while (height < 0 || height > 23);

    piramid(height);
    return 0;
}
// Función piramid
int piramid (int column)
{
        int m = column;
        for (int i = 0; i < column; i++)
        {
            // Ciclo para que digite los espacios necesarios para formar el espacio en blanco de la piramide
            for (int j = 0; j < (column- (i + 1)); j++)
            {
                printf (" ");
            }
            // For secundario
            // Ciclo para que empiece a dibujar la piramide con el numeral
            for (int k = 0; k <= i + 1; k++)
            {
                printf ("#");
            }
            printf ("\n");
        }
    return 0;
}