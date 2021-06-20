import socket

def is_port_open(host, port):
    s = socket.socket(); # create new socket
    s.settimeout(0.2) # allow user to change

    try:
        # try to connect to host using given port
        s.connect((host,port))
    except:
        return False # port closed/cannot connect
    else:
        return True # port is open
   
openPorts = 0
host = input("Enter a host:\n")
myFile = open('common_ports.txt')

for line in myFile:
    line = int(''.join(filter(str.isdigit, line))) # Extract number from string

    if is_port_open(host,line):
        print("[+]" + str(host) + ':' + str(line))
        openPorts = openPorts + 1
    else:
        print("[-]" + str(host) + ':' + str(line))

print("Total open: " + str(openPorts))