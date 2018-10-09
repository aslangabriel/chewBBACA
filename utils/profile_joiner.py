#!/usr/bin/env python3

import argparse
import csv
from collections import defaultdict

def main():
	parser = argparse.ArgumentParser(
		description="This program joins two profiles with the ")
	parser.add_argument('-p1', nargs='?', type=str, help='profile 1', required=True)
	parser.add_argument('-p2', nargs='?', type=str, help='profile 2', required=True)
	parser.add_argument('-o', nargs='?', type=str, help='outut file name', required=True)

	args = parser.parse_args()

	profile1 = args.p1
	profile2 = args.p2
	outputFile = args.o


	dictaux= defaultdict(list)

	print ("reading profile 1")
	with open(profile1) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		headers = next(reader)

		len1=0
		for row in reader:
			i=0
			for elem in row:
				dictaux[headers[i]].append(elem)
				i+=1
			len1+=1

	print ("reading profile 2")
	with open(profile2) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		headers = next(reader)

		len2=0
		for row in reader:
			i=0
			for elem in row:
				#~ print (elem)
				dictaux[headers[i]].append(elem)
				i+=1
			len2+=1

	listheaders2include=[]
	lists2print=[]
	for header in headers:
		aux= dictaux[header]
		if len(aux)==len1+len2:
			listheaders2include.append(header)
	i=0

	print ("building new profile")
	while i<len1+len2:
		aux=[]
		for header in listheaders2include:
			aux.append(dictaux[header][i])
		i+=1
		lists2print.append(aux)

	newProfileStr=('\t'.join(map(str, listheaders2include)))+"\n"
	for elem in lists2print:
		newProfileStr += ('\t'.join(map(str, elem)))+"\n"

	with open(outputFile, "w") as f:
		f.write(newProfileStr)


	print ("Done")


if __name__ == "__main__":
	main()