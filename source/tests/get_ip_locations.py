#!/usr/bin/env python

''' 
name: mydomaintrace
author: JetChars (Cai Wenjie)
date: 2016.4.21
dependency: dnspython
'''

import urllib
import socket
import sys
import re
import time
import json
import os
import socket


def get_location(ipaddr):
    '''get root name server list
    return: a list of str list'''
    if not re.match('^([0-9]{1,3}\.){3,3}[0-9]{1,3}$', str(ipaddr)):
        return None
    result = None
    while not result:
        try:
            page = urllib.urlopen("http://ip.netease.com/service/getipinfo?ip="+ipaddr)
            result = page.read()
        except (socket.error, EOFError, IOError):
            continue
        finally:
            time.sleep(0.2)
            page.close()
    return result

def str_location(res):
    '''return None'''
    if not res:
        print "|  |  |  |  |  |  |"
        return
    result = json.loads(res)
    for item in ["continent", "country", "subdivisions", "city", "county", "isp"]:
        print result["data"][item]["names"]["zh_CN"], "|",
    print result["data"]["location"]["org"]

def print_locations():
    querys = []
    mtrinfo = os.popen("mtr -w "+sys.argv[1])
    mtrinfo.readline().strip()
    print mtrinfo.readline().strip()
    for item in mtrinfo.readlines():
        line = item.strip()
        querys.append(line.split()[1])
        print line
    for item in querys:
        print item, "|",
        str_location(get_location(item))

if __name__ == '__main__':

    # # check args
    # if len(sys.argv) == 1:
    #     print "ip addr required"
    #     sys.exit(0)
    # # if "-t", start auto tests
    # if sys.argv[1] == '-t':
    #     pass
    # else:
    assert socket.inet_aton("192.169.4.45")
    ping100 = os.popen("ping -c 100 -i 0.01 -q 220.181.30.53").read()
    print ping100
    # search ipaddr, package loss and avg latency
    ptn = re.compile(r'.+?([\d.]+).+?([\d.]+)% packet loss.+?[\d.]+/([\d.]+)/[\d.]+/[\d.]+', re.DOTALL)
    print ptn.findall(ping100)
