"""
Vehicle class
"""


class Vehicle:
    """
    Class Vehicle helps to find out info about
    available vehicles
    """
    def __init__(self, vehicleNo, is_available=True):
        """
        Initializing the variables
        :param number: vehicle number
        :param is_available: determines whether vehicle
         available or not
        >>> vehicle = Vehicle(1)
        >>> vehicle.vehicleNo
        1
        >>> vehicle.is_available
        True
        """
        self.vehicleNo = vehicleNo
        self.is_available = is_available


