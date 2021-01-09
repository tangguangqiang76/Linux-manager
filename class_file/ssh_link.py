import paramiko


def ssh_command(hosts, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hosts[0], port=hosts[1], username=hosts[2], password=hosts[3], timeout=2)
        stdin, stdout, stderr = ssh.exec_command(command)
    except TimeoutError:
        return hosts[0] + '超时' + '\n'
    except ConnectionResetError:
        return hosts[0] + '系统为windows' + '\n'
    except Exception as e:
        return hosts[0] + ': ' + str(e) + '\n'
    info = stdout.read().decode('utf-8')
    ssh.close()
    return hosts[0] + ': ' + info
