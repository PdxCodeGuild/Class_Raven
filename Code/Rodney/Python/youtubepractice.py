## class is a blueprint for creating instances (each employee we creat is an instance for exmaple)
## data and functions ====== attributes and methods 


'''class Employee:
    
    def __init__(self, first, last, pay): ### name, email, and pay are all attributes of our class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

    def fullname(self):
        return '{#} {#}'.format(self.first, self.last)



## unique instances of the employee class 
## instance variables contain data that is unique to each instance
emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)#<__main__.Employee object at 0x7f84a1eb5130>
#print(emp_2)#<__main__.Employee object at 0x7f84a1eb5d30>

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())'''

### recursion


'''import time
def countdown(number):
    ## counting down to zero (base case: number = 0, recursive case: number != 0, countdown again, but number -1)...write this before
    print(number)
    time.sleep(1) # pause for a second

    if number == 0: ## base case (will exit the loop)
        return 

    countdown(number - 1)


countdown(10)'''



'''def fibonacci(n):                                
    if n == 0 or n == 1:
        return 1                                        ## recursvie case: call fibonnaci, n - 1, n - 2
                                                         ## if we want 5 fibonacci numbers, that's n
    return fibonacci(n - 1) + fibonacci(n - 2)       ## base is when n == 0 or n ==1 (first two numbers in sequence)...return 1

print([fibonacci(n) for n in range(6)])       ''' 

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    

emp_1 = Employee('Corey', 'Shafer', 50000)
emp_2 = Employee('Test', 'User', 60000)


