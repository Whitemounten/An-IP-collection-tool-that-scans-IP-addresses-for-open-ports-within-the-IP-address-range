import socket
import argparse
import ipaddress

# Define command line arguments
parser = argparse.ArgumentParser(description='IP Collection Tool')
parser.add_argument('range', type=str, help='Target IP address range (CIDR notation)')
parser.add_argument('-p', '--ports', type=str, help='Port range to scan (default: 1-1000)', default='1-1000')
parser.add_argument('-o', '--output', type=str, help='Output file path')
args = parser.parse_args()

# Parse port range argument
start_port, end_port = args.ports.split('-')
start_port = int(start_port)
end_port = int(end_port)

# Parse IP address range argument
network = ipaddress.ip_network(args.range)

# Initialize output list
results = []

# Iterate through IP address range
for ip in network:
    ip = str(ip)
    try:
        # Connect to IP address on each port
        for port in range(start_port, end_port+1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                # If port is open, add IP address and port to results
                results.append((ip, port))
                print(f"Port {port} is open on {ip}")
            sock.close()
    except socket.gaierror:
        pass

# Save results to output file
if args.output:
    with open(args.output, 'w') as f:
        for ip, port in results:
            f.write(f"{ip}:{port}\n")
