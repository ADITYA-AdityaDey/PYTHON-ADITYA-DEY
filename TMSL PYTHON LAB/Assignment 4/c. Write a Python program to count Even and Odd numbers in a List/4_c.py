NumList = []
Even_count = 0
Odd_count = 0
j = 0

Number = int(input("PLEASE ENTER THE TOTAL NUMBER OF LIST ELEMENTS : "))
for i in range(1, Number + 1):
    value = int(input("PLEASE ENTER THE VALUE OF %d ELEMENT : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_count = Even_count + 1
    else:
        Odd_count = Odd_count + 1
    j = j + 1

print("\nTOTAL NUMBER OF EVEN NUMBERS IN THIS LIST =  ", Even_count)
print("TOTAL NUMBER OF ODD NUMBERS IN THIS LIST = ", Odd_count)
