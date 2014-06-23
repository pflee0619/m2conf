#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author Kim Kong  kongqingzhang@gmail.com
import sys
from GGC import  ggc_set,facebook_set,twitter_set
import threading
import time
import ping
import requests
import re
from requests.exceptions import SSLError, Timeout



dict_name_set = {
    'google': ggc_set,
    'facebook': facebook_set,
    'twitter': twitter_set}

init_threading_count = threading.activeCount()
ipList = []
pyver2 = sys.version < '3'
usage = '''
------------------------
-h, --help: get help
sudo python set_goagent.py:  get google host file and google_hk/talk iplist
sudo python set_goagent.py 100: get google host file, and google_hk/talk iplist ping delay<100
sudo python set_goagent.py facebook: get facebook host file

if you are windows users, need admin open the cmd/command program, not need input sudo command.
----------------------------
'''


"""
get argv message
"""

max_ping_value = None
set_name = 'google'
if len(sys.argv) == 2:
    set_name = sys.argv[1]
    if re.match(r'[0-9]+', set_name) is not None:
        set_name = 'google'
        max_ping_value = sys.argv[1]


def get_host(ip_addr):
    """
    test ip is connected to port 443 and get ping message
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
        ping_value = ['delay: %.5sms, lost: %s%%' % (ping_artt, ping_lost), ping_artt, ping_lost]
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

def get_ip(ip_s, thread_limit=None, timeout=0.01):
    """
    read ip_set it is changed by net_address function, then requests.get and ping ip, if access successfully, append it to ipList.
    """
    # print ip_s
    ip_addr_list=[]
    lock = threading.Lock()
    thread_pool = []
    for ip_tuple in ip_s:
        # print ip_tuple
        for nu in range(ip_tuple[1], ip_tuple[2]):
            ip = ip_tuple[0] + '.' + str(nu)
            ip_addr_list.append(ip)

    while ip_addr_list or thread_pool:
        while ip_addr_list and (thread_limit is None or len(thread_pool) < thread_limit):
            ip = ip_addr_list.pop()
            get_thread = GetHost(ip, lock)
            get_thread.start()
            thread_pool.append(get_thread)

        print(threading.activeCount() - init_threading_count, 'threading working...')


        for get_thread in thread_pool:
            get_thread.join(timeout=timeout)
            if not get_thread.is_alive():
                thread_pool.remove(get_thread)

        # while threading.activeCount() > init_threading_count:
        #     pass
    print("all threads are done")

def group_ip(ip_ss):
    """
    group ip it can be accessed
    """
    for temp_list in ip_ss:
        if 'appengine' in str(temp_list[0]):
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
    :Parameters
        :input_iter: will change the iter to config file
    :Variable
        :m[0]:  filter host
        :m[1]:  ip_addr
        :m[2]:  ping list
        :m[2][0]: "delay: 418.6ms, lost: 0%"
        :m[2][1]: ping_artt  avg ping delay, filter lower ping delay on line 172

    """
    google_list = []
    talk_list = []
    try:
        import ConfigParser
        from ConfigParser import DuplicateSectionError
        config = ConfigParser.RawConfigParser()
    except ImportError:
        import configparser  # python 3
        from configparser import DuplicateSectionError
        config = configparser.RawConfigParser()
    for m in input_iter:
        try:
            config.add_section(m[0])
        except DuplicateSectionError:
            pass
        config.set(m[0], m[1], m[2][0])
        if max_ping_value and m[2][1] and int(m[2][1]) < int(max_ping_value) or not max_ping_value and m[2] == 0:
            if m[0] == 'appengine': # ping < 100
                google_list.append(m[1])
            if m[0] == 'talk':
                talk_list.append(m[1])
    config.add_section('iplist')
    config.set('iplist', 'google_hk', '|'.join(google_list))
    config.set('iplist', 'google_talk', '|'.join(talk_list))
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
            if temp * n <= ip_number < temp * (n + 1):
                return [temp * n, temp * (n + 1)]
            n += 1
    for net in net_address_s:
        netlist = net.split('/')
        if int(netlist[1]) == 24:
            yield (netlist[0][:netlist[0].rindex('.')], 0, 255)
        elif int(netlist[1]) > 24:
            m = 32 - int(netlist[1])
            ip_number = int(netlist[0].split('.')[3])
            ip_number_list = get_ip_number_list(m, ip_number)
            yield (netlist[0][:netlist[0].rindex('.')], ip_number_list[0], ip_number_list[1])
        elif 16 <= int(netlist[1]) < 24:
            m = 24 - int(netlist[1])
            ip_number = int(netlist[0].split('.')[2])
            ip_number_list = get_ip_number_list(m, ip_number)
            for m in range(ip_number_list[0], ip_number_list[1]):
                yield ('.'.join(netlist[0].split('.')[:2] + [str(m)]), 0,255)
        else:
            pass    # < 16  do nothing


class GetHost(threading.Thread):

    def __init__(self, ip_address, lock):
        threading.Thread.__init__(self)
        self.ip_address = ip_address
        self.lock = lock

    def run(self):
        a = get_host(self.ip_address)
        try:
            if isinstance(a, list):
                ipList.append(a)
        except:
            pass


    def stop(self):
        pass




def run_pro():
    """
    """
    get_ip(net_address(dict_name_set[set_name]), thread_limit=500)
    to_config(group_ip(ipList))


if __name__ == '__main__':
    start_time = time.clock()
    if len(sys.argv) == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print usage
        sys.exit(0)
    run_pro()
    end_time = time.clock()
    t = str(end_time - start_time)
    print('run %s s' % t)


