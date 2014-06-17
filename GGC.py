#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mhohai, Kim Kong'


"""
net address is from http://bgp.he.net/AS15169#_prefixes
"""

ggc_set = [
    # '1.179.253.0/24',   # TH
    # '1.179.252.0/24',
    # '1.179.251.0/24',
    # '1.179.250.0/24',
    # '1.179.249.0/24',
    # '1.179.248.0/24',

    # '8.6.48.0/21',
    # '8.8.4.0/24',   # AS15169
    # '8.8.8.0/24',
    # '8.15.202.0/24',
    # '8.34.208.0/21',
    # '8.34.216.0/21',
    # '8.35.192.0/21',
    # '8.35.200.0/21',

    # '12.216.80.0/24',


    # '23.236.48.0/20 ',
    # '23.251.128.0/19',
    # '23.255.128.0/17',
    # '23.228.128.0/18',

    # '64.233.160.0/24',
    # '64.233.164.0/24',
    # '64.233.165.0/24',
    # '64.233.168.0/24',
    # '64.233.171.0/24',
    # '64.233.172.0/24',


    # '66.102.0.0/20',
    # '66.102.2.0/24',
    # '66.102.3.0/24',
    # '66.102.4.0/24',

    # '66.249.64.0/24',
    # '66.249.65.0/24',
    # '66.249.66.0/24',
    # '66.249.67.0/24',
    # '66.249.69.0/24',
    # '66.249.70.0/24',
    # '66.249.72.0/24',
    # '66.249.73.0/24',
    # '66.249.74.0/24',
    # '66.249.76.0/24',
    # '66.249.77.0/24',
    # '66.249.78.0/24',
    # '66.249.79.0/24',
    # '66.249.80.0/24',
    # '66.249.81.0/24',
    # '66.249.83.0/24',
    # '66.249.84.0/24',
    # '66.249.85.0/24',
    # '66.249.88.0/24',
    # '66.249.89.0/24',
    # '66.249.90.0/24',
    # '66.249.91.0/24',
    # '66.249.92.0/24',
    # '66.249.93.0/24',

    # '70.32.130.0/24',
    # '70.32.131.0/24',
    # '70.32.132.0/24',
    # '70.32.133.0/24',
    # '70.32.144.0/24',
    # '70.32.148.0/23',
    # '70.32.158.0/24',

    # '72.14.192.0/18',
    # '72.14.208.0/23',
    # '72.14.225.0/24',
    # '72.14.228.0/24',
    # '72.14.244.0/23',

    # '74.125.0.0/16',
    # '74.125.16.0/24',
    # '74.125.17.0/24',
    # '74.125.18.0/24',
    # '74.125.19.0/24',
    # '74.125.20.0/24',
    '74.125.21.0/24',
    '74.125.22.0/24',
    '74.125.23.0/24',
    '74.125.24.0/24',
    # '74.125.25.0/24',
    # '74.125.26.0/24',
    # '74.125.28.0/24',
    # '74.125.29.0/24',
    # '74.125.30.0/24',
    # '74.125.31.0/24',
    # '74.125.36.0/24',
    # '74.125.37.0/24',
    # '74.125.40.0/24',
    # '74.125.41.0/24',
    # '74.125.42.0/24',
    # '74.125.43.0/24',
    # '74.125.45.0/24',
    # '74.125.54.0/23',
    # '74.125.58.0/24',
    # '74.125.63.0/24',
    # '74.125.68.0/24',
    # '74.125.70.0/24',
    # '74.125.72.0/24',
    # '74.125.73.0/24',
    # '74.125.74.0/24',
    # '74.125.76.0/24',
    # '74.125.88.0/23',
    # '74.125.90.0/23',
    # '74.125.116.0/24',
    # '74.125.117.0/24',
    # '74.125.118.0/24',
    # '74.125.119.0/24',
    # '74.125.121.0/24',
    # '74.125.122.0/24',
    # '74.125.128.0/24',
    # '74.125.129.0/24',
    # '74.125.130.0/24',
    # '74.125.131.0/24',
    # '74.125.132.0/24',
    # '74.125.135.0/24',
    # '74.125.136.0/24',
    # '74.125.137.0/24',
    # '74.125.138.0/24',
    # '74.125.142.0/24',
    # '74.125.143.0/24',
    # '74.125.176.0/24',
    # '74.125.177.0/24',
    # '74.125.178.0/24',
    # '74.125.180.0/24',
    # '74.125.181.0/24',
    # '74.125.182.0/24',
    # '74.125.183.0/24',
    # '74.125.184.0/24',
    # '74.125.185.0/24',
    # '74.125.186.0/24',
    # '74.125.187.0/24',
    # '74.125.188.0/24',
    # '74.125.189.0/24',
    # '74.125.190.0/24',
    # '74.125.191.0/24',
    # '74.125.192.0/24',
    # '74.125.193.0/24',
    # '74.125.194.0/24',
    # '74.125.195.0/24',
    # '74.125.196.0/24',
    # '74.125.198.0/24',
    # '74.125.200.0/24',
    # '74.125.201.0/24',
    # '74.125.203.0/24',
    # '74.125.204.0/24',
    # '74.125.205.0/24',
    # '74.125.206.0/24',
    # '74.125.207.0/24',
    # '74.125.224.0/24',
    # '74.125.225.0/24',
    # '74.125.226.0/24',
    # '74.125.227.0/24',
    # '74.125.228.0/24',
    # '74.125.229.0/24',
    # '74.125.230.0/24',
    # '74.125.231.0/24',
    # '74.125.232.0/24',
    # '74.125.233.0/24',
    # '74.125.234.0/24',
    # '74.125.235.0/24',
    # '74.125.236.0/24',
    # '74.125.237.0/24',
    # '74.125.238.0/24',
    # '74.125.239.0/24',

    # '84.235.77.0/24',  #add
    # '89.207.224.0/21',

    # '103.25.178.0/24',
    # '103.246.187.0/24',

    # '107.167.160.0/19',
    # '107.178.192.0/18',
    # '107.188.128.0/17',

    # '108.59.80.0/20',
    # '108.170.192.0/18',
    # '108.177.0.0/17',

    # '111.92.162.0/24',

    # '113.197.105.0/24',
    # '113.197.106.0/24',
    # '118.174.27.0/24',
    # '118.174.26.0/24',
    # '118.174.25.0/24',
    # '118.174.24.0/24',

    # '130.211.0.0/16',
    # '142.250.0.0/16',
    # '142.251.0.0/16',
    # '146.148.0.0/17',

    # '149.3.177.0/24',
    # '149.126.86.0/24',

    # '162.216.148.0/22',
    # '162.222.176.0/21',


    # '172.217.0.0/16',
    # '172.253.0.0/16',

    # '173.194.0.0/16',
    # '173.194.32.0/24',
    # '173.194.33.0/24',
    # '173.194.34.0/24',
    # '173.194.35.0/24',
    # '173.194.36.0/24',
    # '173.194.37.0/24',
    # '173.194.38.0/24',
    # '173.194.39.0/24',
    # '173.194.40.0/24',
    # '173.194.41.0/24',
    # '173.194.42.0/24',
    # '173.194.43.0/24',
    # '173.194.44.0/24',
    # '173.194.45.0/24',
    # '173.194.46.0/24',
    # '173.194.64.0/24',
    # '173.194.65.0/24',
    # '173.194.66.0/24',
    # '173.194.67.0/24',
    # '173.194.68.0/24',
    # '173.194.69.0/24',
    # '173.194.70.0/24',
    # '173.194.71.0/24',
    # '173.194.72.0/24',
    # '173.194.73.0/24',
    # '173.194.75.0/24',
    # '173.194.76.0/24',
    # '173.194.77.0/24',
    # '173.194.78.0/24',
    # '173.194.79.0/24',
    # '173.194.96.0/24',
    # '173.194.97.0/24',
    # '173.194.98.0/24',
    # '173.194.99.0/24',
    # '173.194.112.0/24',
    # '173.194.113.0/24',
    # '173.194.117.0/24',
    # '173.194.118.0/24',
    # '173.194.119.0/24',
    # '173.194.120.0/24',
    # '173.194.121.0/24',
    # '173.194.124.0/24',
    # '173.194.126.0/24',
    # '173.194.127.0/24',
    # '173.194.136.0/24',
    # '173.194.140.0/24',
    # '173.194.141.0/24',
    # '173.194.142.0/24',

    # '173.255.112.0/20',

    # '192.119.16.0/20',
    # '192.119.20.0/24',
    # '192.119.21.0/24',
    # '192.158.28.0/22',
    # '192.178.0.0/16',
    # '192.179.0.0/16',
    # '192.200.224.0/19',

    # '193.142.125.0/24',
    # '193.186.4.0/24',

    # '197.199.254.0/24',
    # '197.199.253.0/24',
    # '199.192.112.0/22',
    # '199.223.232.0/21',

    # '207.223.160.0/20',

    # '209.85.128.0/17',
    # '209.85.228.0/23'
    # '209.85.238.0/24',

    # '216.58.192.0/19',

    # '216.239.32.0/24',
    # '216.239.33.0/24',
    # '216.239.34.0/24',
    # '216.239.35.0/24'
    # '216.239.36.0/24'
    # '216.239.38.0/24'
    # '216.239.39.0/24'
    # '216.239.44.0/24'
    # '216.239.60.0/24'





    # '217.163.7.0/24',



]


# contain gcc_set
gcc_set2 = [
    # '64.233.160.0/19',
    # '216.239.32.0/19',
    # '70.32.128.0/19',
    # '66.249.64.0/19',


]

facebook_set = [
    # '74.119.76.0/22',
    # '69.63.184.0/21',
    # '69.63.176.0/24',
    # '69.63.176.0/21',
    # '69.171.255.0/24',
    # '69.171.240.0/20',
    # '69.171.239.0/24',
    # '69.171.224.0/20',
    # '66.220.152.0/21',
    # '66.220.144.0/21',
    # '31.13.96.0/19',
    # '31.13.87.0/24',
    # '31.13.86.0/24',
    # '31.13.85.0/24',
    # '31.13.84.0/24',
    # '31.13.83.0/24',
    # '31.13.82.0/24',
    # '31.13.81.0/24',
    # '31.13.80.0/24',
    # '31.13.79.0/24',
    # '31.13.78.0/24',
    # '31.13.77.0/24',
    # '31.13.76.0/24',
    # '31.13.75.0/24',
    # '31.13.74.0/24',
    # '31.13.73.0/24',
    # '31.13.72.0/24',
    # '31.13.71.0/24',
    # '31.13.70.0/24',
    # '31.13.69.0/24',
    # '31.13.68.0/24',
    # '31.13.66.0/24',
    # '31.13.65.0/24',
    # '31.13.64.0/24',
    '31.13.64.0/19',
    '31.13.24.0/21',
    '204.15.20.0/22',
    '199.201.64.0/22',
    '173.252.96.0/19',
    '173.252.70.0/24',
    '173.252.64.0/19',
]

twitter_set = [
    # '8.25.197.0/24',
    # '8.25.196.0/24',
    # '8.25.195.0/24',
    # '8.25.194.0/24',
    # '209.170.99.0/24',
    # '199.96.63.0/24',
    # '199.96.62.0/23',
    # '199.96.61.0/24',
    # '199.96.60.0/24',
    # '199.96.60.0/23',
    # '199.96.59.0/24',
    # '199.96.58.0/24',
    # '199.96.58.0/23',
    # '199.96.57.0/24',
    # '199.96.56.0/24',
    # '199.96.56.0/23',
    # '199.59.148.0/22',
    # '199.16.156.0/23',
    # '199.16.156.0/22',
    # '192.133.76.0/22',
    # '185.45.4.0/23',
]
