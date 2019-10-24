
from scapy.all import RandMAC,RandIP,Ether,IP,sendp #针对性的导入函数,避免加载慢
import sys

iface = 'ens33'
if len(sys.argv) >= 2:
    iface = sys.argv[1]

packet = Ether(src=RandMAC(),dst=RandMAC())/IP(src=RandIP(),dst=RandIP())
sendp(packet,iface=iface,loop=1) #loop 自带的循环发包
