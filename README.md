#small-programs  
Various personal small programs that can be useful.

The python folder contains scripts that do not require use of the makefile  
  
==============  

####Python Scripts:  
script | purpose
:----------- | :-----------  
secret_santa | matches each given name with a single one of the other given names (without matching multiple names to the same one)
monitorUptime | pings a target server every 20s to check if it's still up. If not, it records the start and end time on "hostname.uptime" and terminates itself

####Bash Scripts:  
script | purpose
:----------- | :-----------  
backup | makes a copy of target file with the current date appended to the filename. use it when you want to make a quick backup of a file you're about to change
eye | a simple animation of a blinking eye (from 'The Talos Principle'). the delay between frames can be changed by giving any argument accepted by 'sleep'.

####You can run these commands from a terminal in the repository folder:  

command | effect  
:---------- | :----------  
make | compile all programs  
make prog_name | compile a specific program (or run it, if it has * next to it's name) 
make c | clean all .o files from the source folder  

####Availiable programs with makefile:  
  
progam | purpose
:----------- | :-----------  
mem_alloc | uses a user specified ammount of 100MB blocks from system memory, can be useful for testing

####Projected:
