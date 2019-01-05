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
