#!/usr/bin/python
# -*-coding:Utf-8 -*
import os.path
import random

EVENT_FOCUS_TABLE_FILE = 'event_focus_table.txt'
EVENT_MEANING_TABLE_FILE = 'event_meaning_table.txt'

focus_table,meaning_table = {},{}

def rollD200():
	return random.randrange(1,200+1)

def rollD100():
	return random.randrange(1,100+1)

def getRange(rangeString):
	rangeString = rangeString.split('-')
	rangeArray = range(int(rangeString[0]), int(rangeString[1])+1)
	return rangeArray

def loadDataFile(name):
	path = os.path.join('data',name)
	try:
		with open(path, 'r+') as my_file:
			dictionnary = {}
			for line in my_file.readlines():
				line = line.strip()
				number,text = line.split('. ')
				dictionnary[number] = text
			return dictionnary
	except IOError as e:
		print(e)

def rollEventFocus():
	diceValue = rollD100()
	for key in focus_table:
		if diceValue in getRange(key):
			return focus_table[key]

def rollEventMeaning():
	diceValue = rollD200()
	return meaning_table[str(diceValue)]

if __name__ == '__main__':
	focus_table = loadDataFile(EVENT_FOCUS_TABLE_FILE)
	meaning_table = loadDataFile(EVENT_MEANING_TABLE_FILE)
	print rollEventFocus()
	print rollEventMeaning()
