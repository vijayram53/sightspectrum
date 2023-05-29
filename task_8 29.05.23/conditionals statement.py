#Conditional statement

#Example code:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Example code:
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#Example code:
number = 0
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')
print('This statement is always executed')

#Example code:

     number = 5
# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    # inner else statement
    else:
        print('Number is positive')
# outer else statement
else:
    print('Number is negative')
# Output: Number is positive


#Example code:


letter = "A"
 
if letter == "B":
    print("letter is B")
 
elif letter == "C":
    print("letter is C")
 
elif letter == "A":
    print("letter is A")
 
else:
    print("letter isn't A, B or C")






