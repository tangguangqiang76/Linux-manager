import hosts, re
from class_file import ssh_link


def links(command):
    ip = str_convert_list()
    ret = []
    for p in ip:
        host_link = [p, hosts.host_port, hosts.host_user, hosts.host_password]
        ret.append(ssh_link.ssh_command(host_link, command))
    return ret


def str_convert_list():
    if isinstance(hosts.host_ip, list):
        return hosts.host_ip
    elif isinstance(hosts.host_ip, str):
        x = re.compile(r'(([0-9]?|1\d\d|2[0-4]\d|25[0-5])\.){3}')
        start = re.search(x, hosts.host_ip)
        start = start.group(0)
        swap = hosts.host_ip.replace(start, '')
        swap = swap.split('-')
        min = swap[0]
        max = swap[1]
        print(min,max,swap)
        ret = []
        for number in range(int(min), int(max)+1):
            swap = start + str(number)
            ret.append(swap)
        return ret
    else:
        ret = 'Error'
        return ret