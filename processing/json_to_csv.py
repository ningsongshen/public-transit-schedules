import csv
import os

class Update:
    def __init__(self, trip_id, start_time, start_date, route_id, stop_sequence, departure_time, stop_id) -> None:
        self.trip_id = trip_id
        self.start_time = start_time
        self.start_date = start_date
        self.route_id = route_id
        self.stop_sequence = stop_sequence
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.vehicle_id = ""
        self.vehicle_label = ""
        self.timestamp = 0

def gtfs_to_csv(infile: str, outfile: str) -> None:
    u = Update(0, "", "", "", 0, 0, "")
    entries = set()
    to_add = set()
    with open(infile, "r") as f:
        line = f.readline().strip()
        while line != '':
            if line.startswith("trip {"):
                u.trip_id = f.readline().strip().split()[-1][1:-1]
                u.start_time = f.readline().strip().split()[-1][1:-1]
                u.start_date = f.readline().strip().split()[-1][1:-1]
                u.route_id = f.readline().strip().split()[-1][1:-1]
                temp = f.readline().strip()
                if temp != "}":
                    temp = f.readline().strip()

            elif line.startswith("stop_time_update {"):
                u.stop_sequence = f.readline().strip().split()[1]
                temp = f.readline().strip()
                u.departure_time = f.readline().strip().split()[-1]
                temp = f.readline().strip()
                u.stop_id = f.readline().strip().split()[-1][1:-1]
                temp = f.readline().strip()

                # Avoid the use of deepcopy for efficiency from 0.2 seconds to 0.1 seconds
                to_add.add(Update(u.trip_id, u.start_time, u.start_date, u.route_id, u.stop_sequence, u.departure_time, u.stop_id))
            
            elif line.startswith("vehicle {"):
                vid = f.readline().strip().split()[-1][1:-1]
                vlabel = f.readline().strip().split()[-1][1:-1]
                for i in to_add:
                    i.vehicle_id = vid
                    i.vehicle_label = vlabel

            elif line.startswith("timestamp: "):
                ts = line.split()[-1]
                for i in to_add:
                    i.timestamp = ts
                for i in to_add:
                    entries.add(i)
                to_add.clear()


            line = f.readline().strip()

    with open(outfile, "w+", newline='', encoding='utf-8') as outf:
        outfwriter = csv.writer(outf)
        outfwriter.writerow(["trip_id", "start_date", "start_time", "route_id", "stop_sequence", "departure_time", "stop_id", "vehicle_id", "vehicle_label", "timestamp"])
        for i in entries:
            data = [i.trip_id, i.start_date, i.start_time, i.route_id, i.stop_sequence, i.departure_time, i.stop_id, i.vehicle_id, i.vehicle_label, i.timestamp]
            # print(data)
            outfwriter.writerow(data)

def convert_folder(indirectory: str, outdirectory: str) -> int:
    total_files_converted = 0

    converted = set()
    # Get list of files already converted, without extension
    for file in os.listdir(outdirectory):
        converted.add(file[:-4])

    for file in os.listdir(indirectory):
        in_filepath = indirectory + "/" + file
        if file[:-4] in converted:
            os.remove(in_filepath)
        elif file[:-4] not in converted:
            in_filepath = indirectory + "/" + file
            out_filepath = outdirectory + "/" + file[:-4] + '.csv'
            gtfs_to_csv(in_filepath, out_filepath)
            os.remove(in_filepath)
            total_files_converted += 1

    return total_files_converted

if __name__ == "__main__":
    from processing.constants.locations import LOCAL_DIRECTORY, OUTPUT_DIRECTORY

    print('Converting files to CSV...')
    sum = 0

    converted = set()
    for file in os.listdir(OUTPUT_DIRECTORY):
        converted.add(file[:-4])

    for file in os.listdir(LOCAL_DIRECTORY):
        if file[:-4] not in converted:
            in_filepath = LOCAL_DIRECTORY + "/" + file
            out_filepath = OUTPUT_DIRECTORY + "/" + file[:-4] + '.csv'
            gtfs_to_csv(in_filepath, out_filepath)
            sum += 1
    print(f'Done. {sum} files converted.')
