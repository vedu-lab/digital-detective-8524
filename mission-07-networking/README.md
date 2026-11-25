# Mission 7 — How computers communicate

## 1. Task / objective
The objective of Mission 7 is to explore computer networking fundamentals, explain core networking types and models (LAN, MAN, WAN, DNS, routers, protocols, packet switching, client-server), perform privacy-safe terminal network diagnostics (`ping` and `nslookup`), and construct a structured technical explanation of the end-to-end communication lifecycle when opening a website in a browser.

## 2. Work completed
- Populated the comprehensive network concepts reference table with precise definitions and practical examples.
- Conducted real network connectivity tests using `ping -c 4 example.com` to observe ICMP transmission, latency, and packet loss metrics.
- Executed DNS resolution queries using `nslookup example.com` to observe A-record IP mapping.
- Authored a numbered 6-step end-to-end trace illustrating how a client browser communicates with a remote server over TCP/IP and HTTP/HTTPS.
- Ensured all local IP addresses, router gateways, and wireless network SSIDs are sanitized (`[redacted]`).

---

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A high-speed network spanning a geographically constrained area, such as a single home, classroom, computer laboratory, or office floor. | A home Wi-Fi or Ethernet network connecting a student's laptop, smartphone, gaming console, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A medium-scale telecommunications network covering an entire town, municipality, or large university campus, often interconnecting several LANs. | A university campus network interconnecting administrative buildings, student libraries, and academic department labs across town. |
| **WAN (Wide Area Network)** | A vast telecommunications network spanning large geographical distances, across states, countries, or entire continents. | The global public **Internet**, which connects millions of independent private, commercial, and governmental networks worldwide. |
| **DNS (Domain Name System)** | A globally distributed hierarchical database that functions as the Internet's directory service, translating human-friendly domain names into machine-routable IP addresses. | Translating `example.com` into the destination IPv4 address `104.20.23.154`. |
| **Router** | A Layer 3 network hardware device that analyzes incoming IP packet headers, determines the most efficient routing path across network subnets, and forwards data toward its destination. | A home broadband wireless router routing traffic between local home LAN devices and the Internet Service Provider's (ISP) WAN infrastructure. |
| **Protocol** | A standardized, formal set of established rules, message formats, and timing constraints governing how networked devices exchange data and handle transmission errors. | **HTTPS** (Hypertext Transfer Protocol Secure) and **TCP** (Transmission Control Protocol). |
| **Packet switching** | A network communication method in which data streams are divided into small, individually addressed segments (packets) that travel independently along dynamic network routes and are reassembled at the destination. | Standard Internet IP transmission, where packets find alternate routes around network congestion or temporary router outages. |
| **Client-server** | A distributed software architecture where client applications request data, files, or processing services, and dedicated central or cloud servers listen, process, and return responses. | A user's web browser (**client**) requesting an HTML web page from an Apache/NGINX web server (**server**). |

---

### Task 7.2 — Observe network information

#### 1. Connectivity Test Output:
```bash
ping -c 4 example.com
```
```text
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=59 time=5.090 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=59 time=32.420 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=59 time=70.760 ms
64 bytes from 104.20.23.154: icmp_seq=3 ttl=59 time=39.821 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.090/37.023/70.760/23.382 ms
```

#### 2. DNS Lookup Output:
```bash
nslookup example.com
```
```text
Server:		[redacted DNS server]
Address:	[redacted DNS server]#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154
```

#### Conceptual Observations:
- **What a connectivity test helps check**: `ping` utilizes ICMP (Internet Control Message Protocol) echo requests to determine whether a remote server is online and reachable, measures network latency (round-trip time in milliseconds), and verifies connection stability by calculating packet loss percentages (here, 0.0% loss).
- **What information a DNS lookup displays**: `nslookup` queries a DNS nameserver (port 53) and returns the authoritative or cached DNS records for the requested hostname, specifically displaying the resolved destination IP addresses (`172.66.147.243` and `104.20.23.154`).
- **Role of DNS when entering a website name**: Humans remember mnemonic words (like `example.com`), while network routers exclusively route numerical IP packets. DNS bridges this gap by instantaneously converting the human-readable domain name into an IP address so the client can initiate a network connection.

---

### Task 7.3 — What happens when you open a website? (Step-by-Step)

1. **User Request & DNS Resolution**:
   The user types a URL (e.g., `https://example.com`) into the web browser (**client**). The browser checks its local DNS cache; if the IP address is not cached, it queries a recursive **DNS** resolver, which traverses root, TLD, and authoritative nameservers to resolve the domain into the target server's IP address (`104.20.23.154`).

2. **Connection Establishment (TCP & TLS Handshake)**:
   The **client** initiates a TCP 3-way handshake (SYN $\to$ SYN-ACK $\to$ ACK) using the Transmission Control **Protocol** to establish a reliable connection with the **server** on port 443. For secure HTTPS, a TLS cryptographic handshake immediately follows to verify server identity and negotiate shared encryption keys.

3. **HTTP Request Generation & Transmission**:
   The browser **client** formats an HTTP GET request (e.g., `GET / HTTP/2`) containing request headers (User-Agent, Accept, Host). The operating system's networking stack encapsulates this application-layer request into TCP segments, then into IP packets containing source and destination IP addresses.

4. **Packet Switching & Routing across Networks**:
   The packets leave the client device via the local network interface, passing through the local **router** (gateway). Through **packet switching**, autonomous routers across regional networks and the wider WAN inspect destination IP headers and dynamically forward the packets along optimal routes toward the destination data center.

5. **Server Processing & HTTP Response**:
   The destination web **server** receives the incoming packets, reassembles the TCP stream, decrypts the TLS payload, and passes the HTTP request to the web server software (e.g., NGINX). The server processes the request, locates the requested resource, and returns an HTTP response (e.g., `HTTP/2 200 OK`) containing response headers and the HTML body payload.

6. **Client Rendering & Display**:
   The web **server** transmits the response packets back across the network to the **client**. The browser parses the returned HTML, builds the Document Object Model (DOM) and CSSOM, executes scripts, fetches linked external assets (images, stylesheets, fonts), and renders the interactive webpage on the screen for the user.

---

## 3. Commands / tools used
| Command | Purpose |
| :--- | :--- |
| `ping -c 4 example.com` | Sends 4 ICMP echo request packets to check host reachability and latency. |
| `nslookup example.com` | Queries DNS nameservers to resolve domain names into IP addresses. |

## 4. My understanding
- Modern networking relies on modular abstraction layers (OSI and TCP/IP models).
- The client-server model underpins virtually all web services, enabled by underlying transport protocols (TCP) that provide reliable delivery atop unreliable packet-switched IP networks.
- Privacy in networking is crucial: personal gateway IPs and MAC addresses should be shielded from public repositories to prevent tracking or targeting.

## 5. Difficulties faced
- No major difficulties. Both `ping` and `nslookup` responded with 0% packet loss and low latency.

## 6. How I resolved them
- Sanitized local DNS resolver IP addresses and private network gateways in terminal logs with `[redacted]`.

## 7. Evidence / files
- `mission-07-networking/README.md` (this report)

## 8. Commit details
- **Commit message**: `Explain networking concepts and website communication`
- **Branch**: `main`
- **Push target**: `origin main`
