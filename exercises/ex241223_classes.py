'''class Cars:

    def __init__(self, engine, wheels, doors, color):
        self.manoa = engine
        self.galgal = wheels
        self.delet = doors
        self.zeva = color

    def fix_cars(self, ):


class Toyota(Cars):

    def __init__(self):
        pass
'''
import re

price = 'price: $184.50'
expresion = 'price: \$([0-9]*\.[0-9]{2})'
matches = re.search(expresion,price)
print(matches.group(0))
print(matches.group(1))

print_num = float(matches.group(1))
print(f"{print_num:.2f}")