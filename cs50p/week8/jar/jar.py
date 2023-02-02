class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self.stored = 0
        if self.capacity < 0:
            raise ValueError

    def __str__(self):
        return "🍪" * self.stored

    def deposit(self, n):
        if self.capacity < (self.stored + n):
            raise ValueError
        self.stored += n

    def withdraw(self, n):
        if n > self.stored:
            raise ValueError
        else:
            self.stored -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.stored


def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)


if __name__ == "__main__":
    main()
