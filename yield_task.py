"""
Ushbu Python class - CloneRange o'rnatilgan range funktsiyasini mimika 
qilish uchun mo'ljallangan, ammo ba'zi o'zgarishlar bilan. Sinf ham postitve, 
ham negative qadam bilan ishlaydi va uni eng ajralib turadigan joyi shundaki, 
CloneRange classda float type dagi sonlarni ishlatsa boladi.
"""
class CloneRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start-step
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop and self.step > 0:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start
        if self.start > self.stop and self.step < 0:
            self.start += self.step
            if self.start <= self.stop:
                raise StopIteration
            return self.start


def add(n):
    print(f"Summation of number {n}")
    for i in range(n):
        yield f"{n} + {i} = {n + i}"
    yield "--------------------------"

def substract(n):
    print(f"Subtraction of number {n}")
    for i in range(n):
        yield f"{n} - {i} = {n - i}"
    yield "--------------------------"

def multiply(n):
    print(f"Multiplication of number {n}")
    for i in range(n):
        yield f"{n} * {i} = {n * i}"
    yield "--------------------------"

def divide(n):
    print(f"Division of number {n}")
    for i in range(1, n):
        yield f"{n} / {i} = {n / i}"
    yield "--------------------------"

def power(n):
    print(f"Exponentiation of number {n}")
    for i in range(n):
        yield f"{n} ^ {i} = {n ** i}"
    yield "--------------------------"

def final(n):
    yield from add(n)
    yield from substract(n)
    yield from multiply(n)
    yield from divide(n)
    yield from power(n)

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    for item in final(n):
        print(item)

