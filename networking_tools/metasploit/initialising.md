If this is your first time using Metasploit, you'll have just a few things to do before you utilize its full functionality. Let's go ahead and get everything started!



First things first, we need to initialize the database! Let's do that now with the command: msfdb init
If you're using the AttackBox, you don't need to do this.

No answer needed
Before starting Metasploit, we can view some of the advanced options we can trigger for starting the console. Check these out now by using the command: msfconsole -h

No answer needed
We can start the Metasploit console on the command line without showing the banner or any startup information as well. What switch do we add to msfconsole to start it without showing this information? This will include the '-'

-q
Once the database is initialized, go ahead and start Metasploit via the command: msfconsole

No answer needed
After Metasploit has started, let's go ahead and check that we've connected to the database. Do this now with the command: db_status

No answer needed
Cool! We've connected to the database, which type of database does Metasploit 5 use? 

postgresql
