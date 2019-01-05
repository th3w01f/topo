#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import random


lmensj = ["A network port is a non-physical interface by which two machines \nwho exchange data through a specific service. \nAccording to the OSI (Open System Interconnection) model, its administration corresponds to layer 4 (transport)","Decoy = It means decoy and is used to hide the IP of the origin machine that is doing the exploration","Fingerprint = It means identification by fingerprint and is used to detect the operating system of the machines being scanned","Spoof = Means to falsify and is related to some type of service or protocol that you want to falsify.","Puertos reservados por el sistema = <1024 \nregistered ports = [1024:49151] \nprivate ports and for personal use = [1025:65535]"]

def escaner(ip):
	#vars
	run = True
	#-
	while(run == True):
		lmrand = random.randint(0,4)
		print("##[(L)azyness (S)ample (F)or (N)map]##")
		print("Tip{")
		print(lmensj[lmrand])
		print("}")
		print("---Default ports for some services---")
		print("Ports / Services \n  21     FTP \n  22     SSH \n  25     SMTP \n  53     DNS \n  80     HTTP \n  110    POP3 \n  143    IMAP \n  443    HTTPS \n  993    IMAPSSL \n  995    POPSSL")
		print("""{
			(1)-Scan_All_My_Ports               .     (7)-TCP-ACK[sA]       (14)-PortState[netstat]
			(2)-Basic_Scan[sS Pn O].                  (8)-Window_scanTCP[sW](15)-Scan_The_Local_NetWork
			(3)-Scan_UDP[sU].                         (9)-Maimon_scan[sM]
			(4)-Scan_TCPNULL[sN]                      (10)-TCP_adaptative_scan--scanflags[URG ACK PSH RST SYN FIN]
			(5)-Scan_XMAS[sX]                         (11)-Ip_scan(sO)
			(6)-scan_FIN[sF]                          (12)-<user>:<pass>@<server>:<port>(b)
			(q)-quit                                 (13)-IdleScan $[Ej. nmap -sI zombie_host target_host]$[sI]
			}""")
		usrAns = input('enter an option > ')
		if(usrAns == '1'):
			os.system('sudo netstat -tuna')
			print("#[List of active UDP/TCP Ports]#")
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 'q'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '2'):
			os.system('sudo nmap -A -T3 -sS -Pn -O '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '3'):
			os.system('sudo nmap  -sU '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '4'):
			os.system('sudo nmap  -sN '+ip)
			usrAns = input('(q) or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '5'):
			os.system('sudo nmap  -sX '+ip)
			usrAns = input('(q)uit o (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '6'):
			os.system('sudo nmap -sF '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '7'):
			os.system('sudo nmap -sA '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '8'):
			os.system('sudo nmap -sW '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '9'):
			os.system('sudo nmap -sW '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '10'):
			flags = input('ingresa las flags > ')
			os.system('sudo nmap --scanflags '+flags+' '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '11'):
			os.system('sudo nmap  -sO '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '12'):
			print("$[Ej. nmap <user>:<pass>@<server>:<port>]$")
			user = input('user > ')
			psw = input('psw > ')
			port = input('port > ')
			os.system('sudo nmap -Pn -b '+user+':'+psw+'@'+ip+':'+port)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '13'):
			os.system('sudo nmap -sI -Pn '+ip)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '14'):
			port = input('Port Number > ')
			os.system('sudo netstat -putan | grep '+port)
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == '15'):
			dgateway = input('input the gateway > ')
			os.system('sudo nmap -A -T3 -sI '+dgateway+'/24')
			usrAns = input('(q)uit or (c)ontinue ? > ')
			if(usrAns == 's'):
				os.system('clear')
				run = False
			if(usrAns == 'c'):
				os.system('clear')
				run = True
		if(usrAns == 'q'):
			run = False
