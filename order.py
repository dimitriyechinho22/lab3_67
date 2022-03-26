"""
Order class
"""

import random
import location
import item
import vehicle


list_of_orders = []

def checking(lst, num):
    """
    Checking if number in lst
    :param lst: list
    :param num: number
    :return: ended number
    """
    for i in range(10000):
        if num not in lst:
            break
        else:
            num = random.randint(1, 100000000)
    return num



class Order:
    """
    Working with orders
    """
    def __init__(self, user_name: str, city: str, postoffice: int, items: list, vehicle=None):
        """
        Initializing the variables
        :param user_name: name of a user
        :param city: city where order has to go
        :param postoffice: number of postoffice
        :param items: list of items that customer has added
        :param vehicle: list of vehicles
        >>> my_items = [item.Item('book',110), item.Item('chupachups',44)]
        >>> ord = Order('Oleg','Lviv', 53, my_items)
        >>> print(ord.user_name)
        Oleg
        """
        self.user_name = user_name
        self.location = location.Location(city, postoffice)
        self.items = items
        self.vehicle = vehicle
        number_of_order = random.randint(1, 100000000)
        number_of_order = checking(list_of_orders, number_of_order)
        list_of_orders.append(number_of_order)
        self.number_of_order = number_of_order

    def calculateAmount(self):
        """
        Calculates the total price
        >>> my_items = [item.Item('book',110), item.Item('chupachups',44)]
        >>> ord = Order('Oleg','Lviv', 53, my_items)
        >>> ord.calculateAmount()
        154
        """
        result = 0
        for i in self.items:
            result += i.price
        return result

    def assignVehicle(self, assigned_vehicle):
        """
        Assigning the vehicle
        """
        self.vehiclee = assigned_vehicle
    def __str__(self):
        """
        returning the line of order number
        """
        return f"Your order number is {self.number_of_order}."

if __name__ == '__main__':
    import doctest
    doctest.testmod()