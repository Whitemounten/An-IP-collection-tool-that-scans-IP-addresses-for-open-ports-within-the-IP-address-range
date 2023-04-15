# An-IP-collection-tool-that-scans-IP-addresses-for-open-ports-within-the-IP-address-range

u code is a Python script that implements an IP aggregation tool that scans IP addresses for open ports within a given IP address range.

The code uses the "socket" module to create a TCP socket and try to connect to a specific port range at every IP address within a given IP address range. If a connection is successful (ie the port is open), the IP address and port number are added to the results list.
