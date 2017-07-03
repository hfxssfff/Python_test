#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import socket
import threading
from socket import *

openNum = 0
threads = []
targetPorts = []

parser = argparse.ArgumentParser()
parser.add_argument('-H',dest='targetHost',type=str,help='目标主机')
#parser.add_argument('-P',dest='targetPorts',type=int,nargs='+',help='目标端口')
args = parser.parse_args()
targetHost = args.targetHost.strip()
#targetPorts = args.targetPorts
if targetHost == None:
    print('\n你必须传入一个主机名或地址及端口号')
    exit(0)
#测试命令行传参--------------
print(targetHost)
#---------------------------


def connScan(targetHost,targetPort):
    global openNum
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((targetHost,targetPort))
        print('%s 端口开放' % str(targetPort))
        openNum = openNum + 1
        lock.acquire()
        print('%d/TCP open' % targetPort)
        lock.release()
        connSkt.close()
    except:
        pass
        #print('%s端口关闭' % targetPort)

def portScan(targetHost,targetPort):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('Can not resolve %s: Unknow host' % targetHost)
        return
    connScan(targetHost,targetPort)

def main():
    for Ports in range(1,1081):
        targetPorts.append(Ports)
    setdefaulttimeout(1)
    for p in targetPorts:
        t = threading.Thread(target=portScan,args=(targetHost,p))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('端口测试完成,有%s个开放' % str(openNum))

if __name__ == '__main__':
    main()
