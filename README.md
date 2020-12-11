# se-2200e
Scholar's Electives 2200E Supervised Individual Research I

Title of Project: "Using Machine Learning to Optimize Transit Scheduling and Efficiency"

This repository contains the code to collect, process, and model the data to better predict transit schedule deviations. We use the London Transit's GTFS feed as a data source and focus on the particulars regarding a medium-sized city and highly directional travel (to Western University).

## System Overview

_Ensure that the processing and the modelling do not run at the same time!_

### Collecting

- An AWS virtual machine is used to collect data continuously
- The `realtime_grab.py` script pings the London Transit GTFS API and creates a text file
- Crontab runs the `realtime_grab.py` script every minute when London Transit operates.
- At regular intervals through the week, researcher manually transfers data from the VM to the raw data store with the `download.py` script

### Processing

WIP
- A single entrypoint will convert GTFS data to malleable CSV files, use only the latest trip updates, and consolidate into a single file
- remote_empty: Remove empty removes empty files (duh)
- remove_header: Remove header removes the CSV header (duh)
- json_to_csv converts all GTFS files to CSV format in specified folders. If already converted, it does not convert again. Runs on about 40,000 files or 70,000,000 lines in <30 mins.
- keep_latest: in each file all updates are kept. But we only want the latest stop_time_update, the rest can be discarded.
- combine: combine all files in to one file
- schedule_matching: combine the scheduled data and the actual data so we can easily do modelling

### Modelling

## Other Notes

Things to do:
- Process the historical data and perform a linear regression
- jupyter notebook or python files?
- learn about the other algorithms and how to implement them

How the files work:
- realtime_grab.py is uploaded to an AWS EC2 instance
- Using a cron job, it is run every minute and file stored into /data/
- Using another cron job, the files stored into /data/ are transferred to AWS S3
- I'll go into S3 once its all done to download the dataset and clean it up

Notable struggles:
- Setting up an EC2 Instance and working with AWS CLI and permissions
- reading/writing to files with a+ in Python
- installing the required stuff in EC2
