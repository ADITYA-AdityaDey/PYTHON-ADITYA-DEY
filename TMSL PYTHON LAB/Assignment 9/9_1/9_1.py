import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_value_between(start, end):
    return random.randint(start, end)

def generate_random_multiple_of_7():
    return random.randrange(0, 71, 7)

# Generate a random alphabetical string
random_string = generate_random_string(100)
print("Random Alphabetic String:", random_string)

# Generate a random value between two integers (inclusive)
start_value = 0
end_value = 4
random_value = generate_random_value_between(start_value, end_value)
print("Random Value between {} and {} (inclusive): {}".format(start_value, end_value, random_value))

# Generate a random multiple of 7 between 0 and 70
random_multiple_of_7 = generate_random_multiple_of_7()
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_7)

