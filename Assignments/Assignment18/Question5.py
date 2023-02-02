# 5. Write a python program to print all key names in the dictionary, one by one


data = {
   'Counrty': 'India',
   'State': 'Bihar',
   'FName': 'Deepak',
   'LNmae': 'Kumar'
}
for keys, value in data.items():
   print(keys)