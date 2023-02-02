# 4. Write a python program to create a function which expects kwargs arguments


def func(**kwargs):
	for key, value in kwargs.items():
		print("%s => %s" % (key, value))


func(FName='Deepak', Lname='Kumar', Gender='Male', Age='21')
