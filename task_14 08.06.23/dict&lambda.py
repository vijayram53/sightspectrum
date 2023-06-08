#dictiory

#Example code:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Example code
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) 
car["color"] = "white"
print(x)


#Example code
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#Example code:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#Lambda Function

#Example code:

 x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Example code

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))




 
  


