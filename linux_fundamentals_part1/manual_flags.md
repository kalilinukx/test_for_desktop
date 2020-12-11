Most of the commands you'll learn about have a lot of options that are not immediately known at first glance, these options are known as flags, and have the format <command> <flag> <input>. These flags can be learned about using the man command. The man command has the format man <command>. Therefore, to learn about flags for the echo command, we would type man echo. Typing that shows us a nicely formatted document:



We get alot of information, but the flags are stored in the description section. For example the flag to remove the newline is -n. So to output "Shiba" without the newline you would type echo -n Shiba.        

Note: Some commands support the -h flag, meaning you can type <command> -h and get a list of flags and other useful information without using man.           

How would you output hello without a newline
echo n