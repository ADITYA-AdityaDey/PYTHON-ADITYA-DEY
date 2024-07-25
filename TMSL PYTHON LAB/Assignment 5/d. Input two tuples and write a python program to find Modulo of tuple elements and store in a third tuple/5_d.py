tup1 = (10, 4, 5, 6)
tup2 = (5, 6, 7, 5)


print("THE ORIGINAL TUPLE 1 : " + str(tup1))
print("THE ORIGINAL TUPLE 2 : " + str(tup2))

# TUPLE MODULO
# USING ZIP() + GENERATOR EXPRESSION
res = tuple(ele1 % ele2 for ele1, ele2 in zip(tup1, tup2))

# PRINTING RESULT
print("THE MODULUS TUPLE : " + str(res))

