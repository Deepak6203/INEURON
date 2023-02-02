# 8. Write a Python script to print distinct elements along with 
# their frequencies of occurrence in the list


any_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']
frequency = {}

for item in any_list:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# print the frequency
print(frequency)

# Output
# {'A': 3, 'B': 3, 'C': 1, 'D': 2}