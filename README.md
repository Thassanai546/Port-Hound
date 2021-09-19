# Python-Port-Sniffer

![doggo](https://user-images.githubusercontent.com/72495327/123127704-6f968e80-d442-11eb-9547-a525e8fd5203.PNG)

>[-] = Closed Port\
[+] = Open Port

## Description
Python port scanner built using Socket. This program also features Typer which allows users to pass in parameters in the CLI. Users may scan for a specific port or a range of ports. Socket will automatically convert hostnames like example.com to their IP addresses.

## Installation
This script uses the following imports:
+ typer
+ socket
+ time
+ typing 
  + optional

## Usage
+ After downloading the script, you can run it in command prompt by typing `portscanner.py`. This will present you with a help page.
+ Under `Commands:` you will see a list of available options. `--help` can be appended to any of these.
+ Example `portscanner.py scanrange --help` will show you how to scan a range of hosts, presenting the output below:
+ You may pass in a text file (`.txt`) with a list of ports to scan using scanlist.

Only ever port scan website that you have permission to scan.

![image](https://user-images.githubusercontent.com/72495327/123128528-2266ec80-d443-11eb-8bfc-b3b5027a3948.png)
