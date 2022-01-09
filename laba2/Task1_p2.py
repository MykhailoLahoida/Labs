"""Create a class that descibes a Product of online store. As a Product fields you can use a price, description and
product' dimensions.
Create a class that describes a Customer. As a Customer fields you can use surname, name, patronymic, mobile phone, etc.
Create a class that describes an Order.
- the order must contain data about the customer who carried it out and products. Implement a method for calculating
the total order value."""
class Product:
    def __init__(self, name, price, description, height, width):
        if not isinstance(name, str):
            raise TypeError("Name is a string value")
        elif not isinstance(price, int):
            raise TypeError("Price is a integer value")
        elif not isinstance(description, str):
            raise TypeError("Description is a string value")
        elif not isinstance(height, float):
            raise TypeError("Height is a float value")
        elif not isinstance(width, float):
            raise TypeError("Width is a float value")
        elif price < 0 or height < 0 or width < 0:
            raise ValueError("Price, width and height are positive values")
        else:
            self.__name = name
            self.__price = price
            self.__description = description
            self.__height = height
            self.__width = width

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name is a string value")
        else:
            self.__name = name

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError("Price is a integer value")
        elif price < 0:
            raise ValueError("Price is a positive value")
        else:
            self.__price = price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError("Description is a string value")
        else:
            self.__description = description

    @height.setter
    def height(self, height):
        if not isinstance(height, float):
            raise TypeError("Height is a float value")
        elif height < 0:
            raise ValueError("Height is a positive values")
        else:
            self.__height = height

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError("Width is a float value")
        elif width < 0:
            raise ValueError("Width is a positive values")
        else:
            self.width = width

class Customer:
    def __init__(self, surname, name, patronymic, phone):
        if not isinstance(surname, str) or not isinstance(name, str) or not isinstance(patronymic, str) \
                or not isinstance(phone, str):
            raise TypeError("Surname, name, patronymic and phone are string values")
        else:
            self.__surname = surname
            self.__name = name
            self.__patronymic = patronymic
            self.__phone = phone

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def phone(self):
        return self.__phone

class Order:
    def __init__(self, customer, products):
        self.__customer = customer
        self.__products = products

    @property
    def total_val(self):
        total_value = 0
        for prod in self.products:
            total_value += prod.price * self.products[prod]
        return total_value

    @property
    def customer(self):
        return self.__customer

    @property
    def products(self):
        return self.__products

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer is a object of class 'Customer'")
        self.__customer = customer

    @products.setter
    def products(self, products):
        if not isinstance(products, dict):
            raise TypeError("Products is a dict")
        self.__products = products

if __name__ == "__main__":
    Michael = Customer("Lahoida", "Mykhailo", "Myroslavovych", "+380999999999")
    Ball = Product('Ball', 300, "Good Ball", 60.5, 60.5)
    Phone = Product('Phone', 26000, "Good Phone", 6.5, 20.5)
    Ord = Order(Michael, {Ball: 5, Phone: 1})
    print('Data about customer: ', Ord.customer.name, Ord.customer.surname, Ord.customer.patronymic, Ord.customer.phone)
    print('Product list:')
    for prod in Ord.products:
        print(prod.name, Ord.products[prod])
    print('Total: ', Ord.total_val)
