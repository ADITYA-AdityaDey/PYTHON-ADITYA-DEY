import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

# Test Data
degree_input = 15

# Convert degrees to radians
result_in_radians = degrees_to_radians(degree_input)

# Display the result
print(f'Degree: {degree_input}')
print(f'Radians: {result_in_radians}')

