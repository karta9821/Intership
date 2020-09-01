"""
Przyjąłem, że ilości i ceny
 są liczbami całkowitymi,
chociaż cena mogłaby być typu
 float w funkcji round(cena, 2)
"""

import random
import data as d


class Product(d.ParentProduct):
    def __init__(self, name: str, amount: int, price: int):
        super(Product, self).__init__(name)
        self.amount = amount
        self.price = price

    def __repr__(self):
        return self.name

    def show_price(self, currency: str) -> None:
        print(f'{self.name} price is {self.price} {currency}')

    def show_amount(self) -> None:
        print(f'{self.name} amount is {self.amount}')

    def calculate_total_value(self) -> int:
        return self.price * self.amount


for product in d.products:
    product['amount'] = random.randint(product['amount']['min'], product['amount']['max'])
    product['price'] = random.randint(product['price']['min'], product['price']['max'])


d.obj_list = [Product(product['name'], product['amount'], product['price']) for product in d.products]
summary_list = [product.calculate_total_value() for product in d.obj_list]


with open('results_01.txt', 'w') as f:
    for product, obj, summary in zip(d.products, d.obj_list, summary_list):
        f.write(f'[data.obj_list: {product} - Object: {obj} - summary_list: {summary}]\n')


