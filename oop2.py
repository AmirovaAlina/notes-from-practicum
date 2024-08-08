class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price):
        new_price = price - (price * self.__discount/100)
        return round(new_price, 2)

    def set_discount(self, final_price):
        self.__discount = final_price
        if final_price > 80:
            self.__discount = 80
        else:
            self.__discount = final_price

              
customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)