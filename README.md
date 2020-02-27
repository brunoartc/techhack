## 1.1.a

```console
bruno@bruno-340XAA-350XAA-550XAA:~/Documents/techhack$ fping -g 192.168.43.1/24 2> /dev/null | grep "alive"
192.168.43.1 is alive
192.168.43.106 is alive
192.168.43.190 is alive
192.168.43.248 is alive
```

```console
192.168.43.106 is alive
```

## 1.1.b

```sh
telnet 192.168.43.248 21
```


```console
bruno@bruno-340XAA-350XAA-550XAA:~/Documents/techhack$ telnet 192.168.43.248 21
Trying 192.168.43.248...
Connected to 192.168.43.248.
Escape character is '^]'.
220 ProFTPD 1.3.5 Server (Debian) [::ffff:192.168.43.248]
```

## 1.1.c

```log
# Nmap 7.80 scan initiated Thu Feb 27 16:08:02 2020 as: nmap -sS -A -o - 192.168.43.248
Nmap scan report for debian (192.168.43.248)
Host is up (0.017s latency).
Not shown: 994 closed ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         ProFTPD 1.3.5
22/tcp  open  ssh         OpenSSH 6.7p1 Debian 5+deb8u7 (protocol 2.0)
| ssh-hostkey: 
|   1024 38:1c:57:f5:7f:71:8f:b8:84:96:41:75:37:a2:d1:d8 (DSA)
|   2048 28:43:35:c6:a1:d1:9b:59:0e:76:cb:c2:fb:eb:31:78 (RSA)
|   256 ad:98:ca:f7:3a:20:cc:83:3f:df:c4:2c:3c:70:3a:45 (ECDSA)
|_  256 88:ff:f9:47:b3:1e:cf:56:a7:b5:c8:98:d5:38:13:63 (ED25519)
80/tcp  open  http        Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Site doesn't have a title (text/html).
111/tcp open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          35308/tcp   status
|   100024  1          49773/udp   status
|   100024  1          54985/tcp6  status
|_  100024  1          59954/udp6  status
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.2.14-Debian (workgroup: WORKGROUP)
MAC Address: 1C:1B:B5:06:ED:16 (Intel Corporate)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 59m58s, deviation: 1h43m55s, median: -2s
|_nbstat: NetBIOS name: DEBIAN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.2.14-Debian)
|   Computer name: debian
|   NetBIOS computer name: DEBIAN\x00
|   Domain name: \x00
|   FQDN: debian
|_  System time: 2020-02-27T16:08:19-03:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2020-02-27T19:08:19
|_  start_date: N/A

TRACEROUTE
HOP RTT      ADDRESS
1   17.29 ms debian (192.168.43.248)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Feb 27 16:08:22 2020 -- 1 IP address (1 host up) scanned in 19.73 seconds
```


## 1.1.d Program

# Usage

> you can use the proggram passing the target IP as the first arg and the protocol as second arg

```sh
python3 main.py 127.0.0.1 UDP
```
