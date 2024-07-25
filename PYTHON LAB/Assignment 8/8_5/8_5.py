def count_occurrences(file_name, pattern):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            occurrences = content.count(pattern)
            print(f'The pattern "{pattern}" occurs {occurrences} times in the file.')
    except FileNotFoundError:
        print(f'Error: File "{file_name}" not found.')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    pattern = input("Enter the string pattern to search: ")

    count_occurrences(file_name, pattern)

