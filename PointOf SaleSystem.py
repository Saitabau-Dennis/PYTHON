class Saleitem:
    def __init__(self,item_id,name,unit_price):
        self.item_id=item_id
        self.name=name
        self.unit_price=unit_price
class Standarditem(Saleitem):
    def __init__(self, item_id, name, unit_price,quantity):
        self.quantity=quantity
        super().__init__(item_id, name, unit_price)
    def calculate_total(self):
        return self.quantity * self.unit_price
class Discountitem(Standarditem):
    def __init__(self, item_id, name, unit_price, quantity, discount_percentage):
        self.discount_percentage = discount_percentage
        super().__init__(item_id, name, unit_price, quantity)

    def calculate_total(self):
        discounted_price = self.unit_price * (1 - self.discount_percentage)
        return self.quantity * discounted_price

class Serviceitem(Saleitem):
    def __init__(self, item_id, name,unit_price,hours,hourly_rate):
        self.hourly_rate=hourly_rate
        self.hours=hours
        super().__init__(item_id, name,unit_price)
    def calculate_total(self):
        return self.hours * self.hourly_rate

standard_item=Standarditem(200,'cooking oil',300,20)
cost=standard_item.calculate_total()
print("THE TOTAL COST FOR STANDARD ITEM IS:",cost)

discount_item=Discountitem(201,'cabbage',500,60,0.2)
cost=discount_item.calculate_total()
print("THE TOTAL COST FOR DISCOUNT ITEM IS:",cost)

service_item=Serviceitem(203,'car',90,4,100)
cost=service_item.calculate_total()
print("THE TOTAL COST FOR SERVICE ITEM IS:",cost)
