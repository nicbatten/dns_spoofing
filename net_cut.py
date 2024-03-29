#!/usr/bin/env python
import netfilterqueue

#iptables -I FORWARD -j NFQUEUE --queue-num 0
#this is the place where packets are included by default as they flow through the computer

#iptables -I OUTPUT -j NFQUEUE --queue-num 0
#this will capture all the outgoing packets of the current machine

#iptables -I INPUT -j NFQUEUE --queue-num 0
#this will capture all the incoming packets of the current machine

#iptables --flush
#clear out IP tables

def process_packet(packet):
    print(packet)
    #packet.accept()
    packet.drop()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()