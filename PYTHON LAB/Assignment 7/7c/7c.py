def count_upper_lower_case(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case Characters:", lower_count)

# Example usage:
input_str = 'The quick Brown Fox'
count_upper_lower_case(input_str)

