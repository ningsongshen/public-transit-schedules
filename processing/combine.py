import glob, os

def combine(directory: str, outdirectory: str):
    read_files = glob.glob(directory + '\*.csv')
    with open(outdirectory + '/' + 'result.csv','ab') as outfile:
        outfile.write(str.encode('trip_id,start_date,start_time,route_id,stop_sequence,departure_time,stop_id,vehicle_id,vehicle_label,timestamp\n'))
        for f in read_files:
            with open(f, 'rb') as infile:
                next(infile)
                outfile.write(infile.read())

            os.remove(f)

if __name__ == "__main__":
    from .constants.locations import CLEAN_DIRECTORY, RESULT_DIRECTORY
    combine(CLEAN_DIRECTORY, RESULT_DIRECTORY)