class RetailItem:

    def __init__(self,descr,units,p):
        self.__description = descr
        self.__units_inventory = units
        self.__price = p

    def set_description(self,descr):
        self.__description = descr
    
    def set_units(self,units):
        self.__units_inventory = units
    
    def set_price(self,p):
        self.__price = p

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units_inventory

    def get_price(self):
        return self.__price
