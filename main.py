from class_file import links as l, write as w
import hosts,os


def main():
    while True:
        print("-switch a number--------------------------------------------------")
        print("-1.show firewalld stop/start")
        print("-2.show firewalld enable/disable")
        print("-3.disabled firewalld")
        print("-4.stop firewalld")
        print("-5.alter port")
        print("-6.add port")
        print("-7.restart port")
        print("-------------------------------------------------------------------")
        switch = input("input:")
        if switch == "1":
            command = hosts.firewalld_status
        elif switch == '2':
            command = hosts.firewalld_enable_status
        elif switch == '3':
            command = hosts.firewalld_disabled
        elif switch == '4':
            command = hosts.firewalld_stop
        elif switch == '5':
            command = hosts.port_alter
        elif switch == '6':
            command = hosts.port_add
        elif switch == '7':
            command = hosts.port_res
        else:
            print("Error,you not switch")
            exit(1)
        print('wait a moment...')
        read_info = l.links(command)
        w.write(read_info)
        print('完成,请打开txt查看结果')

if __name__ == '__main__':
    main()
