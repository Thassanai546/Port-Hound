# Python-Port-Sniffer

![porthound-banner](https://user-images.githubusercontent.com/72495327/134083957-95a152b6-f77f-43ab-99ca-08985cee8102.PNG)

>[-] = Closed Port\
[+] = Open Port

## Description

<img src="http://ForTheBadge.com/images/badges/made-with-python.svg" align="left">

<img src="https://forthebadge.com/images/badges/built-with-love.svg">


Python port scanner built using Socket. This program also features Typer which allows users to pass in parameters in the CLI. Users may scan for a specific port or a range of ports. Socket will automatically convert hostnames like example.com to their IP addresses.\
\
The time taken after each scan is printed and closed ports will show up in red during output while open ports will show up in green.

## Installation
This script uses the following imports:
+ click==8.0.3
+ colorama==0.4.4
+ typer==0.4.0

## Usage
+ After downloading the script, you can run it in command prompt by typing `portscanner.py`. This will present you with a help page.
+ Under `Commands:` you will see a list of available options. `--help` can be appended to any of these.
+ Example `portscanner.py scanrange --help` will show you how to scan a range of hosts, presenting the output below:
+ You may pass in a text file (`.txt`) with a list of ports to scan using scanlist.

Only ever port scan website that you have permission to scan.

![image](https://user-images.githubusercontent.com/72495327/123128528-2266ec80-d443-11eb-8bfc-b3b5027a3948.png)

## Example Syntax
+ Use a list of ports and scan loopback address `> porthound.py scanlist 127.0.0.1 common_ports.txt`
+ Scan ports 60 to 100 on loopback address `> porthound.py scanrange 127.0.0.1 60 100`
