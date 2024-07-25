def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()

        with open(destination_file, 'w') as destination:
            destination.write(content)

        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")

    except FileNotFoundError:
        print("One or both of the files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_file_path = 'source.txt'
destination_file_path = 'destination.txt'

copy_file(source_file_path, destination_file_path)

