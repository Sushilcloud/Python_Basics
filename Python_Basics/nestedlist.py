# list in list
# list comprehension
nested_comp=[[i for i in range(1,4)] for j in range(3)]
print(nested_comp)

new_list=nested_comp
for j in range(3):
    new_list.append(j)
    print(new_list)