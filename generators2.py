'''
Python Jupyter - Generators part 2. Generators are iterables while not all iterables are
                 generators. The difference between the two is the way the their implemented.
'''
#%%
def genFunc(num):
  for i in range(num):
    yield i*2

g = genFunc(100)
print(next(g))

#%%
def genFunc(num):
  for i in range(num):
    yield i*2

g = genFunc(100)
print(next(g))
print(next(g))
print(next(g))

#%%
