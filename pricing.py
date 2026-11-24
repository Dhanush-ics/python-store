def calculate_price(price, discount_percent=0):
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Invalid discount")

    return round(price - (price * discount_percent / 100), 2)