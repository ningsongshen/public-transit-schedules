import paramiko

# TODO: Use AsyncSSH to speed up the process. It works now, I let it run in bg, but its kinda slow.

HOSTNAME = 'ec2-3-19-75-202.us-east-2.compute.amazonaws.com'
USERNAME = 'ubuntu'
PRIVATE_KEY_FILE_LOCATION = 'C:/Users/nings/.ssh/vm1-test.pem'
KEY = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE_LOCATION)

# From the home directory
REMOTE_DIRECTORY = 'data'

# Absolute path
LOCAL_DIRECTORY = 'C:/Users/nings/OneDrive - The University of Western Ontario/Scholar\'s 2200E/raw_data'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='ec2-3-19-75-202.us-east-2.compute.amazonaws.com', username='ubuntu', pkey=KEY)

sftp_client = ssh_client.open_sftp()
file_list = sftp_client.listdir(REMOTE_DIRECTORY)
print("Getting files...")

for file in file_list:
    remote_file_path = REMOTE_DIRECTORY + "/" + file
    local_file_path = LOCAL_DIRECTORY + "/" + file
    sftp_client.get(remote_file_path, local_file_path)
    sftp_client.remove(remote_file_path)

# Since file_list is obtained before we do all the downloads, the files that are created by the other script 
# during the process are not downloaded and will be downloaded next time.

print("Done.")
sftp_client.close()