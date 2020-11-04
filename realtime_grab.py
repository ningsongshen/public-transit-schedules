from google.transit import gtfs_realtime_pb2
import urllib.request
import datetime

# It's probably good enough to pull the data every minute and have the EC2 instance running 24/7. 

def get_data():
    feed = gtfs_realtime_pb2.FeedMessage()
    response = urllib.request.urlopen('http://gtfs.ltconline.ca/TripUpdate/TripUpdates.pb')
    feed.ParseFromString(response.read())

    x = datetime.datetime.now()
    dt_string = x.strftime("%Y-%m-%d-%H-%M-%S")
    f = open("data/"+dt_string+".txt", "a+")
    for entity in feed.entity:
        if entity.HasField('trip_update'):
          f.write(repr(entity.trip_update))

    f.close()

get_data()