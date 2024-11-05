import os

def print_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# print_directory_contents('/path/to/directory')