a=[]
n=int(input("ENTER NUMBER OF ELEMENTS : "))
for i in range(1,n+1):
    b=int(input("ENTER ELEMENT : "))
    a.append(b)
a.sort()
print("SECOND LARGEST ELEMENT IS : ",a[n-2])
