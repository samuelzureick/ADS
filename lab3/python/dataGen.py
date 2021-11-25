import random
import math

with open("words.txt") as dicFile:
	dicArray = dicFile.readlines()

newArray = []
for i in range(0,len(dicArray),3):
	newArray.append(dicArray[i])

dicArray = newArray

# generating short, medium, and long sorted dictionaries
f = open("short_sorted_dic", "w")
shortDict = []
for i in range(0,len(dicArray), int(len(dicArray)**.6)):
	shortDict.append(dicArray[i])
	f.write(dicArray[i])
f.close()

medDict = []
f = open("med_sorted_dic", "w")
for i in range(0, len(dicArray), int(len(dicArray)**.3)):
	medDict.append(dicArray[i])
	f.write(dicArray[i])
f.close()

longDict = []
f = open("long_sorted_dic", "w")
for i in range(len(dicArray)):
	f.write(dicArray[i])
f.close()

# shuffling
random.shuffle(shortDict)
f = open("short_unsorted_dic", "w")
for i in range(len(shortDict)):
	f.write(shortDict[i])
f.close()

random.shuffle(medDict)
f = open("med_unsorted_dic", "w")
for i in range(len(medDict)):
	f.write(medDict[i])
f.close()

random.shuffle(dicArray)
f = open("long_unsorted_dic", "w")
for i in range(len(dicArray)):
	f.write(dicArray[i])
f.close()

# generating input sets
temp = []

# generate list of random words from dictionary that gets larger with input dictionary but not crazy big
for i in range(int(len(shortDict)/(3**math.log10(len(shortDict))))):
	temp.append(shortDict[random.randint(0,len(shortDict)-1)])

# misspell 10% of them
for i in range(int(.1*len(temp))):
	temp[random.randint(0, len(temp)-1)] += "qjq"

f = open("short_input_set", "w")
for i in range(len(temp)):
	f.write(temp[i])
f.close()


temp = []

# generate list of random words from dictionary that gets larger with input dictionary but not crazy big
for i in range(int(len(medDict)/(3**math.log10(len(medDict))))):
	temp.append(medDict[random.randint(0,len(medDict)-1)])

# misspell 10% of them
for i in range(int(.1*len(temp))):
	temp[random.randint(0, len(temp)-1)] += "qjq"

f = open("med_input_set", "w")
for i in range(len(temp)):
	f.write(temp[i])
f.close()

temp = []

# generate list of random words from dictionary that gets larger with input dictionary but not crazy big
for i in range(int(len(dicArray)/(3**math.log10(len(dicArray))))):
	temp.append(dicArray[random.randint(0,len(dicArray)-1)])

# misspell 10% of them
for i in range(int(.1*len(temp))):
	temp[random.randint(0, len(temp)-1)] += "qjq"

f = open("long_input_set", "w")
for i in range(len(temp)):
	f.write(temp[i])
f.close()


	


