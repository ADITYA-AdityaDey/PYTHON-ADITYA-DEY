str1 = "RACE"
str2 = "CARE"


# check if length is same
if(len(str1) == len(str2)):

    # sort the strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print(str1 + " AND " + str2 + " ARE ANAGRAM")
    else:
        print(str1 + " AND " + str2 + " ARE NOT ANAGRAM")

else:
    print(str1 + " AND " + str2 + " ARE NOT ANAGRAM")
