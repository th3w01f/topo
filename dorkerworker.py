#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
#vars
usrAns = 's'

def presentation():
	print("!#[WorkerDorker]#!")
	print("Machine Of Dork 4 Lazy Humans")

def opts():
	print("""
	1-[SQLInyectionDorks]
	2-[DevicesAndCameras]
	3-[LoginPages]
	4-[UserAndPassword]
	5-[Vulnerabilities]
	6-[Interest Directories]
	7-[Web Server Banners]
	8-[vulnerable systems]
	9-[network vulnerabilities]
	10-[interest info]
	11-[errors]
	b1-[exploit-db]
	""")
	cont = 0
	opc = input('option > ')
	if(opc == '1'):
		f = open("sqlinydork")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '2'):
		f = open("devcams")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '3'):
		f = open("loginpages")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '4'):
		f = open("usrpsw")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '5'):
		f = open("vulns")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '6'):
		f = open("interestdir")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '7'):
		f = open("webservbanners")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '8'):
		f = open("sysvulns")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '9'):
		f = open("netvulns")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '10'):
		f = open("interestinfo")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == '11'):
		f = open("errors")
		for line in f:
			print('D'+str(cont))
			print(line)
			cont += 1
			print('---')
	if(opc == 'b1'):
		os.system('w3m https://www.exploit-db.com/google-hacking-database/')

