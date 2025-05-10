import os

def get_directory_names(path):
    """
    Gets a list of directory names within a given path.

    Args:
        path: The path to the directory.

    Returns:
        A list containing the names of all directories within the path.
    """

    directory_names = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directory_names.append(item)
    return directory_names

# Example usage:
directory_path = "."  # Current directory
directory_list = get_directory_names(directory_path)
print(directory_list)