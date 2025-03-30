def piece_of_cake(prices, optionals=None, **amounts):
    if optionals is None:
        # no optional ingredients
        optionals = []

    total_price = 0
    for ingredient, price in prices.items():
        # making sure the ingredient isn't optional
        if ingredient not in optionals:
            # calculate the price of the current ingredient and accumulate it with the total price
            total_price += price * (amounts[ingredient] // 100)

    return total_price


if __name__ == '__main__':
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
    print(piece_of_cake({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
    print(piece_of_cake({}))
