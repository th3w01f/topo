
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

| a tool box for digging and gathering information |

positional arguments:
  ipc             store the ip
  urlc            store the url

optional arguments:
  -h, --help      show this help message and exit
  --options       shows the functions of the program
  --change        change the ip & url
  --dnsinf        It shows information about the servers dns, Ipv4 addresses,
                  v6, MX
  --whois         consult who is it?
  --geoip         check the server location (Database: GeoIP2)
  --headinf       Receive response codes from the http / https protocol.
  --robothi       take a look at the robots.txt file
  --dorkerworker  Get interesting dorks with just a few commands
  --sourceview    look at the source code o.o.
  --shodansearch  Search with Shodan
  --shtop         consult your top 10 with Shodan.
  --ntoolbox      commands for the analysis of ports and networks with nMap

$$[(T)ake (O)btain (P)ickUp (O)utputs]$$. . its a lazy tool... . . .

