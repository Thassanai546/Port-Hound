import socket

def is_port_open(host, port):
    s = socket.socket(); # create new socket

    try:
        # try to connect to host using given port
        s.settimeout(0.2)
        s.connect((host,port))
    except:
        return False # port closed/cannot connect
    else:
        return True # port is open
   
host = input("Enter a host:\n")
print("Scan results for: " + socket.gethostbyname(host))
for port in range(50,150):
    if is_port_open(host,port):
        print("[+]" + str(host) + ':' + str(port) + " is open.")
    else:
        print("[-]" + str(host) + ':' + str(port) + " is closed.")