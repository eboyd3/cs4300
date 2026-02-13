def calculate_discount(price, discount):
    #Calculates the final price after applying a discount percentage.
    #Both price and discount can be int or float
    if isinstance(price, (int, float)) and isinstance(discount, (int, float)):
        final_price = price - (price * discount / 100)
        return final_price
    else:
        raise TypeError(f"Expected int or float, got {type(value).__name__}")
    
