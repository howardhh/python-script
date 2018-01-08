# -*- coding: utf-8 -*-
# @Time    : 2018/1/8
# @Author  : Howardhh
# @File    : rundeck_to_ansible.py
# @Desc	   : transfer rundeck config file to ansible format.
# 
import yaml
import re

def _read_yaml(file=''):
	with open(file,'r') as f_read:
		record_list = yaml.load(f_read)
		res = [ item for item in record_list ] if record_list else []
	f_read.close()	
	return res

# fetch value from yaml file
def _format_str(l=''):
	_hostname = l.split(';')[0]
	_ip_and_port = l.split(';')[1]
	_ip = _ip_and_port.split(':')[0] if ':' in _ip_and_port else _ip_and_port
	_port = _ip_and_port.split(':')[1] if ':' in _ip_and_port else '22'
	return _hostname + ' ' + 'ansible_ssh_host=' + _ip + ' ' + 'ansible_ssh_port=' + _port

# transfer resouces.yaml to /etc/ansible/hosts
def _transfer(file=''):
	_hostlist = _read_yaml(file=file)
	_ansible_str = [ item['nodename']+";"+item['hostname'] for item in _hostlist ]
	ansible_host = [ _format_str(item) for item in _ansible_str ]
	return ansible_host

# distinct servers by regular ect_hostname
def _match_ect_hostname(hostname=''):
	pattern = r'^(([a-zA-Z]+)-([a-zA-Z]+)-([a-zA-Z0-9]+))$'
	return re.match(pattern, hostname, re.I)

# generate hosts for ansible
def _generate_hostfile(hostlist=[]):
	group_dict = {}
	for item in hostlist:
		_hostname = item.split()[0]
		if _match_ect_hostname(_hostname):
			_group = _hostname.split('-')[1]
			group_dict.setdefault(_group,[]).append(item)
		else:
			group_dict.setdefault('others',[]).append(item)

	with open('ansible_host', 'w') as f_write:
		for key in group_dict:
			f_write.writelines('['+key+']')
			f_write.writelines('\n')
			for item in group_dict[key]:
				f_write.writelines(item)
				f_write.writelines('\n')
			f_write.writelines('\n')
		f_write.close()

if __name__ == "__main__":
	ansible_host_list = _transfer(file='resources.yaml')
	_generate_hostfile(ansible_host_list)

	#print("Generate /etc/ansible/host succesfully.")