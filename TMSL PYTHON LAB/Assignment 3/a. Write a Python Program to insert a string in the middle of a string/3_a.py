def insert_string_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'DSA'))
print(insert_string_middle('{{}}', 'PYTHON'))
print(insert_string_middle('<<>>', 'JAVA SCRIPT'))

