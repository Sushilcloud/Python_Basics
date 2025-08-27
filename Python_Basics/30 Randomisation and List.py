import random

number=random.randint(1,100)
print(number)

a=random.random()
print(a)

uniform=random.uniform(2,8)
print(uniform)

random_head_or_tail=random.randint(0,1)
if random_head_or_tail==0:
    print("head")
else:
    print("tail")