import sys
import os
import time
from subprocess import Popen, PIPE, check_output
import re

# generate the various dictionaries
dicGen = Popen(['python3','dataGen.py'])

# lists to iterate over w command line parameters
shortDicts = ["short_sorted_dic", "short_unsorted_dic"]
medDicts = ["med_sorted_dic", "med_unsorted_dic"]
longDicts = ["long_unsorted_dic", "long_sorted_dic"]
inputs = ["short_input_set", "med_input_set", "long_input_set"]
dicImp = ["darray.py", "hashset.py", "bstree.py"]

stats = []

for dic in shortDicts:
	stats.append("****************************")
	stats.append("Dictionary: " +dic)
	stats.append("****************************")
	for imp in dicImp:
		print("Testing " +dic +" for dictionary implementation " +imp)
		commands = ['python3','speller_'+imp]
		start = time.time()
		# run program
		output = check_output(commands+['-d',dic,'-m',str(0),"short_input_set"]).decode(sys.stdout.encoding)
		end = time.time()
		stats.append("Implementation: "+imp+"\nTime: "+str(end-start)+" seconds.")
	stats.append("\n")


for dic in medDicts:
	stats.append("****************************")
	stats.append("Dictionary: " +dic)
	stats.append("****************************")
	for imp in dicImp:
		print("Testing " +dic +" for dictionary implementation " +imp)
		commands = ['python3','speller_'+imp]
		start = time.time()
		# run program
		output = check_output(commands+['-d',dic,'-m',str(0),"med_input_set"]).decode(sys.stdout.encoding)
		end = time.time()
		stats.append("Implementation: "+imp+"\nTime: "+str(end-start)+" seconds.")
	stats.append("\n")

for dic in longDicts:
	stats.append("****************************")
	stats.append("Dictionary: " +dic)
	stats.append("****************************")
	for imp in dicImp:
		print("Testing " +dic +" for dictionary implementation " +imp)
		# this control is here because the program breaks with large sorted btree as max recursion depth is reached
		if (dic == "long_sorted_dic" and imp=="bstree.py"):
			stats.append("Dictionary: " +dic +"\nImplementation: "+imp+"\nTime: "+"N/A"+" seconds.")
		else:
			commands = ['python3','speller_'+imp]
			start = time.time()
			output = check_output(commands+['-d',dic,'-m',str(0),"long_input_set"]).decode(sys.stdout.encoding)
			end = time.time()
			stats.append("Implementation: "+imp+"\nTime: "+str(end-start)+" seconds.")
	stats.append("\n")
		
for line in stats:
	print(line)