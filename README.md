[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cb2632b5e4b64b84ad8a4eb490bc3d14)](https://www.codacy.com/app/th3w01f/topo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=th3w01f/topo&amp;utm_campaign=Badge_Grade)

TOPO is a tool that optimizes the information gathering process

Steps for use

When you have a copy of the project you must have installed the version 3 of python next to the pip library

go to the project folder and install the requirements so that certain functions can be used

$ pip3 install -r requirements.txt

Go to the website of Shodan, register and get a KEY API then enter it in the variable that is on line 22 and 46 of the script rsrchtoolv001.py

$ python3 topo.py --help

usage: topo.py [-h] [--options] [--change] [--dnsinf] [--whois] [--geoip]
               [--headinf] [--robothi] [--dorkerworker] [--sourceview]
               [--shodansearch] [--shtop] [--ntoolbox]
               ipc urlc

Example-
$ python3 topo.py --geoip 192.30.253.112 github.com

[GeoLocation IP]

##location##
'United States'

##server info##
{'area_code': 415,
 'city': 'San Francisco',
 'continent': 'NA',
 'country_code': 'US',
 'country_code3': 'USA',
 'country_name': 'United States',
 'dma_code': 807,
 'latitude': 37.7697,
 'longitude': -122.39330000000001,
 'metro_code': 'San Francisco, CA',
 'postal_code': '94107',
 'region_code': 'CA',
 'time_zone': 'America/Los_Angeles'}
 
##time zone##
'America/Los_Angeles'

##ISP lookup##
None

##ASN(Autonomous System Number) Lookup##
'AS36459 GitHub, Inc.'

###

Documentacion(ES):https://drive.google.com/open?id=1dL7jxz45lRVP6DwqkW5G_vDaBvS_31NY

Guia de Usuario(ES):https://drive.google.com/open?id=1CViFq_6tb9rI2F7JyDByA4If2x_VtKWj
