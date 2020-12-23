Continuing with the trend of very special operators, we have the pipe. The pipe is unique because while operators like >> allow you to store the output of a command, the | operator allows you to take the output of a command and use it as input for a second command.

For example, I can use catto get the output of a file, and pipe that into grep to search for a specific string(Note: We will learn more about grep later, but for now just know that it's a command used to find specific strings in an input).  

 

It is worth noting that not all commands support the pipe, and some that do support it require you to use - instead of input, for example cat -. So always check to see if the command does support it  

Read the above!

