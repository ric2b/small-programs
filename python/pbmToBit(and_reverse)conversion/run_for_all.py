import os
import shutil
import sys
import glob
import filecmp

originFolder_remove = "pbm"
destinationFolder_remove = "bit"
Folder_add = "result" #the remove operation overwrites the file
add_header_program = "python add_header.py"
remove_header_program = "python remove_header.py"
arguments = ""

extensionLenght = 4

def check_args():
	""" checks if a file was supplied to the script """
	if len(sys.argv) != 2:
		print "need an extra argument, [add] or [remove]. (to add or remove the header)"
		exit()
	else: 
		return sys.argv[1]

mode = check_args()

if mode == "remove":
	files = list(set(glob.glob(originFolder_remove + "/*")) - set(glob.glob(originFolder_remove + "/*.bit")) - set(glob.glob(originFolder_remove + "/*.exclude")))
	prefix_lenght = len(originFolder_remove + "/")

	for i, val in enumerate(files):
		files[i] = files[i][prefix_lenght:]

	for filename in files:
		filenameNoExtension = filename[0:(len(filename)-extensionLenght)]
		os.system(remove_header_program + " " + originFolder_remove + "/" + filename + arguments)
		shutil.move(originFolder_remove + "/" + filenameNoExtension + ".bit", destinationFolder_remove + "/" + filenameNoExtension + ".bit")

	print
	print remove_header_program + " was ran for all files in the directory " + originFolder_remove
	exit()		

if mode == "add":
	files = list(set(glob.glob(Folder_add + "/*")) - set(glob.glob(Folder_add + "/*.pbm")) - set(glob.glob(Folder_add + "/*.exclude")))
	prefix_lenght = len(Folder_add + "/")

	for i, val in enumerate(files):
		files[i] = files[i][prefix_lenght:]

	for filename in files:
		filenameNoExtension = filename[0:(len(filename)-extensionLenght)]
		os.system(add_header_program + " " + Folder_add + "/" + filename + arguments)
		os.system("rm " + Folder_add + "/" + filename)

	print
	print add_header_program + " was ran for all files in the directory " + Folder_add
	exit()



print "wrong argument, use [add] or [remove]"
exit()