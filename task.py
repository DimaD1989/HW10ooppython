import math


class Hex():
    symbols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

    def __init__(self, number):
        self.number = number

    def trans(self, integer):
        result = ""

        while integer > 0:
            result += str(self.symbols[(
                        integer % 16)])  # А что лучше, сразу задать чисто строковый массив или переводить элементы массива с строки, зато не надо будет каждый в кавычки брать?
            integer = integer // 16
        return f"Ox{result[::-1]}"


class Fraction():

    def __init__(self, numerator, denominator):
        if denominator != 0:
            if numerator < 0 and denominator < 0:
                numerator *= -1
                denominator *= -1
            self.numerator = numerator
            self.denominator = denominator
        else:
            raise ValueError

    def reduce_fraction(self):
        while math.gcd(self.numerator, self.denominator) > 1:
            self.numerator = int(self.numerator / math.gcd(self.numerator, self.denominator))
            self.denominator = int(self.denominator / math.gcd(self.numerator, self.denominator))
        return Fraction(self.numerator, self.denominator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        new_nominator = int((a * d + c * b) / math.gcd(a * d + c * b, b * d))
        new_denominator = int((b * d) / math.gcd(a * d + c * b, b * d))

        return Fraction(new_nominator, new_denominator).reduce_fraction()

    def __mul__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        new_nominator = int((a * c) / math.gcd(a * c, b * d))
        new_denominator = int((b * d) / math.gcd(a * c, b * d))

        return Fraction(new_nominator, new_denominator).reduce_fraction()

    def __truediv__(self, other):
        other.numerator, other.denominator = other.denominator, other.numerator
        return self * other

    def __sub__(self, other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        new_nominator = int((a * d - c * b) / math.gcd(a * d - c * b, b * d))
        new_denominator = int((b * d) / math.gcd(a * d - c * b, b * d))
        return Fraction(new_nominator, new_denominator).reduce_fraction()

    def __pow__(self, other):
        new_nominator = self.numerator ** other.numerator ** (1 / other.denominator)
        new_denominator = self.denominator ** other.numerator ** (1 / other.denominator)
        return new_nominator / new_denominator


frac_1 = Fraction(2, 6)

frac_2 = Fraction(3, 5)

print(frac_1 + frac_2)

print(frac_1 - frac_2)
print(frac_1 * frac_2)
print(frac_1 / frac_2)
print(frac_1 ** frac_2)
