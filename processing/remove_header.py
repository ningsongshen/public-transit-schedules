import os

def remove_header(infolder: str, outfolder: str):
    for i in os.listdir(outfolder):
        with open(outfolder + i, 'r') as fin:
            data = fin.read().splitlines(True)
        with open(outfolder + i, 'w') as fout:
            fout.writelines(data[1:])
            
if __name__ == "__main__":
    inf = "c:/Users/nings/OneDrive - The University of Western Ontario/Scholar's 2200E/raw_data/"
    outf = "c:/Users/nings/OneDrive - The University of Western Ontario/Scholar's 2200E/csv_data/"
    remove_header(inf, outf)