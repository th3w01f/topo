#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import pythonwhois
import pprint
import dns
import dns.resolver
import pygeoip
import shodan
import os
from bs4 import BeautifulSoup as BS
import urllib.request as urlr

#Vars
usrAns = "s"

#--
def ShodanSsearch(busqueda):
	os.system('clear')
	try:
		ShodanKeyString = "RWfPBBhDPi1ummOsEA5qKYrIpbo6Gv5g" #Key de usuario
		ShodanApi = shodan.Shodan(ShodanKeyString) #lo primeto es inicializar la api con el userKey
		results = ShodanApi.search(busqueda) #metodo que retorna un resultado proveniente de un diccionario
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
		for result in results['matches']:
			print('IP: %s' % result['ip_str'])
			print(result['data'])
			print('')
		print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
	except shodan.APIError:
		e = shodan.APIError
		print('Error: %s' % e)


#-

#--Top10
def top10shodan(busqueda):
	os.system('clear')
	print("[Top 10 Shodan]")
	FACETS = [('org',10),('domain',10),('port',10),('asn',10),('country',10)]

	FACET_TITLES = {'org':'Top 10 Organizations','domain':'Top 10 dominios','port':'Top 10 ports','asn':'Top 10 autonomus system','country':'Top 10 countries'}

	apikey = shodan.Shodan('RWfPBBhDPi1ummOsEA5qKYrIpbo6Gv5g')
	result = apikey.count(busqueda,facets=FACETS)
	print('Total results: %s\n' % result['total'])
	for facet in result['facets']:
		print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-")
		print(FACET_TITLES[facet])
		for term in result['facets'][facet]:
			print('%s : %s' % (term['value'], term['count']))
		print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

#-
#--
def geoIp(ip, url):
	os.system('clear')
	print("[GeoLocation IP]")
	# diccionarios .dat con informacion de la direccion Ip
	gi = pygeoip.GeoIP('GeoIP.dat') 
	gicity = pygeoip.GeoIP('GeoLiteCity.dat')
	giISP = pygeoip.GeoIP('GeoIPISP.dat')
	giASN = pygeoip.GeoIP('GeoIPASNum.dat')

	#imprime en pantalla el resultado
	print("##location##")
	pprint.pprint(gi.country_name_by_addr(ip))
	print("##server info##")
	pprint.pprint(gicity.record_by_addr(ip))
	print("##time zone##")
	pprint.pprint(gicity.time_zone_by_addr(ip))
	print("##ISP lookup##")
	pprint.pprint(giISP.isp_by_name(url))
	print("##ASN(Autonomous System Number) Lookup##")
	pprint.pprint(giASN.asn_by_name(url))
	print("###")
#_
#--obtiene informacion de los servidores dns introducidos
def regDns(url):
	os.system('clear')
	print("[DNS Info]")
	try:
		ansAAA = dns.resolver.query(url,'AAAA')
	except dns.resolver.NoAnswer:
		e = dns.resolver.NoAnswer
		print("Error> %s" % e) 
	ansMX = dns.resolver.query(url,'MX')
	ansA,ansNS=(dns.resolver.query(url,'A'),dns.resolver.query(url,'NS'))


	print("Ipv4: ")
	print(ansA.response.to_text())
	print("\n")
	print("Mail Servers")
	print(ansMX.response.to_text())
	print("\n")
	try:
		print("Ipv6")
		print(ansAAAA.response.to_text())
	except NameError:
		e = NameError
		print("Error> %s" % e +" posiblemente no posea dir Ipv6")
	print("\n")
	print("Name servers: ")
	print(ansNS.response.to_text())
	print("###")
#-
#-- Dominio info
def whoIs(url):
	os.system('clear')
	print("[Who Is]")
	pythonwhois.net.get_root_server(url) #se obtiene la informacion del servidor raiz
	whois = pythonwhois.get_whois(url) # un diccionario con toda la informacion del dominio
	whois_raw = pythonwhois.net.get_whois_raw(url)

	#imprimir
	print("#[keys]#")
	print(whois.keys())
	print("###")
	print("#[values]#")
	print(whois.values())
	print("###")
	print("#[raw]#")
	pprint.pprint(whois_raw)
	print("###")
#-
#-- Info Headers
def urlget(url):
	os.system('clear')
	print("[Headers Response]")
	urlobj = urlr.urlopen("https://"+url)
	urldir = urlobj.geturl()
	urlinf = urlobj.info()
	code = urlobj.getcode()

	print("url|>"+urldir+"|<")
	print("-*-*Objeto*-*-")
	print(urlobj)
	print("*-*-info-*-*")
	print(urlinf)
	print("-@-code-@-")
	print(code)
#-
#-- Robothi
def robothi(url):
	os.system('clear')
	print("[RobotHi]")
	urlobj = urlr.urlopen("https://"+url+"/robots.txt")
	soup = BS(urlobj, 'lxml')
	print("#[O.O]#")
	print(soup.get_text())
	print("$[o.o]$")
#-
#-- Obtiene el codigo fuente de la pagina
def scrawl(url):
	os.system('clear')
	urlobj = urlr.urlopen("https://"+url)
	soup = BS(urlobj, 'lxml')
	print("[SOURCE CODE VIEW]")
	print(soup.prettify())
	print("[*]")

