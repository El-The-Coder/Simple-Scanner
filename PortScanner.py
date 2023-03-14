import socket

def scan_port(host, port):
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set timeout
    s.settimeout(0.5)
    
    # Attempt to connect to host and port
    try:
        s.connect((host, port))
        print(f"Port {port} is open on {host}")
    except:
        pass
    
    # Close socket connection
    s.close()

# Get user input for host and port range
hosts = input("Enter comma separated list of hosts: ").split(",")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

# Loop through hosts and port range and scan each port
for host in hosts:
    print(f"Scanning {host}...")
    for port in range(start_port, end_port+1):
        scan_port(host.strip(), port)
