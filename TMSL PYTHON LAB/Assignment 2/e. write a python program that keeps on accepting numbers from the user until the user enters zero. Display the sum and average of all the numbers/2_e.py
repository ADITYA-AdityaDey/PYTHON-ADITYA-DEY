print("INPUT SOME INTEGERS TO CALCULATE THEIR SUM AND AVERAGE. INPUT 0 TO EXIT.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("INPUT SOME NUMBERS")
else:
	print("AVERAGE AND SUM OF THE ABOVE NUMBERS ARE: ", sum / (count-1), sum)
