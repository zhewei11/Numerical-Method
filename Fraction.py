from math import gcd 

class Fraction(object):

    def __init__(self, Numerator:int, Denominator:int): 
        if Denominator == 0:
            print("Denominator cannot be 0")
        else:
            common = gcd(Numerator, Denominator)
            self.Numerator = Numerator // common
            self.Denominator = Denominator // common

    def __add__(self, other): # + 
        new_Numerator = self.Numerator * other.Denominator + other.Numerator * self.Denominator
        new_Denominator = self.Denominator * other.Denominator
        return Fraction(new_Numerator, new_Denominator)

    def __sub__(self, other): # - 
        new_Numerator = self.Numerator * other.Denominator - other.Numerator * self.Denominator
        new_Denominator = self.Denominator * other.Denominator 
        return Fraction(new_Numerator, new_Denominator)

    def __mul__(self, other): # *
        new_Numerator = self.Numerator * other.Numerator
        new_Denominator = self.Denominator * other.Denominator
        return Fraction(new_Numerator, new_Denominator)
       
    def __truediv__(self, other): # / 
        new_Numerator = self.Numerator * other.Denominator
        new_Denominator = self.Denominator * other.Numerator  
        return Fraction(new_Numerator, new_Denominator)

    def __eq__(self, other): # ==
        return self.Numerator == other.Numerator and self.Denominator == other.Denominator

    def __ne__(self, other): # != 
        return not self.__eq__(other)

    def __repr__(self):
        return f"Fraction({self.Numerator},{self.Denominator})"
    
    def __str__(self):
        return f"{self.Numerator}/{self.Denominator}"
