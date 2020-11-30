The logical follow-up to the ping command is 'traceroute'. The easiest way to understand what traceroute does is to think of your home network. Say, for example, that you have a wireless router. Your phone is connected to it, as is your computer. What happens if you want to send something to your phone from your computer? You can't just send stuff directly to your phone -- not without directly connecting them, so how would the information get across? The request would first be sent to your router which acts as a gateway. The router knows every device that's connected to it, ergo, it knows how to get to your phone. The router then forwards your request on to your phone and facilitates the return connection in the same way. Traceroute can be used to map the path your request takes as it heads to the target machine.

The internet is made up of many, many different servers and end-points, all networked up to each other. This means that, in order to get to the content you actually want, you first need to go through a bunch of other servers. Traceroute allows you to see each of these connections -- it allows you to see every intermediate step between your computer and the resource that you requested. The basic syntax for traceroute on Linux is this: traceroute <destination>

By default, the Windows traceroute utility (tracert) operates using the same ICMP protocol that ping utilises, and the Unix equivalent operates over UDP. This can be altered with switches in both instances.



You can see that it took 13 hops to get from my router (_gateway) to the Google server at 216.58.205.46

Now it's your turn. As with before, all questions about switches can be answered with the man page for traceroute
(man traceroute).