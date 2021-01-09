from hosts import write_filename as wf


def write(ret):
    file = open(wf, 'w')
    for read_info in ret:
        file.write(read_info)
    file.close()
    print("exit 0 is Ok--------------------------------------")
