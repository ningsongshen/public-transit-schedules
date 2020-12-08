import paramiko
from collecting.constants.ssh import *

# TODO: Use AsyncSSH to speed up the process. It works now because I let it
# run in bg, but its kinda slow.

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE_LOCATION)
ssh_client.connect(
    hostname=HOSTNAME, 
    username=USERNAME, 
    pkey=key
)

sftp_client = ssh_client.open_sftp()
file_list = sftp_client.listdir(REMOTE_DIRECTORY)
print("Getting files...")

for file in file_list:
    remote_file_path = REMOTE_DIRECTORY + "/" + file
    local_file_path = LOCAL_DIRECTORY + "/" + file
    sftp_client.get(remote_file_path, local_file_path)
    sftp_client.remove(remote_file_path)

# Since file_list is obtained before we do all the downloads, the files that
# are created by the other script during the process are not downloaded and 
# will be downloaded next time.

print("Done.")
sftp_client.close()