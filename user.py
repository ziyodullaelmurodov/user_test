class User:
    def __init__(self, first_name: str, last_name: str, age: int, job: str, availability: bool=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.availability = availability

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price
    
    def apply_discount(self, discount: float):
        self.__price = self.__price * (1 - discount/100)
