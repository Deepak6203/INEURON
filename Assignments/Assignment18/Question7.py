# 7. Write a python program to create three dictionaries, then create one dictionary that
# will contain the other three dictionaries.



        #Dict 1       Dict 2    Dict 3     Dict 3.1  Dict 3.2   Dict 3.3
Dict = { 'Country1': {'India': {"State" : {"Dist" : {"Gaya" : {"Block" : "Halsi"}}}} },
         'Country2': {'Bhutan': {"State" : "Gasa"} },
         'Country2': {'Nepal': {"State" : "Deukhuri"} },
       }

print(Dict['Country1']['India']["State"]["Dist"]["Gaya"]["Block"])#Halsi