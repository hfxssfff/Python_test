#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import socket
import threading
from socket import *
parser = argparse.ArgumentParser()
parser.add_argument('-H',dest='targetHost',type=str,help='目标主机')
#parser.add_argument('-P',dest='targetPorts',type=int,nargs='+',help='目标端口')
args = parser.parse_args()
targetHost = args.targetHost.strip()
#targetPorts = args.targetPorts
'''if (targetHost == None) or (targetPorts[0] == None):
    print('\n你必须传入一个主机名或地址及端口号')
    exit(0)'''
#测试命令行传参--------------
print(targetHost)
#---------------------------
openNum = 0
threads = []
targetPorts = []
for Ports in range(1,1025):
    targetPorts.append(Ports)

def connScan(targetHost,targetPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((targetHost,targetPort))
        lock.acquire()
        openNum+=1
        print('%d/TCP open' % targetPort)
        lock.release()
        connSkt.close()
    except:
        print('close')

def portScan(targetHost,targetPort):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('Can not resolve %s: Unknow host' % targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
    except:
        pass
    setdefaulttimeout(1)
    connScan(targetHost,targetPort)

def main():
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
