from processing.constants.locations import CLEAN_DIRECTORY
import glob

read_files = glob.glob(CLEAN_DIRECTORY + '\*.csv')

with open(CLEAN_DIRECTORY + '/' + 'result.csv','wb') as outfile:
    outfile.write('trip_id,start_date,start_time,route_id,stop_sequence,departure_time,stop_id,vehicle_id,vehicle_label,timestamp')
    for f in read_files:
        with open(f, 'rb') as infile:
            next(infile)
            outfile.write(infile.read())