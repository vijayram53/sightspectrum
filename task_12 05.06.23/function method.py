#split method
#Example code:
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

#Example code:
txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

#Example code:

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


#partition method:

#Example code:

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)


#Example code:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)
