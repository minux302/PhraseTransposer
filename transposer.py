# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from xml.dom import minidom
import copy
import sys


def prettify(elem):
	"""
	This function formats xml for easy viewing
	"""
	rough_string = ET.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return '\n'.join([line for line in reparsed.toprettyxml(indent='	'*2).split('\n') if line.strip()])


key_interval_list = [-1, -2, -3, -4, -5, 6, 5, 4, 3, 2, 1] # Key interval. If original Key is C, it means F, Bb, Eb, ... D, G 
interval_list = [-7, -2, -9, -4, 1, -6, -1, -8, -3, 2, -5] # Parallel movement distance of keyboard
args = sys.argv
tree = ET.parse(args[1])
top = tree.getroot() 
node = top.find(".//Score/Staff")
phrase_length = len(top.findall(".//Measure"))


# Get original Key. Using try because there is no Element <KeySig> as default
try:
	initial_key = int(top.find(".//KeySig/accidental").text)
except AttributeError:
	key = ET.Element("KeySig")
	accidental = ET.SubElement(key, "accidental")
	accidental.text = "0"
	initial_key = 0
	top.find(".//Measure").insert(0,key)


for i in range(len(key_interval_list)):
	for num, e in enumerate(top.findall(".//Measure")):
		dupe = copy.deepcopy(e)

		# change key, pitch, sounds, codeNames
		for accidental in dupe.getiterator("accidental"):
			accidental.text = str(initial_key + key_interval_list[i])
		for pitch in dupe.findall(".//pitch"):
			transpose = int(pitch.text) + interval_list[i]
			pitch.text = str(transpose)
		for tpc in dupe.findall(".//tpc"):
			transpose = int(tpc.text) + key_interval_list[i]
			tpc.text = str(transpose)
		for root in dupe.findall(".//Harmony/root"):
			transpose = int(root.text) + key_interval_list[i]
			root.text = str(transpose)

		node.append(dupe)
		if num == (phrase_length - 1): break


with open(args[2], "w") as file:
	file.write(prettify(top))