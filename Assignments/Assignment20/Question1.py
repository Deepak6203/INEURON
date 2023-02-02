# 1. Write a python program to create a function that takes a list and 
# returns a new list with the original list's unique elements

def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 


