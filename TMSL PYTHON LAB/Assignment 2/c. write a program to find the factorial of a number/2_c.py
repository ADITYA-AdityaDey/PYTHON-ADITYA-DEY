num=int(input("ENTER A NUMBER : "))
factorial=1

# CHECK IF THE NUMBER IS NEGATIVE, POSITIVE OR ZERO

if num<0:
 print("SORRY, FACTORIAL DOES NOT EXISTS FOR NEGATIVE NUMBERS")
elif num==0:
 print("THE FACTORIAL OF 0 IS 1")
else:
 for i in range (1,num+1):
  factorial=factorial*i
 print("THE FACTORIAL OF",num,"IS",factorial)
