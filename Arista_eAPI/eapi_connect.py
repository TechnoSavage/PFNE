import jsonrpclib
from pprint import pprint

ip = '1.1.1.1'
port = '8243'

username = 'eapi'
password = '99saturday'

switch_url = 'https://{}:{}@{}:{}'.format(username, password, ip, port) #also %s works
switch_url = switch_url + '/command-api'

remote_connect = jsonrpclib.Server(switch_url)

response = remote_connect.runCmds(1, ['show version'])
pprint(response)
response = remote_connect.runCmds(1, ['show arp'])
pprint(response)

commands = []
commands.append('vlan 255')
commands.insert(0, 'configure terminal')
commands.insert(0, {'cmd': 'enable', 'input': ''})
commands.append('name GREEN')

remote_connect.runCmds(1, commands)

commands[2] = 'vlan 226'
commands[3] = 'vlan 227'