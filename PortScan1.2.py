import argparse
import nmap

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-H',dest='targetHost',type=str,help='目标主机')
    parser.add_argument('-P',dest='targetPort',type=str,help='目标端口')
    args = parser.parse_args()
    targetHost = args.targetHost
    targetPorts = str(args.targetPort).split(',')
    if (targetHost == None) or (targetPorts[0] == None):
        print('\n你必须传入一个主机名或地址及端口号')
        exit(0)
    #扫描开始--------------------
    for targetPort in targetPorts:
        nmapScan(targetHost,targetPort)
    #---------------------------
def nmapScan(targetHost,targetPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(targetHost,targetPort)
    state = nmScan[targetHost]['tcp'][int(targetPort)]['state']
    print('[*]' + targetHost + ' tcp/' + targetPort + ' ' + state)
if __name__ == '__main__':
    main()
