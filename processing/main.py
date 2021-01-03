import time
from .combine import combine
from .keep_latest import *
from .json_to_csv import *
from .constants.locations import *
from .remove_empty import remove_empty_files

def main():
    # Remote all empty files
    # Convert to CSV
    # Keep only updates with latest timestamp
    # Merge into one file
    # All in ONE CLICK
    
    start = time.time()
    print(f'Start: {time.strftime("%H:%M:%S", time.localtime())}')

    # Remove empty files from download
    print(f'Removing empty files from {LOCAL_DIRECTORY}...')
    total_removed = remove_empty_files(LOCAL_DIRECTORY)
    print(f'Done. {total_removed} files removed. {time.time() - start} seconds elapsed.')

    # Convert all files to CSV
    print('Converting files to CSV...')
    total_converted = convert_folder(LOCAL_DIRECTORY, OUTPUT_DIRECTORY)
    print(f'Done. {total_converted} files converted. {time.time() - start} seconds elapsed.')
    
    # NOT NEEDED RIGHT NOW: Remove header from the files
    # remove_header(LOCAL_DIRECTORY, OUTPUT_DIRECTORY)

    # Keep only the latest timestamps
    print('Cleaning up data...')
    total_processed = keep_latest(OUTPUT_DIRECTORY)
    print(f'Done. {total_processed} files processed. {time.time() - start} seconds elapsed.')
    # DON'T DELETE THE REMAINING FILE, It's needed for the next pipeline download

    # Remove empty files from cleaned
    print(f'Removing empty files from {CLEAN_DIRECTORY}...')
    total_removed = remove_empty_files(CLEAN_DIRECTORY)
    print(f'Done. {total_removed} files removed. {time.time() - start} seconds elapsed.')

    # Combine all files into one big file
    print(f'Combining files...')
    combine(CLEAN_DIRECTORY, RESULT_DIRECTORY)
    print(f'All processing done. Total {time.time() - start} seconds elapsed.')

if __name__ == "__main__":
    main()