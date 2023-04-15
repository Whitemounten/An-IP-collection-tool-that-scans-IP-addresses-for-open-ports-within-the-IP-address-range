# An-IP-collection-tool-that-scans-IP-addresses-for-open-ports-within-the-IP-address-range

This code is a Python script that implements an IP aggregation tool that scans IP addresses for open ports within a given IP address range.

The code uses the "socket" module to create a TCP socket and try to connect to a specific port range at every IP address within a given IP address range. If a connection is successful (ie the port is open), the IP address and port number are added to the results list.

The "argparse" module is used to parse command line arguments such as target IP address range and port range to scan, and saves the results to the console and/or a local text file if an optional output file path is provided.

The "ipaddress" module is used to generate a list of IP addresses in the specified range.

This code provides the implementation of a basic cybersecurity IP collection tool.
