"""
Class for Logistic system
"""


import vehicle
import order
import item

main_lst = []

class LogisticSystem:
    """
    LogisticSystem
    """
    def __init__(self, vehicles: list):
        """
        initialyzing
        >>> veh = LogisticSystem(['mitsubishi', 'bmw'])
        >>> veh.vehicles[1]
        'bmw'
        """
        self.vehicles = vehicles
    def placeOrder(self, order_v):
        """
        placing the order
        :param order_v: certain order
        :return: placement
        """
        if len(self.vehicles) == 0:
            return "There is no available vehicle to deliver an order."
        else:
            for element in self.vehicles:
                if element.is_available:
                    order_tup = (order_v.number_of_order, order_v.location.city,
                                 order_v.calculateAmount())
                    main_lst.append(order_tup)
                    element.is_available = False
                    order_v.assignVehicle(element)
                    break

    def trackOrder(self, number_of_order):
        """
        Tracking the order
        :param number_of_order: number of order
        :return: str
        """
        list_of_orders = [i[0] for i in main_lst]
        if int(number_of_order) not in list_of_orders:
            return 'No such order'
        else:
            for element in main_lst:
                for item in element:
                    if item == number_of_order:
                        main_elem = element
                        break
            return f'Your order #{number_of_order} is sent to {main_elem[1]}, Total price: {main_elem[2]} UAH '

vehicless = [vehicle.Vehicle(1)]
logSystem = LogisticSystem(vehicless)
my_items = [item.Item('book',110), item.Item('chupachups',44)]
my_order = order.Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
print(my_order)
num = int(input("number of the order: "))
print(logSystem.trackOrder(num))



if __name__ == '__main__':
    import doctest
    doctest.testmod()