#For loop: number of condition fixed

#Example:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#output:
apple
cherry

#Example code:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

#Output

0
1
5
No items left.

#Example code:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#output:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry


#while loop: number of condition not fixed

#Example:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Function loop:

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
#Example code:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#output:
1
2
3
4
5
i is no longer less than 6
