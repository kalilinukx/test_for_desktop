The $ is an unusually special operator, as it is used to denote environment variables. These are variables set by the computer(you can set them yourself but we'll get into that) that are used to affect different processes and how they work. Meaning that if you edit these variables you can change how certain processes work on your computer. For example your current user is always stored in an environment variable called $USER. You can view these variables with the echo command.


![alt text](https://imgur.com/bEGpRfG)



Naturally this means environment variables can be used as input for other commands as well, for example say I wanted to create a file which is the name of our current user, I could do touch $USER.



Recall that the >> operator appends output to a file.

Environment variables can also be set pretty easily, just running export <varname>=<value> will set that as an environment variable




How would you set nootnoot equal to 1111

export nootnoot=1111
What is the value of the home environment variable

/home/shiba2
