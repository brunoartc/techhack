# code from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

import socket
import time
import threading
import sys
import re
import urllib.request
from scapy.all import *



iana_well_known = urllib.request.urlopen('https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt').read().decode("UTF-8")


def find_service(port):
   return ( re.match( r'(.*?)([a-z-A-Z-]*)(( +)({})( *)(tcp|udp)+)  '.format(port), iana_well_known, re.M|re.I|re.DOTALL).group(2))


def udp_scan(target, ports):
   for port in ports:
      pkt = sr1(IP(dst=target)/UDP(sport=port, dport=port), timeout=2, verbose=0)
      if pkt == None:
         print("Open / filtered")
      else:
         if pkt.haslayer(ICMP):
            print("Closed")
         elif pkt.haslayer(UDP):
            print("Open / filtered")
         else:
            print("Unknown")
            print(pkt.summary())


try: 
    import queue
except ImportError:
    import Queue as queue


socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()


if len(sys.argv) < 2:
    raise Exception("too few arguments main.py [host]")
target = sys.argv[1]
t_IP = socket.gethostbyname(target)

def portscan(port):
   if len(sys.argv) > 2 and sys.argv[2] == "UDP":
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   else:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      if len(sys.argv) > 2 and sys.argv[2] == "UDP":
         udp_scan(t_IP, [port])
      else:
         con = s.connect((t_IP, port))
         with print_lock:
            print(port, 'is open service:', find_service(port))
            
         con.close()
   except Exception as e:
      print(e)
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = queue.Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 1000):
   q.put(worker)
   
q.join()
print('Time taken:', time.time() - startTime)