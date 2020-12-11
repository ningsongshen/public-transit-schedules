# We have a csv with the actual stop times.
# We have another CSV with the scheduled stop times.
# We want to combine them so we can run a linear regression.
# We use pandas

import pandas as pd 
from processing.constants.locations import CLEAN_DIRECTORY, LTC_DIRECTORY

schedule_csv_path = LTC_DIRECTORY + '/schedule/stop_times.txt'
schedule_df = pd.read_csv(schedule_csv_path)
schedule_df = schedule_df.drop(columns=['stop_headsign', 'arrival_time', 'pickup_type', 'drop_off_type', 'timepoint'])
print(schedule_df.head())

actual_csv_path = CLEAN_DIRECTORY + '/result.csv'
actual_df = pd.read_csv(actual_csv_path, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
print(actual_df.info())
print(actual_df.head())

combined_df = actual_df.merge(schedule_df, how='inner', on=['trip_id', 'stop_id', 'stop_sequence'])
print(combined_df.head())
