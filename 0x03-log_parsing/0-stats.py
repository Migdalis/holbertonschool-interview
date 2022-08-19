#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """
import sys


def print_report(size, status):
    """ Print the statistics """
    print("File size: {}".format(size))
    for code, mnt in status.items():
        if mnt > 0:
            print("{}: {}".format(code, mnt))


if __name__ == '__main__':
    """ Start the reads """
    status_code = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                   '404': 0, '405': 0, '500': 0}
    f_size = 0
    l_reads = 0

    try:
        for line in sys.stdin:
            s_line = line.split()
            l_reads += 1
            if len(s_line) == 9:
                if s_line[-2] in status_code:
                    status_code[s_line[-2]] += 1
                f_size += int(s_line[-1])
            if l_reads % 10 == 0:
                print_report(f_size, status_code)
        print_report(f_size, status_code)
    except KeyboardInterrupt:
        print_report(f_size, status_code)
        raise
