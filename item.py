"""
Docstring for Item
"""

class Item:
    """
    Adjusting the item to order
    """
    def __init__(self, name: str, price: float):
        """
        Initializing the variables
        >>> item = Item('book',110)
        >>> print(item.price)
        110
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Returning the info about item
        >>> print(Item('book',110))
        The customer ordered book. its price: 110 UAH
        """
        return f"The customer ordered {self.name}. its price: {self.price} UAH"


if __name__ == '__main__':
    import doctest
    doctest.testmod()