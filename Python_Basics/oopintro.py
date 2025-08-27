class Person: 
    def _init_(self, first_name,last_name,age):
        # instace variables 
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

p1=Person('Harshit','Vashistra',24)
#p2=Person('Mohit','Vashistra',19)

print(p1.first_name)