# code from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

import socket
import time
import threading
import sys
import re
import urllib.request

service = r''
service_t = r'[a-z]+'

teste = '''
ftp-data            20         udp    File Transfer [Default Data] [Jon_Postel]                                          [Jon_Postel]
ftp-data            20        sctp    FTP                          [Randall_Stewart]                                     [Randall_Stewart]                                                                   [RFC4960]
ftp                 21         tcp    File Transfer Protocol       [Jon_Postel]                                          [Jon_Postel]                                                                        [RFC959]                                                             Defined TXT keys: u=<username> p=<password> path=<path>
                                      [Control]
ftp                 21         udp    File Transfer Protocol       [Jon_Postel]                                          [Jon_Postel]                                                                        [RFC959]                                                             Defined TXT keys: u=<username> p=<password> path=<path>
                                      [Control]
ftp                 21        sctp    FTP                          [Randall_Stewart]                                     [Randall_Stewart]                                                                   [RFC4960]                                                            Defined TXT keys: u=<username> p=<password> path=<path>
ssh                 22         tcp    The Secure Shell (SSH)    '''


teste_t = "ssh                 22         tcp    The Secure Shell (SSH)   "

iana_well_known = urllib.request.urlopen('https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt').read().decode("UTF-8")


def find_service(port):
   return ( re.match( r'(.*?)([a-z-A-Z-]*)(( +)({})( *)(tcp|udp)+)  '.format(port), iana_well_known, re.M|re.I|re.DOTALL).group(2))




print(find_service(443))

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
         s.sendto(b"Hello, Server", (t_IP, port))
         try:
            data, server = s.recvfrom(1)
            print(data)
            #print(port, 'is open')
         except Exception as e:
            pass
      else:
         con = s.connect((t_IP, port))
         with print_lock:
            print(port, 'is open service:', find_service(port))
            try:
               matchObj = re.match(service, iana_well_known)
               print(matchObj)
            except Exception as e:
               print(e)
            
         con.close()
   except Exception as e:
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