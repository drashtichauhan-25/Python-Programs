

class FoodDelivery:
    def delivery(self):
        print("Food will be delivered")


class Zomato(FoodDelivery):
    def delivery(self):
        print("Zomato delivers food to your doorstep")


class Swiggy(Zomato):
    def delivery(self):
        super().delivery()
        print("Swiggy delivers food using delivery partners")



s = Swiggy()
s.delivery()





