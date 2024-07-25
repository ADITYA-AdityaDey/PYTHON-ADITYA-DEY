def write_list_to_file(file_path, input_list):
    try:
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List has been written to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
my_list = [1, 2, 3, 4, 5]
file_path = "output.txt"

write_list_to_file(file_path, my_list)

