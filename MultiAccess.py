import json
import time

from paramiko.client import SSHClient, AutoAddPolicy

credentials = {}
with open("credentials.json") as fh:
    credentials = json.load(fh)

CMD = "ip r p"

for cred in credentials:
    out_file_name = str(cred['name']) + ".txt"
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    SSH_HOST = cred['host']
    client.connect(SSH_HOST, port=cred['port'],
                   username=cred['username'],
                   password=cred['password'])

    stdin, stdout, stderr = client.exec_command(CMD)
    time.sleep(5)
    out_file = open(out_file_name, "w")
    output = stdout.readlines()

    for line in output:
        out_file.write(line)
    out_file.close()
    client.close()
    print("Executed command on " + cred['name'])
    print('Executed successfully')
