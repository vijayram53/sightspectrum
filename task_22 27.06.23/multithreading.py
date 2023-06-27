#Example code:
import threading
 
 
def print_cube(num):

    print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
 
    print("Square: {}" .format(num * num))
 
 
if __name__ =="__main__":
 
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
  
    t1.start()

    t2.start()
 

    t1.join()
  
    t2.join()
 
   
    print("Done!")


#Example code:
import concurrent.futures
 
def worker():
    print("Worker thread running")
 

pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
 

pool.submit(worker)
pool.submit(worker)
 

pool.shutdown(wait=True)
 
print("Main thread continuing to run")    
