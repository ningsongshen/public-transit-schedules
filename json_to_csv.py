import re, csv, copy

class Update:
    trip_id = 0
    start_time = ""
    start_date = ""
    route_id = ""
    stop_sequence = 0
    departure_time = 0
    stop_id = ""
    vehicle_id = ""
    vehicle_label = ""
    timestamp = 0
    
def json_updates_to_csv():
    with open("csv_data/updates/2020-11-27-03-08-01.txt", "w+") as f:
        outfwriter = csv.writer(f)
        u = Update()
        to_add = []
        with open("raw_data/updates/2020-11-27-03-08-01.txt") as inf:
            line = f.readline().strip()
            while line != '':
                if line.startswith("trip {"):
                    u.trip_id = re.match(r'"(.*?)"', f.readline().strip())
                    u.start_time = re.match(r'"(.*?)"', f.readline().strip())
                    u.start_date = re.match(r'"(.*?)"', f.readline().strip())
                    u.route_id = re.match(r'"(.*?)"', f.readline().strip())
                    temp = f.readline().strip()

                elif line.startswith("stop_time_update {"):
                    u.stop_sequence = f.readline().strip()[-1]
                    temp = f.readline().strip()
                    u.departure_time = int(f.readline().strip().split()[-1])
                    temp = f.readline().strip()
                    u.stop_id = re.match(r'"(.*?)"', f.readline().strip())
                    temp = f.readline().strip()

                    export = copy.deepcopy(u)
                    to_add.append(export)
                
                elif line.startswith("vehicle {"):
                    vid = re.match(r'"(.*?)"', f.readline().strip())
                    vlabel = re.match(r'"(.*?)"', f.readline().strip())
                    for i in to_add:
                        i.vehicle_id = vid
                        i.vehicle_label = vlabel

                elif line.startswith("timestamp: "):
                    ts = int(line.split()[-1])
                    for i in to_add:
                        i.timestamp = ts

            for i in to_add:
                outfwriter.writerow([i.trip_id, i.start_date, i.start_time, i.route_id, i.stop_sequence, i.departure_time, i.stop_id, i.vehicle_id, i.vehicle_label, i.timestamp])

if __name__ == "__main__":
    json_updates_to_csv()
