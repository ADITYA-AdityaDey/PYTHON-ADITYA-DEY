assignment=int(input("ENTER MARKS OF THE ASSIGNMENT : "))
test=int(input("ENTER MARKS OF THE TEST : "))
lab=int(input("ENTER MARKS OF THE LAB : "))

avg=(assignment+test+lab)/3

print("AVERAGE MARKS OF JAMES POTTER IS : ",avg)
if(avg>=90):
    print("LETTER GRADE OF JAMES POTTER IS : A")
elif(avg>=80):
    print("LETTER GRADE OF JAMES POTTER IS : B")
elif(avg>=70):
    print("LETTER GRADE OF JAMES POTTER IS : C")
elif(avg>=60):
    print("LETTER GRADE OF JAMES POTTER IS : D")
else:
    print("LETTER GRADE OF JAMES POTTER IS : F")
