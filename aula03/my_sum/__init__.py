def sum(list_values):
    total = 0
    for value in list_values:
        if not isinstance(value, (float, int)):
            raise ValueError
        total += value
    if isinstance(total, float):
        return round(total, 2)
    return total


class Card:
    def __init__(self, number):
        self.number = number

    def validate_number(self):
        return len(self.number) == 16



class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        try:
            return int(a) + int(b)
        except:
            raise ValueError

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        # if b == 0:
        #     raise ValueError
        return a / b