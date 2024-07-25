def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

# Sample List
sample_list = [8, 2, 3, -1, 7]

# Calculate the product
result = multiply_list(sample_list)

# Display the result
print("Expected Output:", result)

