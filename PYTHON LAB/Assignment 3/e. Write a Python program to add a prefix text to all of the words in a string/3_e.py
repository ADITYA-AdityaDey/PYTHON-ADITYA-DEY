# Python3 code to demonstrate working of 
# Append suffix / prefix to strings in list 
# Using list comprehension + "+" operator 

# initializing list 
test_list = ['T', 'M', 'S', 'L'] 

# printing list 
print("ORIGINAL : " + str(test_list)) 

# initializing append_str 
append_str = 'CSE'

# Append prefix to strings in list 
pre_res = [append_str + sub for sub in test_list] 


# Printing result 
print("AFTER PREFIX ADDITION : " + str(pre_res)) 
