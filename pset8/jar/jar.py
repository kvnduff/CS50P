"""
Create cookie jar class according to specifications.
"""


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return("🍪" * self.size)

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Number of cookies exceeds cookie jar capacity.")
        self.size = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies in the cookie jar.")
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be a positive integer.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
