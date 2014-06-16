#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author Kim Kong  kongqingzhang@gmail.com
import pdb
import sys
from GGC import  ggc_set,facebook_set,twitter_set
import threading
import time
import socket
import ping
import requests
import re
from requests.exceptions import SSLError, Timeout


try:
    set_name = sys.argv[1]
    if re.match(r'[0-9]+', set_name) is not None:
        set_name = 'google'
        max_ping_value = sys.argv[1]
except IndexError:
    set_name = 'google'
try:
    max_ping_value = sys.argv[2]
except IndexError:
    max_ping_value = False

dict_name_set = {
    'google': ggc_set,
    'facebook': facebook_set,
    'twitter': twitter_set}

init_threading_count = threading.activeCount()
ipList = []
pyver2 = sys.version < '3'

def get_host(ip_addr):
    """
    test ip is connected to port 443
    """

    try:
        headers=''
        requests.get('https://' + ip_addr, timeout=2)
        return -2
    except SSLError as e:
        name_list = []
        ping_list = ping.quiet_ping(ip_addr)
        ping_artt = ping_list[2]
        ping_lost = ping_list[0]
        ping_value = 'delay: %.5sms, lost: %s%%' % (ping_artt, ping_lost)
        if "', '" in str(e):
            name_list = str(e).split("', '")
            name_list[0] = name_list[0].split("'")[-1]
            name_list[-1] = name_list[-1].split("'")[0]
            # print ip_addr + '\n'
            return [name_list, ip_addr, ping_value]
        elif 'match' in str(e):
            temp_list = str(e).split("'")
            name_list.append(temp_list[-2])
            # print ip_addr
            return [name_list, ip_addr, ping_value]
        return e
    except Timeout:
        # print ip_addr + ' time out'
        return -3
    except Exception as e:
        # print ip_addr + '\n' + str(e)
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
            # yield {'name': 'appengine', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['appengine', temp_list[1], temp_list[2]]
        if 'appspot' in str(temp_list[0]):
            # yield {'name': 'appspot', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['appspot', temp_list[1], temp_list[2]]
        if 'android.com' in (temp_list[0]):
            # yield {'name': 'android', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['android', temp_list[1], temp_list[2]]
        if 'ggpht' in str(temp_list[0]):
            # yield {'name': 'ggpht', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['ggpht', temp_list[1], temp_list[2]]
        if 'gstatic.com' in str(temp_list[0]):
            # yield {'name': 'gstatic', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['gstatic', temp_list[1], temp_list[2]]
        if 'googleapis' in str(temp_list[0]):
            # yield {'name': 'googleapis', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['googleapis', temp_list[1], temp_list[2]]
        if 'talk' in str(temp_list[0]):
            # yield {'name': 'talk', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['talk', temp_list[1], temp_list[2]]
        if 'googleusercontent' in str(temp_list[0]):
            # yield {'name': 'googleusercontent', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['googleusercontent', temp_list[1], temp_list[2]]
        if 'googlecode' in str(temp_list[0]):
            # yield {'name': 'googlecode', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['', temp_list[1], temp_list[2]]
        if 'googlesource' in str(temp_list[0]):
            # yield {'name': 'googlesource', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['googlesource', temp_list[1], temp_list[2]]
        if 'googlevideo' in str(temp_list[0]):
            # yield {'name': 'googlevideo', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['googlevideo', temp_list[1], temp_list[2]]
        if 'googlegroups' in str(temp_list[0]):
            # yield {'name': 'googlegroups', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['', temp_list[1], temp_list[2]]
        if '*.google.com' in temp_list[0] or 'google.com' in temp_list[0]:
            # yield {'name': 'google', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['google', temp_list[1], temp_list[2]]
        if '*.facebook.com' in temp_list[0] or 'facebook.com' in temp_list[0]:
            # yield {'name': 'facebook', 'ip': temp_list[1], 'ping': temp_list[2]}
            yield ['facebook', temp_list[1], temp_list[2]]
        if 'fbcdn' in str(temp_list[0]):
            # yield {'name': 'fbcdn'}
            yield ['fbcdn', temp_list[1], temp_list[2]]
        if 'fbsbx' in str(temp_list[0]):
            yield ['fbsbx', temp_list[1], temp_list[2]]
        if 'akamai' in str(temp_list[0]):
            yield ['twitter', temp_list[1], temp_list[2]]
        # yield {'name': 'all', 'ip': temp_list[1], 'ping': temp_list[2]}



def to_config(input_iter):
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
            config.add_section(m[0])
        except DuplicateSectionError:
            pass
        if max_ping_value:
            if m[0] == 'google' and int(m[2]) < int(max_ping_value): # ping < 100
                # print int(m['ping']) < 100
                google_list.append(m[1])
        else:
            if m[0] == 'google':
                # print True
                google_list.append(m[1])
        config.set(m[0], m[1], m[2])
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
    get_ip(net_address(dict_name_set[set_name]))
    to_config(group_ip(ipList))


if __name__ == '__main__':
    start_time = time.clock()
    global lock
    lock = threading.Lock()
    run_pro()
    end_time = time.clock()
    t = str(end_time - start_time)
    print('run %s s' % t)


