class Car:
    def __init__(self, make, model, year, price, color, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.color = color
        self.mileage = mileage

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def display_info(self):
        print("Car Info:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price:.2f}")
        print(f"Color: {self.color}")
        print(f"Mileage: {self.mileage}\n")
