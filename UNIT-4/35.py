
#Single Inheritence
print("********Single Inheritence********")
class Restaurant:
        def make(self):
            print("Restaurant is making the food")

class pizza(Restaurant):
        def pizzamaking(self):
            print("Pizza available in the manue")

r1=pizza()
r1.make()
r1.pizzamaking()


#multilevel Inheritence

print("******** Multilevel Inheritence********")
class onlineorder(pizza):
    def orderrecive(self):
        print("Order recieved...")

r2=onlineorder()
r2.orderrecive()

# multiple inheritence

print("******** Multiple Inheritence********")

class fooddelivery:   
    def delivery(self):
        print("Order Delivered")

class foodtrack:
    def track(self):
        print("Order Track")

class foodfeedback(fooddelivery,foodtrack):
    def feedback(self):
        print ("feedback done")
    
f1=foodfeedback()
f1.delivery()
f1.track()
f1.feedback()

