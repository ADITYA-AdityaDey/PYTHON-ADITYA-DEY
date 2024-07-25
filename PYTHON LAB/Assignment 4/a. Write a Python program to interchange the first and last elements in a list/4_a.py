a=[]


n= int(input("ENTER THE NUMBER OF ELEMENTS IN LIST : "))
for x in range(0,n):
    element=int(input("ENTER ELEMENT" + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("NEW LIST IS : ")
print(a)
