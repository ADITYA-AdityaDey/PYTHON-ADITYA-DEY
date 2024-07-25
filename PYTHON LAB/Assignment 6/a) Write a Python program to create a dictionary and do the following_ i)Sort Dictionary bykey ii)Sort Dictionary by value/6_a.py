key_value={}

key_value[5] = 10      
key_value[3] = 8
key_value[6] = 77
key_value[4] = 23
key_value[2] = 9     
key_value[1] = 43
 
print("SORTING ON THE BASIS OF KEYS")

for i in sorted(key_value) :
    print ((i, key_value[i]), end =" ")

 
print("\nSORTING ON THE BASIS OF VALUES")

print(sorted(key_value.items(), key=lambda keyval: (keyval[1], keyval[0])))
