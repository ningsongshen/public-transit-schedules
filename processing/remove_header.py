import os

if __name__ == "__main__":
    infolder = "c:/Users/nings/OneDrive - The University of Western Ontario/Scholar's 2200E/raw_data/"
    outfolder = "c:/Users/nings/OneDrive - The University of Western Ontario/Scholar's 2200E/csv_data/"
    for i in os.listdir(outfolder):
        with open(outfolder + i, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(outfolder + i, 'w') as fout:
            fout.writelines(data[1:])