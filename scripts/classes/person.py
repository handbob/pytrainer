class Person:
    def __init__(self, name, age, gender, address, phone_number):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone_number = phone_number

    def free(self):
        del self.name
        del self.gender
        del self.address
        del self.phone_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def display_info(self):
        print("Person Info:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}\n")
