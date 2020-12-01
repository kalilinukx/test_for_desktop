To understand TCP Connect scans (-sT), it's important that you're comfortable with the TCP three-way handshake. If this term is new to you then completing Introductory Networking before continuing would be advisable.

As a brief recap, the three-way handshake consists of three stages. First the connecting terminal (our attacking machine, in this instance) sends a TCP request to the target server with the SYN flag set. The server then acknowledges this packet with a TCP response containing the SYN flag, as well as the ACK flag. Finally, our terminal completes the handshake by sending a TCP request with the ACK flag set.



This is one of the fundamental principles of TCP/IP networking, but how does it relate to Nmap?

Well, as the name suggests, a TCP Connect scan works by performing the three-way handshake with each target port in turn. In other words, Nmap tries to connect to each specified TCP port, and determines whether the service is open by the response it receives.

For example, if a port is closed, RFC 793 states that:

"... If the connection does not exist (CLOSED) then a reset is sent in response to any incoming segment except another reset.  In particular, SYNs addressed to a non-existent connection are rejected by this means."

In other words, if Nmap sends a TCP request with the SYN flag set to a closed port, the target server will respond with a TCP packet with the RST (Reset) flag set. By this response, Nmap can establish that the port is closed.



If, however, the request is sent to an open port, the target will respond with a TCP packet with the SYN/ACK flags set. Nmap then marks this port as being open (and completes the handshake by sending back a TCP packet with ACK set).

This is all well and good, however, there is a third possibility.

What if the port is open, but hidden behind a firewall?

Many firewalls are configured to simply drop incoming packets. Nmap sends a TCP SYN request, and receives nothing back. This indicates that the port is being protected by a firewall and thus the port is considered to be filtered.

That said, it is very easy to configure a firewall to respond with a RST TCP packet. For example, in IPtables for Linux, a simple version of the command would be as follows:

iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset

This can make it extremely difficult (if not impossible) to get an accurate reading of the target(s).



Question: ->

Which RFC defines the appropriate behaviour for the TCP protocol?

RFC 793 
If a port is closed, which flag should the server send back to indicate this?

rst
