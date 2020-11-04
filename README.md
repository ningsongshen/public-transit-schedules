# se-2200e
Supervised Individual Research I - Transit Scheduling

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