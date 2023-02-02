# 5. Write a python script to print two given words in dictionary order


print("Enter Two Words :")
word1,word2=input(),input()
print((word2,word1) if word1 > word2 else (word1,word2))
