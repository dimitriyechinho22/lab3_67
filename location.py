"""
Working with Location class
"""


class Location:
    """
    Location class
    """
    def __init__(self, city: str, postoffice: int):
        """
        Initializing the variables
        :param city: city the item has to be delivered
        :param postoffice: number of the postoffice
        >>> location = Location('Lviv', 85)
        >>> print(location.postoffice)
        85
        """
        self.city = city
        self.postoffice = postoffice
