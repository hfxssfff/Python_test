#coding:utf-8
import dpkt
import socket
from dpkt import *
DesIp = '120.25.86.29'

def filterIp(scr,dst,DesIp):
    if (scr==Ip) or (dst==Ip):
        print('[+] Scr: ' + scr+ ' --> Dst: ' + dst)
    print('No result')

def mac_addr(address):
    """Convert a MAC address to a readable/printable string

       Args:
           address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
       Returns:
           str: Printable/readable MAC address
    """
    return ':'.join('%02x' % compat_ord(b) for b in address)
def printpcap(pcap):
    for (ts,buf) in pcap:
        # Unpack the Ethernet frame
        eth = ethernet.Ethernet(buf)
        mac_scr = eth.src
        mac_dst = eth.dst
        print('Ethernet Frame:',mac_addr(mac_scr),'--->',mac_addr(mac_dst),eth.type)
        ip = eth.data
        if ip != None:
            scr = socket.inet_ntoa(ip.src)
        	dst = socket.inet_ntoa(ip.dst)
        	print('[+] Scr: ' + scr+ ' --> Dst: ' + dst)
        else:
            print('NO RESULT')
def main():
    f = open('..\\..\\Package\\all.pcap','rb')
    pacp = pcap.Reader(f)
    print('OK')
    printpcap(pacp)

main()
