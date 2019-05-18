#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import argparse
import subprocess as sp
import shlex

def meminfo(pkg):
    ret = []
    for line in str(sp.check_output(shlex.split('adb shell dumpsys meminfo'))).split('\\n'):
        line = line.strip()
        if pkg in line:
            info = {'mem': line.split(':')[0], 'pkg': line.split()[1]}
            if info not in ret:
                ret.append(info)
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Description')
    parser.add_argument('time', help="Time to watch performance", type=int)

    args = parser.parse_args()

    for _ in range(args.time):
        print(meminfo('api'))
        time.sleep(1)
