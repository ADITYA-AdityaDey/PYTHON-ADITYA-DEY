def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r') as file:
            lines = [file.readline().strip() for _ in range(n)]
            return lines
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    
    try:
        n = int(input("Enter the number of lines to read: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        exit()

    result = read_first_n_lines(file_path, n)
    
    if isinstance(result, list):
        print(f"\nThe first {n} lines of the file '{file_path}' are:\n")
        for line in result:
            print(line)
    else:
        print(result)

