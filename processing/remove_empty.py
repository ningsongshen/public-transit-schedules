from processing.constants.locations import LOCAL_DIRECTORY
import os

def remove_empty_files(directory):
    total_removed = 0
    print('Removing empty files...')

    for file in os.listdir(directory):

        filepath = directory + "/" + file

        try: 
            if os.path.getsize(filepath) == 0:
                os.remove(filepath)
                total_removed += 1

        except WindowsError:
            continue

    print(f'Done. {total_removed} files removed.')

if __name__ == "__main__":
    remove_empty_files(LOCAL_DIRECTORY)