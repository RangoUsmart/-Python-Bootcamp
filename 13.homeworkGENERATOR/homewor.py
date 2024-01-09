'''
Problem 1
Create a generator that generates the squares of numbers up to some number N.
'''
def square(n):
    for i in range(n):
        yield i**2
        
for x in square(26):
    print(x)
    
'''
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:
'''
print("-"*100)
import random

def rand_num(minv,maxv,s):
    val=0
    for i in range(s):
        val=random.randint(minv,maxv)
        yield val
        
for num in rand_num(1,10,1):
    print(num)
    
'''    
Problem 3
Use the iter() function to convert the string below into an iterator:    
'''    
print("-"*100)

s = 'hello'
s_iter=iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
 
'''    
Problem 4
Explain a use case for a generator using a yield statement where you
would not want to use a normal function with a return statement.  

У Python ключове слово yield використовується для створення генераторів.
Генератори це функції, які можуть зберігати свій стан виконання між викликами. 
Коли функція викликається з оператором yield, вона повертає значення,
але залишає свій стан, щоб в наступний раз продовжити виконання з того ж місця. 
'''

def yi_gen():
    yield 1
    yield 2
    yield 3

gen = yi_gen()

print(next(gen))  # Виведе: 1
print(next(gen))  # Виведе: 2
print(next(gen))  # Виведе: 3    

print("-"*100)    

'''    
Problem 4
Extra Credit!
Can you explain what gencomp is in the code below? 
(Note: We never covered this in lecture! You will have to do some Googling/Stack Overflowing!) 
'''

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)
print(type(gencomp))
for item in gencomp:
    print(item)