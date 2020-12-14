import os
from processing.combine import combine
from processing.keep_latest import keep_latest
from processing.json_to_csv import json_updates_to_csv
from processing.remove_header import remove_header
from processing.constants.locations import CLEAN_DIRECTORY, LOCAL_DIRECTORY, OUTPUT_DIRECTORY, RESULT_DIRECTORY
from processing.remove_empty import remove_empty_files

def main():
    # Remote all empty files
    # Convert to CSV
    # Keep only updates with latest timestamp
    # Merge into one file
    # All in ONE CLICK
    
    # Remove empty files from download
    remove_empty_files(LOCAL_DIRECTORY)

    # Convert all files to CSV
    print('Converting files to CSV...')
    sum = 0

    converted = set()
    for file in os.listdir(OUTPUT_DIRECTORY):
        converted.add(file[:-4])

    for file in os.listdir(LOCAL_DIRECTORY):
        in_filepath = LOCAL_DIRECTORY + "/" + file
        if file[:-4] in converted:
            os.remove(in_filepath)
        elif file[:-4] not in converted:
            in_filepath = LOCAL_DIRECTORY + "/" + file
            out_filepath = OUTPUT_DIRECTORY + "/" + file[:-4] + '.csv'
            json_updates_to_csv(in_filepath, out_filepath)
            os.remove(in_filepath)
            sum += 1
    print(f'Done. {sum} files converted.')
    
    # Remove header from the files
    # remove_header(LOCAL_DIRECTORY, OUTPUT_DIRECTORY)

    # Keep only the latest timestamps
    files = sorted(os.listdir(OUTPUT_DIRECTORY))
    sum = 0
    print('Cleaning up data...')
    for i in range(len(files) - 1):
        curf = OUTPUT_DIRECTORY + "/" + files[i]
        nextf = OUTPUT_DIRECTORY + "/" + files[i+1]
        keep_latest(files[i], curf, nextf)
        sum += 1
        os.remove(curf)
    print(f'Done. {sum} files processed.')
    # DON'T DELETE THE REMAINIGN FILE, It's needed for the next pipeline download
    
    # Combine files and delete clean CSVs
    remove_empty_files(CLEAN_DIRECTORY)
    combine(CLEAN_DIRECTORY, RESULT_DIRECTORY)

if __name__ == "__main__":
    main()