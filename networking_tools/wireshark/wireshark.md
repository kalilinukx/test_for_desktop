We've gone over the basic theory -- now let's put it into practice! In this task we're going to look at some captured network traffic to see the advantages of understanding the OSI and TCP/IP Models.

Wireshark is a tool used to capture and analyse packets of data going across a network.

We're going to use Wireshark to get an idea of what these models look like in practice, with real world data.

Download the attached .pcap file (Wireshark capture) and follow along!

When you first load the packet into Wireshark you're given a list of captured data in the top window (there are two items in this window just now), and in the bottom two windows you're shown the data contained in each captured packet of data:

There are 5 pieces of information here:

Frame 1 -- this is showing details from the physical layer of the OSI model (Network Interface layer of the TCP/IP model): the size of the packet received in terms of bytes)
Ethernet II -- this is showing details from the Data Link layer of the OSI model (Network Interface layer of the TCP/IP model): the transmission medium (in this case an Ethernet cable), as well as the source and destination MAC addresses of the request.
Internet Protocol Version 4 -- this is showing details from the Network layer of the OSI model (Internet Layer of the TCP/IP model): the source and destination IP addresses of the request.
Transmission Control Protocol -- this is showing details from the Transport layer of the OSI and TCP/IP models: in this case it's telling us that the protocol was TCP, along with a few other things that we're not covering here.
Hypertext Transfer Protocol -- this is showing details from the Application layer of the OSI and TCP/IP models: specifically, this is a HTTP GET request, which is requesting a web page from a remote server.
This is not a Wireshark room, so we're not going to go into any more depth than that. The important thing is that you understand how the theory you learnt earlier translated into a real life scenario. For more in-depth packet analysis, check out the Wireshark room by Cryillic.

With that in mind, click on the second captured packet (in the top window) and answer the following questions:

