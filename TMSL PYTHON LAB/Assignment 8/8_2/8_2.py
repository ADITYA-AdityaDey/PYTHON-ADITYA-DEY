def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
file_path = '8_2.py'
lines_count = count_lines(file_path)

if lines_count is not None:
    print(f"The number of lines in the file '{file_path}' is: {lines_count}")

