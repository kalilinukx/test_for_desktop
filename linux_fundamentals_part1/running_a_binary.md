Occasionally there will be times when you want to run downloaded or user created programs. This is done by providing the full path to the binary, for example say you download a binary that outputs noot, providing the full path to that binary will execute it. 



Note: A binary is just executable code, think a windows exe file

This seems like a good time to mention Relative Paths! Every time you intend on running the binary, you don't need to provide a full path, you can use Relative Paths.

Relative Paths:

The chart below will assume the current path is /tmp/aa 

Relative Path	Meaning	Absolute Path	Relative Path	Running a binary with a Relative Path	Running A Binary with an Absolute Path
.	Current Directory	/tmp/aa 	.	./hello	/tmp/aa/hello
..	Directory before the current directory	/tmp	..	../hello	/tmp/hello
~	The user's home directory	/home/<current user>	~	~/hello	/home/<user>/hello


These shortcuts are incredibly efficient, and save time. These shortcuts for every command, so if I were to run ls . it would be the same as running ls <current directory>   



How would you run a binary called hello using the directory shortcut . ?

./hello
How would you run a binary called hello in your home directory using the shortcut ~ ?

~/hello
How would you run a binary called hello in the previous directory using the shortcut .. ?

../hello
