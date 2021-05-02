from scapy.all import *



ip = IP(src="10.0.2.4", dst="10.0.2.5")

tcp = TCP(sport=9091, dport=514, flags="SA", seq=2390674446)



pkt = ip/tcp

ls(pkt)

send(pkt, verbose=0)
