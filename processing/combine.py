from processing.constants.locations import CLEAN_DIRECTORY
import glob

read_files = glob.glob(CLEAN_DIRECTORY + '\*.csv')

with open(CLEAN_DIRECTORY + '/' + 'result.csv','wb') as outfile:
    for f in read_files:
        with open(f, 'rb') as infile:
            outfile.write(infile.read())