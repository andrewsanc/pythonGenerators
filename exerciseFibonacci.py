'''
Python Jupyter - Exercise: Fibonnaci Numbers 
'''
#%%
def fib(num):
  if num < 2:
    return num
  
  return fib(num-1) + fib(num-2)

print(fib(6))

#%%
def fib2(number):
    a =  0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))
#%%
