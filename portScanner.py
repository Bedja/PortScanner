#!/usr/bin/python

import sys
from socket import *
from termcolor import colored
import argparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(colored(f'{tgtPort} TCP open', 'green'))
    except:
        print(colored(f'{tgtPort} Closed', 'red'))

    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"Unknown Host {tgtHost}")
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(colored(f'[+] Scan Results For {tgtName[0]}', 'blue'))
    except:
        print(colored(f'[+] Scan Results For: {tgtIP}', 'blue'))
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = argparse.ArgumentParser(description='Usage of program: -H <target host> -P <target port>')
    parser.add_argument('-H', dest='tgtHost', type=str, help='sepcify your target Host')
    parser.add_argument('-P', dest='tgtPort', type=str, help='specify target ports seperated by comma')
    options = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
