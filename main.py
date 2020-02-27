# code from https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_network_scanner.htm

import socket
import time
import threading
import sys

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
         s.sendto("TORANJA", (t_IP, port))
         try:
            data, server = clientSocket.recvfrom(1024)
            print(port, 'is open')
         except:
            pass
      else:
         con = s.connect((t_IP, port))
      with print_lock:
         print(port, 'is open')
      con.close()
   except:
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