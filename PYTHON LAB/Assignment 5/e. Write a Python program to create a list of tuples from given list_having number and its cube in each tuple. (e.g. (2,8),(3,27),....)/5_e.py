# LIST OF TUPLES HAVING NUMBER AND ITS CUBE

def cubeoflist(li):
    # LIST OF TUPLES
    result=[(num, num**3) for num in li]
    return result

# initialise list
li = [3, 4, 1, 2]

# PRINT THE RESULT
print(cubeoflist(li))
