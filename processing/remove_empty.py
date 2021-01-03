import os

def remove_empty_files(directory: str) -> int:
    total_files_removed = 0
    for file in os.listdir(directory):
        filepath = directory + "/" + file
        try: 
            if os.path.getsize(filepath) == 0:
                os.remove(filepath)
                total_files_removed += 1
        except WindowsError:
            continue
    return total_files_removed 

if __name__ == "__main__":
    from .constants.locations import LOCAL_DIRECTORY
    remove_empty_files(LOCAL_DIRECTORY)