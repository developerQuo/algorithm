# Coin Changing Problem
def coin_changing_program(change):
    n500 = 0
    n100 = 0
    n50 = 0
    n10 = 0
    n1 = 0

    while change >= 500:
        change -= 500
        n500 += 1
    while change >= 100:
        change -= 100
        n100 += 1
    while change >= 50:
        change -= 50
        n50 += 1
    while change >= 10:
        change -= 10
        n10 += 1
    while change >= 1:
        change -= 1
        n1 += 1

    return {
        "500": n500,
        "100": n100,
        "50": n50,
        "10": n10,
        "1": n1,
    }


print(coin_changing_program(799))
