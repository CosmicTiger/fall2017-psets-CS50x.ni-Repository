from cs50 import get_int

"""
    // Autor: Luisángel Martín Marcia Palma
    // PSET 6 mario.py
"""

"""The function that creates the piramid"""
def piramid (height):
    for i in range (0, height, 1):
        for j in range(0, (height - (i+1)), 1):
            print(' ', end='')
        for k in range(0, i+2, 1):
            print('#', end='')
        print('')
    return


"""The function that helps to verify the input from the user"""
def getHeight():
    height = get_int("Height: ")

    while height < 0 or height > 23:
        height = get_int("Height: ")

    return int(height)


"""Main function"""
def main ():
    piramid(getHeight())
    return

if __name__ == ("__main__"):
    main()