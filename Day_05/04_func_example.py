coffie_price = [("capuchino", 3.5), ("expreso", 6.2), ("moka", 1.9)]


def coffie_max(coffie_list):
    hight_price = 0
    coffie_expense = ""

    for coffie, price in coffie_list:
        if price > hight_price:
            hight_price = price
            coffie_expense = coffie

    return (coffie_expense, hight_price)


print(coffie_max(coffie_price))
