'''
Python Jupyter - Generators. Generators allows us to produce sequence or values over time. 
                 With the keyword yield, we're able to pause and resume functions. 
'''
#%%
def makeList(num):
  result = []
  for i in range(num): # With range. Each sequence of range it takes up memory, with generators they wont.
    result.append(i*2)
  return result

myList = makeList(100)
print(myList)

#%%
