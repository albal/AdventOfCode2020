# https://www.programiz.com/python-programming/precedence-associativity
import re

with open('input18.txt', 'r') as file:
    data = file.read().split('\n')


class mySwap(int):
    def __add__(self, other):
        return mySwap(int(self) + other)

    def __sub__(self, other):
        return mySwap(int(self) * other)


def parse(calculation):
    calculation = re.sub(r"(\d+)", r"mySwap(\1)", calculation)
    calculation = calculation.replace("*", "-")
    return eval(calculation)


print("Sun:", sum(map(parse, data)))
