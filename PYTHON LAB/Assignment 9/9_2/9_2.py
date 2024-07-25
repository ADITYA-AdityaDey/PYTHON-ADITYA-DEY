import random
from datetime import datetime, timedelta

# Generate a random integer between 0 and 6 (excluding 6)
random_int_0_to_6 = random.randint(0, 5)
print("Random integer between 0 and 6 (excluding 6):", random_int_0_to_6)

# Generate a random integer between 5 and 10 (excluding 10)
random_int_5_to_10 = random.randint(5, 9)
print("Random integer between 5 and 10 (excluding 10):", random_int_5_to_10)

# Generate a random integer between 0 and 10 with a step of 3
random_int_0_to_10_step_3 = random.randrange(0, 11, 3)
print("Random integer between 0 and 10 with a step of 3:", random_int_0_to_10_step_3)

# Generate a random date between two dates (e.g., 2019-02-17 and today's date)
start_date = datetime.strptime("2019-02-17", "%Y-%m-%d")
end_date = datetime.now()
random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
print("Random date between 2019-02-17 and today:", random_date.strftime("%Y-%m-%d"))

