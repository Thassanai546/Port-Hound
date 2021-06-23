from typing import Optional
import typer
import socket
import time

app = typer.Typer()

def banner(): # Dog that sniffs for ports
    print('''
    Sniffing...
      __      _
    o'')}____//
    `_/      )
    (_(_/-(_/
    ''')

@app.command() # User can enter a port to scan
def scan(host: str, port: int, timeout: Optional[float] = typer.Argument(.2)):
    con = socket.socket()
    con.settimeout(timeout)
    try:
        con.connect((host,port))
    except:
        print(f"[-] {host}: {port}")
    else:
        print(f"[+] {host}: {port} - Open")

@app.command() # User can enter a port list text document to scan
def scanlist(host: str, file: str, timeout: Optional[float] = typer.Argument(.2)):
    banner()
    print("Target: " + socket.gethostbyname(host) + "\n")
    time_start = time.time()
    try:
        file = open(file) # Attempt to open user specified file
        print("File opened successfully")
        for portNo in file:
            scan(host, int(portNo), timeout)
    except:
        print("could not open that file!")
    print("Time Taken: " + str(round(time.time() - time_start,2)))

@app.command() # range not yet supported in typer, min max used instead
def scanrange(host: str, start: int, end: int, timeout: Optional[float] = typer.Argument(.2)):
    banner()
    print("Target: " + socket.gethostbyname(host) + "\n")
    time_start = time.time()
    portRange = range(start,end+1)
    for port in portRange:
        scan(host, port, timeout)
    print("-------------------\nTime Taken: " + str(round(time.time() - time_start,2)))

if __name__ == "__main__":
    app()