#!/usr/bin/env python
#coding:utf-8

''' 
name: link|monitor.py
author: JetChars (Cai Wenjie)
date: 2016.4.21
python version: 2.7.6
'''

import socket
import sys
import re
import os


def is_link_health(ipaddr):
    '''check link health
    return: bool'''

    assert socket.inet_aton(ipaddr)
    retry = 0
    while True and retry < 3:
        ping100 = os.popen("ping -c 100 -i 0.01 -q " + ipaddr).read()
        # print ping100
        # search ipaddr, package loss and avg latency
        ptn = re.compile(r'.+?([\d.]+).+?([\d.]+)% packet loss.+?[\d.]+/([\d.]+)/[\d.]+/[\d.]+',
                         re.DOTALL)
        res = ptn.findall(ping100)
        if len(res) == 1:
            return float(res[0][1]) <= 10.0 and float(res[0][2]) <= 50.0
        else:
            retry += 1

def get_link_status(ipaddr):
    '''collect link status w/ `mtr -w`
    return: str'''

    assert socket.inet_aton(ipaddr)
    mtr_retry = 0
    link_status = None
    while not link_status and mtr_retry < 3:
        link_status = os.popen("mtr -w " + ipaddr).read()
    return link_status

def log_append(file_path, log_str):
    '''saving to log
    return: None'''

    with open(file_path, 'a') as log_file:
        log_file.write(log_str)


if __name__ == '__main__':

    # check args
    if len(sys.argv) == 1:
        print "ip addr required"
        sys.exit(1)
    else:
        pass
        # ptn = re.compile(r'(?:(?:(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2})\.){3,3}(?:25[0-5]|2[0-4]\d|1\d\d|\d{1,2}))', re.DOTALL)
        # print ptn.findall("220.181.30.255dsafasdfasdfs220.181.30.255")
        # assert socket.inet_aton(sys.argv[1])
        # if not is_link_health(sys.argv[1]):
        #     log_append("/var/log/icmp_to_" + sys.argv[1] + ".log", get_link_status(sys.argv[1]))
    
        
