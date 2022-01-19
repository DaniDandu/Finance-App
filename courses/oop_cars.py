class Car:
    def __init__(self, model: str, brand: str, price: int):
        self.model = model
        self.brand = brand
        self.price = price

    def start_engine(self):
        print("start")


vw = Car("Golf", "Volkswagen", 30000)


class Volkswagen(Car):
    def __init__(self, model: str, price: int):
        super().__init__(model, "Volkswagen", price)


class VolkswagenGolf(Volkswagen):
    def __init__(self):
        super().__init__("Golf", 30000)


vw2 = VolkswagenGolf()
print(vw2.__dict__)
