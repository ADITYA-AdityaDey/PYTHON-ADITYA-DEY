# Python3 code to demonstrate working of 
# Replace words from Dictionary
# Using list comprehension + join()

# initializing string
test_str = 'TechnoIndia is one of the best colleges in India'

# printing original string
print("The original string is : " + str(test_str))

# lookup Dictionary
lookp_dict = {"India" : "West Bengal"}

# one-liner to solve problem
res = " ".join(lookp_dict.get(ele, ele) for ele in test_str.split())

# printing result 
print("Replaced Strings : " + str(res))
