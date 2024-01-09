'''
Step 1

'''
# def gener(n):
#     for i in range(n):
#         yield i**3

# for x in gener(10):
#     print(x)

'''
Step 2

'''
# def gen_fibon(n):
#     a=1
#     b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
        
# for number in gen_fibon(10):
#     print(number)

'''
Step 3

'''
# def simple_gen():
#     for x in range(3):
#         yield x
        
# for number in simple_gen():
#     print(number)
    
# g = simple_gen()    

# print(next(g))
# print(next(g))
# print(next(g))
# print(g)

s='hello'
# for letter in s:
#     print(letter)
    
# s_iter=iter(s)
# for i in int(s_iter)*3:
#     next(s_iter)