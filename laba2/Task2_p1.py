"""Create a class called Rational for performing arithmetic with fractions. Write a program to test your class. Use
integer variables to represent the private data of the class – the numerator and the denominator. Provide a __init__()
method that enables an object of this class to be initialized when it’s declared. The __init__() should contain default
parameter values in case no initializers are provided and should store the fraction in reduced form. For example, the
fraction 2/4 would be stored in the object as 1 in the numerator and 2 in the denominator. Provide public methods that
perform each of the following tasks:
- printing Rational numbers in the form a/b, where a is the numerator and b is the denominator.
- printing Rational numbers in floating-point format."""
import math
class Rational:
    def __init__(self, numerator=1, denumerator=1):
        if not isinstance(numerator, int) and not isinstance(denumerator, int):
            raise TypeError("Numerator and denumerator are integer numbers")
        elif denumerator == 0:
            raise ArithmeticError("The denumerator is not zero")
        else:
            divider = math.gcd(numerator, denumerator)
            self.__numerator = numerator // divider
            self.__denumerator = denumerator // divider

    @property
    def printer(self):
        return str(self.numerator) + '/' + str(self.denumerator)

    @property
    def count(self):
        return self.numerator / self.denumerator

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denumerator(self):
        return self.__denumerator

    @numerator.setter
    def numerator(self, numerator):
        if not isinstance(numerator, int):
            raise TypeError("Numerator is integer number")
        else:
            divider = math.gcd(numerator, self.__denumerator)
            self.__numerator = numerator // divider
            self.__denumerator //= divider

    @denumerator.setter
    def denumerator(self, denumerator):
        if not isinstance(denumerator, int):
            raise TypeError("Denumerator is integer number")
        else:
            divider = math.gcd(denumerator, self.__numerator)
            self.__numerator //= divider
            self.__denumerator = denumerator // divider


if __name__ == "__main__":
    number = Rational(5, 10)
    print('Rational number ', number.printer)
    print('Equals ', number.count, '\n')
    number.numerator = 5
    number.denumerator = 25
    print('Rational number ', number.printer)
    print('Equals ', number.count)

