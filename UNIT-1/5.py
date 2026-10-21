#Write a program to create and manipulate lists using indexing slicing and list comprehensions.

list=[1,2,3,4,'A','B']
print(list)
print(list[:2])
print(list[2:5])

list.append('Drashti')
print('After append:',list)

list.remove(1)
print('After Remove :',list)

list.pop()
print('After pop:',list)


sqr=[1,2,3,4,5]

square=[x**2 for x in sqr]
print(square)
    
