from fractions import Fraction

class ProperFraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def value(self):
        return self.numerator / self.denominator

    def __eq__(self, other):
        if not isinstance(other, ProperFraction):
            return NotImplemented
        return self.value() == other.value()

    def __ne__(self, other):
        return  self.value() != other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __add__(self, other):
        fraction1 = Fraction(self.numerator, self.denominator)
        fraction2 = Fraction(other.numerator, other.denominator)
        res = fraction1 + fraction2
        return ProperFraction(res.numerator, res.denominator)

    def __sub__(self, other):
        fraction1 = Fraction(self.numerator, self.denominator)
        fraction2 = Fraction(other.numerator, other.denominator)
        res = fraction1 - fraction2
        return ProperFraction(res.numerator, res.denominator)

    def __mul__(self, other):
        fraction1 = Fraction(self.numerator, self.denominator)
        fraction2 = Fraction(other.numerator, other.denominator)
        res = fraction1 * fraction2
        return ProperFraction(res.numerator, res.denominator)

def main():
    fraction1 = ProperFraction(1, 2)
    fraction2 = ProperFraction(1, 3)
    print(fraction1 > fraction2)
    print(fraction1 + fraction2)
    print(fraction1 - fraction2)
    print(fraction1 * fraction2)


if __name__ == '__main__':
    main()
