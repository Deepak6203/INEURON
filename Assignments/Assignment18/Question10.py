# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {'C': 92, 'Java': 66, 'Python': 85}




sample_dict = {'C': 92, 'Java': 66, 'Python': 85}
print("The original dictionary is : " + str(sample_dict))
temp = min(sample_dict.values())
res = [key for key in sample_dict if sample_dict[key] == temp]

print("Keys Min IS : " + str(res))
