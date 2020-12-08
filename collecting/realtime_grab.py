from google.transit import gtfs_realtime_pb2
import urllib.request
import datetime

# This file runs on a virtual machine and is run by a cron job frequently
# It's probably good enough to pull the data every minute and have the EC2 instance running 24/7. 

def get_realtime_feed_data():
    """Pull data from GTFS realtime feed and write update to text file

    """
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

if __name__ == "__main__":
    get_realtime_feed_data()