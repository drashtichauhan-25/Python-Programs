class Mobile:
    def __init__(self, brand, price, features):
        self.brand = brand
        self.price = price
        self.features =  features


    def display(self):
        print("The brand of mobile is:",self.brand)
        print("the price of mobile is:",self.price)
        print("the feature of mobile is :",self.features)

    def __del__(self):
       print("Mobile object destroyed")



    
m1=Mobile("APPLE",180000,"18 PRO MAX")
m1.display()
del m1

        
