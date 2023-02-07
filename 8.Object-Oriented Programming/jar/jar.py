class Jar:

    def __init__(self, capacity=12):
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    # adds cookies
    def deposit(self, n):
        self.cookies += n

    # removes cookies
    def withdraw(self, n):
        self.cookies -= n

    @property
    def size(self):
        return self.cookies

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Can only be positive int")
        self._capacity = capacity

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, x):
        if x > self.capacity:
            raise ValueError("Over the limit")
        elif x < 0:
            raise ValueError("Not enough cookies")
        self._cookies = x
        
