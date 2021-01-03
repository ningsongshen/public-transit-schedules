from processing.constants.locations import OUTPUT_DIRECTORY, CLEAN_DIRECTORY
import csv, os

def keep_latest_times(curfilename: str, curfilepath: str, nextfilepath: str):
    ## ALGORITHM USED
    # for each file, open the next file and create dict with all entries: key=unique, value=timestamp.
    # open current file, check if exists in dict AND has smaller timestamp
    # if so, continue
    # else, write line to new file
    # repeat for remaining files

    # HOW DO I VERIFY THAT THIS IS CORRECT?
    nextf_updates = {}
    with open(nextfilepath, mode='r') as nextf:
        reader = csv.reader(nextf)
        nextf_updates = {row[0] + row[1] + row[2] + row[4]: row[9] for row in reader}

    with open(curfilepath, mode='r') as curf, open(CLEAN_DIRECTORY + '/' + curfilename, mode='w+', newline='') as outf:
            reader = csv.reader(curf)
            outwriter = csv.writer(outf)
            # outwriter.writerow(["trip_id", "start_date", "start_time", "route_id", "stop_sequence", "departure_time", "stop_id", "vehicle_id", "vehicle_label", "timestamp"])
            for row in reader:
                key = row[0] + row[1] + row[2] + row[4]
                if key in nextf_updates and nextf_updates[key] >= row[9]:
                    continue
                outwriter.writerow(row)

def keep_latest(directory: str) -> int:
    files = sorted(os.listdir(directory))
    total_files_processed = 0
    for i in range(len(files) - 1):
        curf = directory + "/" + files[i]
        nextf = directory + "/" + files[i+1]
        keep_latest_times(files[i], curf, nextf)
        total_files_processed += 1
        os.remove(curf)

    return total_files_processed

if __name__ == "__main__":
    files = sorted(os.listdir(OUTPUT_DIRECTORY))
    sum = 0
    print('Cleaning up data...')
    for i in range(len(files) - 1):
        curf = OUTPUT_DIRECTORY + "/" + files[i]
        nextf = OUTPUT_DIRECTORY + "/" + files[i+1]
        keep_latest(files[i], curf, nextf)
        os.remove(files[i])
        sum += 1
    print(f'Done. {sum} files processed.')