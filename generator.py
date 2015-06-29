#! /bin/python3
from math import sqrt

class Squares:
    def __init__(self, n):
        self.n = n

    def get_squares_in_Z_mod_nZ(self):
        squares = [(a**2 % self.n) for a in range(self.n)]
        return set(squares)

    def get_squares_in_1_N(self):
        squares = [(a**2) for a in range(int(sqrt(self.n)))]
        return set(squares)

def differences(A):
    differences = [(b-a) for b in A for a in A]
    return set(differences)

def sumset(A, B):
    sumset = [(a+b) for a in A for b in B]
    return set(sumset)
