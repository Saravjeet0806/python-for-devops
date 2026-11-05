# x = 5
# y= "john"
# print(x)
# print(y)

### casting
# x = str(3)  #'3'
# y = int(3)
# z = float(3)
# print(x)
# print(y)
# print(z)
# print(type(x)) #<class 'str'>
# print(type(y)) #<class 'int'>

# x, y, z = "orange", "banana", "camel"
# print(x, y, z)
# print(type(x), type(y), type(z))


# fruits = ["apple", "banana", "guava"]
# x, y, z = fruits
# print(x, y, z)

my_dict = {
    'id': '4',
    'name': 'Saravjeet',
    'hobbies': ['cricket', 'volleyball', 'football']
}

print(my_dict)
print(my_dict['hobbies'][0]) #cricket

my_dict['hobbies'][1] = 'casino'
print(my_dict)