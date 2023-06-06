
#Example code:
string = "Hello, World!"
character = "0"

index = string.index(character)
print("Index:", index)


#Example code:


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")





#Example code:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#Example code:


def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)
add_numbers(5, 4)


#Example code:

def find_square(num):
    result = num * num
    return result
square = find_square(3)

print('Square:',square)

