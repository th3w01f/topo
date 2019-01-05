
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

