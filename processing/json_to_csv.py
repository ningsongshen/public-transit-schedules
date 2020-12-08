import copy, csv, os
import Update

    
def json_updates_to_csv(infile, outfile):
    with open(outfile, "w+", newline='', encoding='utf-8') as inf:
        outfwriter = csv.writer(inf)
        u = Update()
        outfwriter.writerow(["trip_id", "start_date", "start_time", "route_id", "stop_sequence", "departure_time", "stop_id", "vehicle_id", "vehicle_label", "timestamp"])
        to_add = []
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

                    export = copy.deepcopy(u)
                    to_add.append(export)
                
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
                        data = [i.trip_id, i.start_date, i.start_time, i.route_id, i.stop_sequence, i.departure_time, i.stop_id, i.vehicle_id, i.vehicle_label, i.timestamp]
                        # print(data)
                        outfwriter.writerow(data)
                    to_add = []


                line = f.readline().strip()
                
if __name__ == "__main__":
    infolder = "raw_data/updates/"
    outfolder = "csv_data/updates"
    for i in os.listdir(infolder):
        json_updates_to_csv(infolder + i, outfolder + i[:-4] + ".csv")
