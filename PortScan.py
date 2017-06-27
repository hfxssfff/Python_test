import argparse
import threading
import socket
from socket import *
screenLock = threading.Semaphore(value=1)
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H',dest='targetHost',type=str,help='目标主机')
    parser.add_argument('-P',dest='targetPorts',type=int,nargs='+',help='目标端口')
    args = parser.parse_args()
    targetHost = args.targetHost
    targetPorts = args.targetPorts
    if (targetHost == None) or (targetPorts[0] == None):
        print('\n你必须传入一个主机名或地址及端口号')
        exit(0)
    #扫描开始--------------------
    print('连接主机' + targetHost)
    portScan(targetHost,targetPorts)
    #---------------------------
def connScan(targetHost,targetPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((targetHost,targetPort))
        connSkt.send("ViolentPython\r\n".encode())
        results = connSkt.recv(100)
        screenLock.acquire()
        print('%d/TCP open' % targetPort)
        print(str(results))
    except:
        screenLock.acquire()
        #print('%d/TCP closed' % targetPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(targetHost,targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('Can not resolve %s: Unknow host' % targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('Scan result for:' + targetName)
    except:
        print('Scan result for:' + targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        #print('ScanPort:' + str(targetPort))
        t = threading.Thread(target=connScan,args=(targetHost,targetPort))
        t.start()
if __name__ == '__main__':
    main()
