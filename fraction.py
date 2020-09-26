from __future__ import annotations
"""
    Simple fraction class with a few property examples
"""


class Fraction:
    """
        Fraction class
    """

    def __init__(self: Fraction, num: int = 0, den: int = 1):
        """
            Fraction constructor
            Throws ValueError when denominator is zero
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero!")

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError("Numerator and Denominator must be type int")

        if den < 0:
            if num < 0:
                num = abs(num)
            else:
                num = -num
            den = abs(den)

        div: int = Fraction.gcd(num, den)
        self.num: int = num // div
        self.__den: int = den // div

# ================================================
# Examples of property style getters and setters
#
    @property
    def num(self: Fraction) -> int:
        """
        'Getter' property
        """
        return self.__num

    @num.setter
    def num(self: Fraction, new_num: int) -> None:
        """
        'Setter' property
        """
        print(f"setting the numerator: {new_num}")
        self.__num = new_num

    @property
    def den(self: Fraction) -> int:
        return self.__den
#
# ===================================================

    def reduce(self: Fraction):
        """
            Not neededfor immutable type
        """
        pass

    def __str__(self: Fraction) -> str:
        return str(self.__num) + '/' + str(self.__den)

    def __add__(self: Fraction, other: Fraction) -> Fraction:
        num1 = self.__num * other.den
        num2 = other.__num * self.__den
        return Fraction(num1 + num2, self.__den * other.den)

    def __mul__(self: Fraction, other: Fraction) -> Fraction:
        return Fraction(self.__num * other.num, self.__den * other.den)

    def __eq__(self: Fraction, other: Fraction) -> bool:
        return self.__num == other.num and self.__den == other.den

    @staticmethod
    def gcd(a: int, b: int) -> int:
        if b != 0:
            return Fraction.gcd(b, a % b)
        else:
            return abs(a)


def manual_tester() -> None:
    print("gcd(34, 17) =", Fraction.gcd(34, 17))
    print("gcd(3, 17) =", Fraction.gcd(3, 17))
    print("gcd(1024, 2) =", Fraction.gcd(1024, 2))

    frac = Fraction(3, -6)
    print("Fraction(3, -6) =", frac)
    frac = Fraction(-3, -6)
    print("Fraction(-3, -6) =", frac)
    frac = Fraction(-6, -3)
    print("Fraction(-6, -3) =", frac)
    frac = Fraction(3, 7)
    print("Fraction(3, 7) =", frac)
    frac1 = Fraction(1, 2)
    frac2 = Fraction(2, 3)
    frac3 = Fraction(-1, 5)
    frac4 = Fraction(1, 2)
    print("f1 === f4?", frac1 == frac4)
    # frac3 = frac1 + frac2
    print(frac1, '+', frac2, '=', frac1 + frac2)
    print(frac1, '+', frac3, '=', frac1 + frac3)
    print("gcd(2,-4) =", Fraction.gcd(2, -4))
    print(Fraction(3))
    print("done")
    print(Fraction(den=5, num=1))
    print(Fraction(den=6, num=2))


if __name__ == "__main__":
    manual_tester()

    x: Fraction = Fraction(9, 10)
    print(f"x.num is {x.num}, x.den is {x.den}")
    x.num = 5
    print(f"x.num is {x.num}, x.den is {x.den}")

    try:
        f: Fraction = Fraction(1, 0)
    except ValueError:
        print("Denominator cannot be zero!")

    try:
        f: Fraction = Fraction(1, 1.1)
    except TypeError:
        print("Numerator and Denominator must be type 'int'.")
