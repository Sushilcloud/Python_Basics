# dictionary  comprehension
square = {f"square of {num} is ":num**2 for num in range(1,10)}
#print(square)
for k,v in square.items():
    print(f"{k}:{v}")
string="sushil"
word_count={char:string.count(char)for char in string}
print(word_count)

# sets comprehension

s={ k**2 for k in range(1,11)}
print(s)