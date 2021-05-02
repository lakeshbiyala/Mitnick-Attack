lfrom scapy.all import *

ip = IP(src="10.0.2.4", dst="10.0.2.5")
tcp = TCP(sport=1023, dport=514, flags="S", seq=778933536)

pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
