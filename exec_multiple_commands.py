from paramiko import Channel
from paramiko.client import SSHClient, AutoAddPolicy
import time
import discord

SSH_PASSWORD = 'oliversoft'
SSH_USER = 'admin'
SSH_PORT = 2222
SSH_HOST = '192.168.80.27'

client = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy)

client.connect(SSH_HOST, port=SSH_PORT,
               username=SSH_USER,
               password=SSH_PASSWORD,
               look_for_keys=False,
               allow_agent=False)

with client.invoke_shell() as ssh:
    ssh.send('ip ad ad ad=192.168.87.1/24 interface=All_LAN\n')

    time.sleep(1)

    ssh.send('ip r add gateway=192.168.87.1')
    time.sleep(1)
    ssh.recv(1024)


client.close()
