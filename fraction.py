class Fraction:
    """
        Fraction class
    """
    
    def __init__(self, num, den):
        """
            Fraction constructor
            Throws ValueError when denominator is zero
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero!")
        
        negative = ((num < 0) or (den < 0)) and not (num < 0 and den < 0)
        
        div = Fraction.gcd(num, den)
        self.num = num // div
        self.den = den // div
        
        if negative:
            self.num = -abs(self.num)
            self.den = abs(self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return Fraction(num1 + num2, self.den * other.den)

    def __mul__(self, other):
        return Fraction(self.num * other.num, self.den * other.den)
    
    def __eq__(self, other):
        return self.num == other.num and self.den == other.den
    
    @staticmethod
    def gcd(a, b):
        if b != 0:
            return Fraction.gcd(b, a % b)
        else:
            return abs(a)


if __name__ == "__main__":
    try:
        f = Fraction(1, 0)
    except:
        print("Denominator cannot be zero!")
        
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
    frac4 = Fraction(1, 2)
    print("f1 == f4?", frac1 == frac4)
    frac3 = frac1 + frac2
    print(frac1, '+', frac2, '=', frac3)