import time

from paramiko.client import SSHClient, AutoAddPolicy
import getpass

SSH_PASSWORD = 'oliversoft'
SSH_USER = 'admin'

SSH_PORT = 2222
SSH_HOST = '192.168.80.27'

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy)
try:
    client.connect(SSH_HOST, port=SSH_PORT,
                   username=SSH_USER,
                   password=SSH_PASSWORD)
    CMD = "ip dhcp-ser leas p"
    stdin, stdout, stderr = client.exec_command(CMD)
    time.sleep(5)
    output = stdout.readlines()
    print('okay')
    for line in output:
        print(line.strip())

    with open("backup.txt","w") as out_file:
        for line in output:
            out_file.write(line)
    client.close()
    print('Success')
except Exception:
    print('failed to establish connection')
