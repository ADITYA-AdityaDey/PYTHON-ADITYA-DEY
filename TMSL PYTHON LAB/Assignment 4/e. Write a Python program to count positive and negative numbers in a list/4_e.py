list = [1,-2,-4,6,7,-23,45,-0,9,14,-14]
pos_count, neg_count = 0, 0


# ENHANCED FOR LOOP

for num in list:
   # CHECK FOR BEING POSITIVE
   if num >= 0:
      pos_count += 1
   else:
      neg_count += 1
      
      
print("POSITIVE NUMBERS IN THE LIST : ", pos_count)
print("NEGATIVE NUMBERS IN THE LIST : ", neg_count)
