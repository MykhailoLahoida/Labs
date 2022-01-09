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

    def decorator(func):
        def inner(self, other):
            obj = func(self, other)
            divider = math.gcd(self.numerator, obj.denumerator)
            obj.numerator //= divider
            obj.denumerator //= divider
            return obj
        return inner

    @decorator
    def __add__(self, other):
        lcm = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
        self.numerator = self.numerator * lcm // self.denumerator + other.numerator * lcm // other.denumerator
        return self

    @decorator
    def __sub__(self, other):
        lcm = self.denumerator * other.denumerator // math.gcd(self.denumerator, other.denumerator)
        self.numerator = self.numerator * lcm // self.denumerator - other.numerator * lcm // other.denumerator
        return self

    @decorator
    def __mul__(self, other):
        self.numerator = self.numerator * other.numerator
        self.denumerator = self.denumerator * other.denumerator
        return self

    @decorator
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError('The numerator of the fraction we divide by cannot be zero')
        self.numerator *= other.denumerator
        self.denumerator *= other.numerator
        return self

    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denumerator == other.numerator / other.denumerator

    def __ne__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denumerator != other.numerator / other.denumerator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denumerator > other.numerator / other.denumerator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denumerator >= other.numerator / other.denumerator

    def __lt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denumerator < other.numerator / other.denumerator

    def __le__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numerator / self.denominator <= other.numerator / other.denominator

    @property
    def printer(self):
        return str(self.__numerator) + '/' + str(self.__denumerator)

    @property
    def count(self):
        return self.__numerator / self.__denumerator

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
    print('Equals ', number.count)
    number1 = Rational(1, 2)
    print('Summa of: ', number.printer, ' and', number1.printer, ' = ', (number + number1).printer)
    print('Different of: ', number.printer, ' and', number1.printer, ' = ', (number - number1).printer)
    print('Multiply of: ', number.printer, ' and', number1.printer, ' = ', (number * number1).printer)
    print('Division of: ', number.printer, ' and', number1.printer, ' = ', (number / number1).printer)
    print(number > number1)
