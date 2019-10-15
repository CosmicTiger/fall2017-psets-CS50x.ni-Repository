from cs50 import get_float

def greedy(k):

    k = float(k)

    change = round(k * 100)
    change = int(change)
    count = 0
    count = int(count)

    while change >= 25:
        change -= 25
        count += 1

    while change >= 10:
        change -= 10;
        count += 1

    while change >= 5:
        change -= 5
        count += 1

    while change >= 1:
        change -= 1
        count += 1

    return print("Change is: {}".format(count))

def main():
    chngrqst = get_float("O hai! How much change is owed?\n")

    while chngrqst < 0:
        chngrqst = get_float("O hai! How much change is owed?\n")

    greedy(chngrqst)

    return

if __name__ == '__main__':
    main()