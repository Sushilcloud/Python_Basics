import random

friend=["sushil","lokesh","rajeev","rakesh","sanjay"]

#for i in friend:
    #print(i)
print(random.choices(friend))

random_index=random.randint(0,4)
print(friend[random_index])