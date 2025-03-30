"""
Week 5 Ex 2 - piece_of_cake
"""


def piece_of_cake(prices, optionals=None, **amounts):
    """Calculate the total price of a cake recipe based on the ingredients prices per 100g and amonts.

    Args:
        prices (dict): A dictionary of the ingredients prices, 
                    key is the ingredient name and value is the price per 100g.
        optionals (list, optional): list of optional ingredients for the cake recipe 
                    (we want to save money so they doesn't count in the total price).
        amounts (dict): A dictionary of the ingredients amounts, 
                    key is the ingredient name and value is the amount in grams.

    Returns:
        int: The total price that we have to pay for all the cake ingredients.

    Raises:
        KeyError: If ingredient key from the prices dict is not exist as a key in the amounts dict.
    """
    if optionals is None:
        # no optional ingredients
        optionals = []

    total_price = 0
    for ingredient, price in prices.items():
        # making sure the ingredient isn't optional
        if ingredient not in optionals:
            # calculate the price of the current ingredient and accumulate it with the total price
            if ingredient in amounts.keys():
                total_price += amounts[ingredient] * (price / 100)

    return total_price


if __name__ == '__main__':
    result = piece_of_cake(
        prices={'bread': 25, 'jam': 10},
        optionals=[],
        bread=100,
        jam=50
    )
    print(result)
