#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auther Kim Kong  kongqingzhang@gmail.com
import pdb
import sys
from GGC import  net_address_set
import threading
import time
import socket
import ping
import requests
from requests.exceptions import SSLError, Timeout

try:
    p = sys.argv[1]
except IndexError:
    p = False

init_threading_count = threading.activeCount()
ipList = []
pyver2 = sys.version < '3'

def get_host(ip_address):
    """
    test ip is connected to port 443
    """

    try:
        headers=''
        requests.get('https://' + ip_address, timeout=2)
        return -2
    except SSLError as e:
        name_list = []
        ping_artt = ping.quiet_ping(ip_address)[2]
        if "', '" in str(e):
            name_list = str(e).split("', '")
            name_list[0] = name_list[0].split("'")[-1]
            name_list[-1] = name_list[-1].split("'")[0]
            # print ip_address + '\n'
            return [name_list, ip_address, ping_artt]
        elif 'match' in str(e):
            temp_list = str(e).split("'")
            name_list.append(temp_list[-2])
            # print ip_address
            return [name_list, ip_address, ping_artt]
        return e
    except Timeout:
        # print ip_address + ' time out'
        return -3
    except Exception as e:
        # print ip_address + '\n' + str(e)
        return -4

def get_ip(ip_s):
    """
    read 3-tuplues, get host and filter to iter, it's some bugs because I don't know  thread well
    """
    # print ip_s
    for ip_tuple in ip_s:
        for nu in range(ip_tuple[1], ip_tuple[2] + 1):
            ip = ip_tuple[0] + '.' + str(nu)
            get_thread = GetHost(ip)
            get_thread.start()
    print(threading.activeCount() - init_threading_count, 'threading working...')
    while threading.activeCount() > init_threading_count:
        pass

def group_ip(ip_ss):
    for temp_list in ip_ss:
        if 'appengine' in str(temp_list[0]):
            # yield {temp_list[1]: 'appengine'}
            yield {'name': 'appengine', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'appspot' in str(temp_list[0]):
            yield {'name': 'appspot', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'android.com' in (temp_list[0]):
            yield {'name': 'android', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'ggpht' in str(temp_list[0]):
            yield {'name': 'ggpht', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'gstatic.com' in str(temp_list[0]):
            yield {'name': 'gstatic', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googleapis' in str(temp_list[0]):
            yield {'name': 'googleapis', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'talk' in str(temp_list[0]):
            yield {'name': 'talk', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googleusercontent' in str(temp_list[0]):
            yield {'name': 'googleusercontent', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googlecode' in str(temp_list[0]):
            yield {'name': 'googlecode', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googlesource' in str(temp_list[0]):
            yield {'name': 'googlesource', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googlevideo' in str(temp_list[0]):
            yield {'name': 'googlevideo', 'ip': temp_list[1], 'ping': temp_list[2]}
        if 'googlegroups' in str(temp_list[0]):
            yield {'name': 'googlegroups', 'ip': temp_list[1], 'ping': temp_list[2]}
        if '*.google.com' in temp_list[0] or 'google.com' in temp_list[0]:
            yield {'name': 'google', 'ip': temp_list[1], 'ping': temp_list[2]}
        # yield {'name': 'all', 'ip': temp_list[1], 'ping': temp_list[2]}


def dic_to_config(input_iter):
    """
    all iter change to config file
    """
    google_list = []
    if pyver2:
        import ConfigParser
        from ConfigParser import DuplicateSectionError
        config = ConfigParser.RawConfigParser()
    else:
        import configparser
        from configparser import DuplicateSectionError
        config = configparser.RawConfigParser()
    for m in input_iter:
        try:
            config.add_section(m['name'])
        except DuplicateSectionError:
            pass
        if p:
            if m['name'] == 'google' and int(m['ping']) < int(p): # ping < 100
                # print int(m['ping']) < 100
                google_list.append(m['ip'])
        else:
            if m['name'] == 'google':
                # print True
                google_list.append(m['ip'])
        config.set(m['name'], m['ip'], m['ping'])
    config.add_section('iplist')
    config.set('iplist', 'google_hk', '|'.join(google_list))
    config.write(open('new_host_file', 'w'))

def net_address(net_address_s):
    """
    "192.168.1.0/24" net address change to tuplues ("192.168.1", 0, 255)
    """
    ipList = []
    def get_ip_number_list(m, ip_number):
        n = 0
        temp = 2 ** m
        while 1:
            if m * n <= ip_number < m * (n + 1):
                return [m * n, m * (n + 1)]
            n += 1
    for net in net_address_s:
        netlist = net.split('/')
        if int(netlist[1]) == 24:
            yield (netlist[0][:netlist[0].rindex('.')], 0, 255)
        elif 16 <= int(netlist[1]) < 24:
            m = 24 - int(netlist[1])
            ip_number = int(netlist[0].split('.')[2])
            ip_number_list = get_ip_number_list(m, ip_number)
            for m in range(ip_number_list[0], ip_number_list[1]):
                yield ('.'.join(netlist[0].split('.')[:2] + [str(m)]), 0,255)
        else:
            pass    # < 16  do nothing


class GetHost(threading.Thread):

    def __init__(self, ip_address):
        threading.Thread.__init__(self)
        self.ip_address = ip_address

    def run(self):
        a = get_host(self.ip_address)
        global lock
        try:
            lock.acquire()
            if isinstance(a, list):
                ipList.append(a)
        except:
            pass
        finally:
            lock.release()
    def stop(self):
        pass




def run_pro():
    """
    """
    #
    get_ip(net_address(net_address_set))
    dic_to_config(group_ip(ipList))
    # import ping
    # print ping.quiet_ping('www.google.com')[2]

if __name__ == '__main__':
    global lock
    lock = threading.Lock()
    run_pro()


