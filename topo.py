#!/usr/bin/env python
#-*- coding:utf-8 -*-

from  rsrchtoolv001 import whoIs 
from  rsrchtoolv001 import regDns
from  rsrchtoolv001 import geoIp
from  rsrchtoolv001 import top10shodan
from  rsrchtoolv001 import ShodanSsearch as Shsearch
from  rsrchtoolv001 import urlget
from  rsrchtoolv001 import robothi
from  rsrchtoolv001 import scrawl
from  dorkerworker import opts
from lazy_nmapscan import escaner
import dns
import os
import argparse

#gb
parser = argparse.ArgumentParser(
	prog='topo.py',
	description='| a tool box for digging and gathering information |',
	epilog='$$[(T)ake (O)btain (P)ackets (O)utputs]$$. . its a lazy tool... . . .'
	)
parser.add_argument('ipc', action='store',help='store the ip')
parser.add_argument('urlc', action='store',help='store the url')
parser.add_argument('--options', action='store_true', help='shows the functions of the program')
parser.add_argument('--change', action='store_true', help='change the ip & url')
parser.add_argument('--dnsinf', action='store_true', help='It shows information about the servers dns, Ipv4 addresses, v6, MX')
parser.add_argument('--whois', action='store_true', help='consult who is it? ')
parser.add_argument('--geoip', action='store_true', help='check the server location (Database: GeoIP2)')
parser.add_argument('--headinf', action='store_true', help='Receive response codes from the http / https protocol.')
parser.add_argument('--robothi', action='store_true', help='take a look at the robots.txt file')
parser.add_argument('--dorkerworker', action='store_true', help='Get interesting dorks with just a few commands')
parser.add_argument('--sourceview', action='store_true', help='look at the source code o.o.')
parser.add_argument('--shodansearch', action='store_true', help='Search with Shodan')
parser.add_argument('--shtop', action='store_true', help='consult your top 10 with Shodan.')
parser.add_argument('--ntoolbox', action='store_true', help='commands for the analysis of ports and networks with nMap')


if(__name__ == '__main__'):
	args = parser.parse_args()
	ipc = args.ipc
	urlc = args.urlc
	if(args.ntoolbox == True):
		escaner(ipc)
	if(args.shtop == True):
		busqueda = input('ranking search > ')
		top10shodan(busqueda)
	if(args.shodansearch == True):
		busqueda = input('shodan search > ')
		Shsearch(busqueda)
	if(args.sourceview == True):
		scrawl(urlc)
	if(args.dorkerworker == True):
		opts()
	if(args.robothi == True):
		robothi(urlc)
	if(args.headinf == True):
		urlget(urlc)
	if(args.geoip == True):
		geoIp(ipc, urlc)
	if(args.whois == True):
		whoIs(urlc)
	if(args.dnsinf == True):
		try:
			regDns(urlc)
		except dns.resolver.NoAnswer:
			e = dns.resolver.NoAnswer
			print("Error:%s"% e)
	if(args.change == True):
		url = input('url > ')
		ip = input('ip > ')
