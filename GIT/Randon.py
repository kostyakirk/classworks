import random

a = random.randrange(1, 11)
b = int(input())
if b == a:
    print("true")
elif b > a or b < a:
    print("false")

