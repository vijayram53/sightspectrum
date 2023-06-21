#Example code:
def get_count(arr,size,target_value):
    count=0
    for i in range(0,size):
        if arr[i]==target_value:
            count=count+1
    return count
    
    

my_list=[1,2,2,2,2,1,1,1,1,3,3,3,3,4,4,3,3,3,3,3,2,2,2]
print('1 occurance:',get_count(my_list,len(my_list),1))
print('2 occurance:',get_count(my_list,len(my_list),2))
print('3 occurance:',get_count(my_list,len(my_list),3))
print('4 occurance:',get_count(my_list,len(my_list),4))


#Example code:
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#Example code:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

#Example code:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Example code:

x = 5
y = "hello"
try:
    z = x + y
except TypeError:
    print("Error: cannot add an int and a str")

#Example code:

     
a = [1, 2, 3]
try:
    print ("Second element = %d" %(a[1]))
 
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
 
except:
    print ("An error occurred")




