# 6. Write a python program to create a dictionary that contains three dictionaries.
# (nested)


        #Dict 1       Dict 2    Dict 3
Dict = { 'Country1': {'India': {"State" : "Bihar"} },
         'Country2': {'Nepal': {"State" : "Deukhuri"} }
       }

print(Dict['Country1']['India']["State"])
print(Dict['Country2']['Nepal']["State"])