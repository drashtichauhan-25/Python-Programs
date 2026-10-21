class Shopping:
    def product( self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity= quantity

    def display(self):
        total = self.price * self. quantity
        print("Name of product is:",self.name)
        print("Quantity if product is :",self.quantity)
        print("price of 1 product is:",self.price)
        print("total amount is:",total)

s1 =Shopping()
s1.product( "Penbox",50,3)
s1.display()

