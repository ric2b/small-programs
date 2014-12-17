NOTE: all mentioned directories are to be created in the same directory as this readme

To convert pbm to bit:
	1. Generate 128x128 .pbm files in Gimp (or a similar program)
	2. Store all .pbm files you want to convert in a directory called "pbm"
	3. Create a folder called "bit"
	4. From terminal, run this command: python run_for_all.py remove

To convert bit to pbm:
	1. Store all 128x128 .bit files you want to convert in a directory called "result"
	2. From terminal, run this command: python run_for_all.py add
	NOTE: this deletes the .bit files to prevent clutter in the folder. If this is not desired, add '#' to the beginning of line 52 

- amends softwaresTM
