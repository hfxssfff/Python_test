import argparse
import nmap

nmScan = nmap.PortScanner()
phost = '*'
nmScan.scan(phost,'22')
print(nmScan.scaninfo())
#state = nmScan[targetHost]['tcp'][int(targetPort)]['state']
#print('[*]' + targetHost + ' tcp/' + targetPort + ' ' + state)
print('[*]' + phost + ' tcp/' + '22' + ' ' + 'State:%s' % nmScan[phost]['tcp'][int('22')])
