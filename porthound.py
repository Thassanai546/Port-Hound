from typing import Optional
import typer
import socket
import time

app = typer.Typer()

def banner(): # Dog that sniffs for ports
    print('''
                    Warning!!! Port scanning a target without permission
        |\_/|       can get you into trouble.     
        | @ @       If you want to test the scanner use 127.0.0.1
        |   <>              _ 
        |  _/\------____ ((| |))
        |               `--' |   
    ____|_       ___|   |___.' 
    /_/_____/____/_______|
    ''')

@app.command() # User can enter a specific port to scan
def scan(host: str, port: int, timeout: Optional[float] = typer.Argument(.2)):
    con = socket.socket()
    con.settimeout(timeout)
    try:
        con.connect((host,port))
    except:
        print(f"[-] {host}: {port}")
    else:
        print(f"[+] {host}: {port} - Open")

@app.command() # User can specify a list of ports to scan
def scanlist(host: str, file: str, timeout: Optional[float] = typer.Argument(.2)):
    print("Target: " + socket.gethostbyname(host) + "\n")
    time_start = time.time()
    try:
        if '.txt' not in file:
            file += '.txt'
        
        file = open(file) # Attempt to open user specified file
        print("File opened successfully")
        for portNo in file:
            scan(host, int(portNo), timeout)
    except:
        print("could not open that file!")
    # time taken in seconds down to 2 decimal places
    print(f"-------------------\nTime Taken: {str(round(time.time() - time_start,2))}")

@app.command() # User can enter a range of ports to scan. Range type in Python not supported by Typer yet
def scanrange(host: str, start: int, end: int, timeout: Optional[float] = typer.Argument(.2)):
    print("Target: " + socket.gethostbyname(host) + "\n")
    time_start = time.time()
    portRange = range(start,end+1)
    for port in portRange:
        scan(host, port, timeout)
    print(f"-------------------\nTime Taken: {str(round(time.time() - time_start,2))}")

if __name__ == "__main__":
    banner()
    app()