try:
    with open('10_4.py', 'r') as file:
        # Your code to read from the file goes here
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'data.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

