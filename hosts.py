# host_ip = [
#     '50.113.255.36',
#     '50.113.255.37',
#     '50.113.255.38',
#     '50.113.255.39',
#     '50.113.255.40',
#     '50.113.255.21',
#     '50.113.255.22',
#     '50.113.255.23',
#     '50.113.255.24',
#     '50.113.255.25',
#     '50.113.255.26',
#     '50.113.255.27',
#     '50.113.255.28',
#     '50.113.255.44',
#     '50.113.255.45',
#     # '50.113.255.46',  windows
#     '50.113.255.29',
#     '50.113.255.30',
#     '50.113.255.31',
#     '50.113.255.32',
#     '50.113.255.33',
#     '50.113.255.34',
#     '50.113.255.35',
#     '50.113.255.41',
#     '50.113.255.42',
#     '50.113.255.43'
#
#]

host_ip = '192.168.1.1-20'
# host_ip = ['192.168.1.1','192.168.1.2']
#你可以使用两种不同的方法批量输入IP地址

#连接信息
host_port = 52013
host_user = 'root'
host_password = "123456"
command = "systemctl status firewalld | grep Active | awk '{print $3}' | cut -f1 -d ')' | cut -f2 -d '('"
write_filename = '结果.txt'

# 防火墙
firewalld_status = "systemctl status firewalld | grep Active | awk '{print $3}' | cut -f1 -d ')' | cut -f2 -d '('"
firewalld_enable_status = "systemctl list-unit-files | grep firewalld | awk '{print $2}'"
firewalld_disabled = "systemctl disable firewalld && systemctl list-unit-files | grep firewalld | awk '{print $2}'"
firewalld_stop = "systemctl stop firewalld && systemctl status firewalld | grep Active | awk '{print $3}' | cut -f1 -d ')' | cut -f2 -d '('"

# 端口
port_alter = "sed -i 's/#Port 22/Port 22/g' /etc/ssh/sshd_config && echo 'alter OK'"
port_add = "echo 'Port 52013' >> /etc/ssh/sshd_config && echo 'add OK'"
port_rest = "systemctl restart sshd && && echo 'restart sshd OK'"
reboot = "reboot && echo 'system is reboot'"
