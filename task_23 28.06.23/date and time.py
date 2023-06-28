x =[45]
for i in x:
  if i > 10:
    continue
  print("hello world")
##if x > 20:
##    print("and also above 20!")
##else:
##    print("but not above 20.")


#Example code:

class hai:
    def __init__(self, name, company):
        self.name = name
        self.company = company

 
    def show(self):
        print("Hello my name is " + self.name+" and I" +
              " work in "+self.company+".")
 
 
obj = hai("John", "hello")
obj.show()





#Example code:


import threading

def vijay(number):
    print ('vijay:  %s' , %number)
    return

threads = []
for k in range(5):
    t = threading.Thread(target=vijay, args=(k,))
    threads.append(t)
    t.start()



Date and time:

from datetime import date
  
# date object of today's date
today = date.today() 
  
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


Example code:


import datetime
 
today = datetime.date.today()
three_days_ago = today - datetime.timedelta(days=3)
 
print("Today:", today)
print("Three days ago:", three_days_ago)



    







