class House:
    def __init__(self, address, number_of_rooms, price, house_type, year_built):
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.price = price
        self.house_type = house_type
        self.year_built = year_built

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_number_of_rooms(self):
        return self.number_of_rooms

    def set_number_of_rooms(self, number_of_rooms):
        self.number_of_rooms = number_of_rooms

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_house_type(self):
        return self.house_type

    def set_house_type(self, house_type):
        self.house_type = house_type

    def get_year_built(self):
        return self.year_built

    def set_year_built(self, year_built):
        self.year_built = year_built

    def display_info(self):
        print("House Info:")
        print(f"Address: {self.address}")
        print(f"Number of Rooms: {self.number_of_rooms}")
        print(f"Price: {self.price:.2f}")
        print(f"Type: {self.house_type}")
        print(f"Year Built: {self.year_built}\n")
