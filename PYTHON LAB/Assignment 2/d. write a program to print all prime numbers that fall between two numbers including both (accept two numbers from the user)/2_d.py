start = int(input("ENTER THE START OF RANGE : "))
end = int(input("ENTER THE END OF RANGE : "))

for num in range(start, end + 1):
   if num > 1:
       for i in range(2, int(num**0.5) + 1):
           if (num % i) == 0:
               break
       else:
           print(num)
