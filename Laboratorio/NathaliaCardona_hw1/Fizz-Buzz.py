import numpy as np
for i in range(101):
	a=i%3
	b=i%7
	if (a==0 and (b==0 or "7" in str(i))):
		print("Fizz Buzz")
	elif (a==0 and b!=0):
		print("Fizz")
	elif (b==0 or "7" in str(i) and a!=0):
		print ("Buzz")
	else:
		print(i)
