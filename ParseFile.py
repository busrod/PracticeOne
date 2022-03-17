from paramiko.client import SSHClient, AutoAddPolicy
from paramiko import SSHConfig

SSH_CONFIG = 'file.txt'
SSH_HOST = "HQ-OS"

config = SSHConfig()
config_file = open(SSH_CONFIG)

config.parse(config_file)

dev_config = config.lookup(SSH_HOST)

client = SSHClient

client.set_missing_host_key_policy(AutoAddPolicy)
HOST = dev_config['host']

client.connect(HOST, port=int(dev_config['port']),
               username=dev_config['user'],
               key_filename=dev_config['file'],
               look_for_keys=False,
               allow_agent=False)

client.close()

