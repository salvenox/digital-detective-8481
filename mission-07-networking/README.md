# Mission 07 – Networking Basics

## Task / Objective
To understand basic networking concepts and learn how computers communicate over a network.

## Work Completed

Learned the following networking concepts:

- **LAN:** Local Area Network connects devices in a small area such as a home, office or college.
- **MAN:** Metropolitan Area Network connects networks across a city.
- **WAN:** Wide Area Network connects devices over large geographical areas. The Internet is an example.
- **DNS:** Domain Name System converts domain names into IP addresses.
- **Router:** A router forwards data between different networks.
- **Protocol:** A set of rules used for communication between devices. Examples include HTTP, HTTPS, TCP and IP.
- **Packet Switching:** Data is divided into smaller packets that travel through a network.
- **Client-Server:** A client sends requests and a server provides responses.

## Commands / Tools Used

### 1. Ping Command
Command:
`ping -c 4 google.com`

Result:
- 4 packets transmitted.
- 4 packets received.
- 0% packet loss.
- Average response time: 35.381 ms.

This command checks connectivity with another host.

### 2. DNS Lookup
Command:
`nslookup google.com`

Result:
- DNS lookup was successful.
- Multiple IP addresses were returned.
- DNS server information was displayed.

This command checks how a domain name is resolved into IP addresses.

### 3. Network Interface Information
Command:
`ifconfig`

Result:
- Network interfaces were displayed.
- The active network interface was identified.
- Network configuration information was displayed.

This command helps inspect network interfaces on macOS.

### 4. HTTP Response
Command:
`curl -I https://www.google.com`

Result:
- HTTP response status: 200
- Protocol: HTTP/2

This command displays the response headers returned by a website.

## How a Website Loads

1. The user enters a website address in the browser.
2. DNS finds the IP address of the domain.
3. The browser establishes a connection with the server.
4. A secure connection is established using TLS for HTTPS.
5. The browser sends an HTTP request.
6. The server sends the requested resources.
7. The browser processes the resources and displays the webpage.

## My Understanding

I learned how computers communicate over networks and how DNS, routers, protocols and packet switching help transfer data. I also learned how to check internet connectivity, perform DNS lookups and inspect HTTP response headers using Terminal commands.

## Difficulties Faced

Initially, understanding DNS resolution and network commands was difficult.

## How I Resolved Them

I practised networking commands in macOS Terminal and observed their outputs to understand their purpose.

## Evidence / Files

- `mission-07-networking/README.md`
- Practical commands and their observed results.

Note: Personal network addresses and hardware identifiers have not been included for privacy.

## Commit Details

To be updated after committing and pushing this mission.