import random #imported to use the pseudo-random number generator
import time   #imported to use pythom time module

def fib():
   #this variable holds the time before executing the program
   start_time = time.time()
   #a random number is assigned to the ranom_index variable
   random_index = random.randint(15, 35)
   #a list was is created to hold a ibonacci sequence
   fibonacci_list = [0,1]
   #the list will be implemented up to the random index choosen
   list_filled = False

   while list_filled != True:
      #the if checks if the random number is less than 2
      if random_index < 3:
         fibonacci_list[random_index]
      #this else will implement the list until it reach the random number
      else:
         for i in range(2,random_index): 
            fibonacci_list.append(int(fibonacci_list[i-1]) + int(fibonacci_list[i-2]) )
         #once the last index is implemented then the boolean variable gets changed to true to exit while loop
         end_time = time.time()
         list_filled = True
   
   #This calculates the execution time           
   total_time = end_time - start_time
   #The result of the execution time and fibonacci implementation is returned
   return ( "fib(" + str(random_index) + ")=" + str(fibonacci_list[random_index-1]) + "\nfib(" + str(random_index) + ") took " + str(total_time) + " seconds" )


#the function is called and the result will be printed to terminal        
print(fib())
