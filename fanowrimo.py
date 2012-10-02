#!/usr/bin/env python

# Version 1.0
# Last modified 2012-10-2

"""fanowrimo.py: "Fast Novel Writing Month."

Generate a novel of exactly 50000 words, in accordance with National Novel Writing Month (nanowrimo.org).

Output format is in Markdown. If (no or too many) arguments are given, this message will display.

Example usage:
./fanowrimo.py GreatAmericanNovel.md
"""

from sys import argv
from sys import exit
from os.path import exists
import random

byline = "a novel by Ernst Hummingway"
toc = "Table of Contents"
the_end = "THE END"
epilogue_title = "EPILOGUE"

remainder = 50000 - len(byline.split(" ")) - len(toc.split(" ")) - len(the_end.split(" ")) - len(epilogue_title.split(" "))

def usage():
	print __doc__
	exit()

def phrase_gen(wordcount):
	"""Generates a string of given length (wordcount)."""

	phrase = random.choice(words).strip()

	for i in range(1, wordcount):
		phrase = phrase + " " + random.choice(words).strip()

	return phrase

def para_gen():
	"""Generates a paragraph of sentences of random length with random punctuation."""

	punct = ['!', '?', ';', ',', ',', ',', ',', '.', '.', '.', '.', '.', '.', '.', '.']
	punc = '.'
	prev_punc = '.'

	paragraph = []	
	for i in range(5, random.randint(6, 30)):

		if prev_punc in ['!', '?', '.']:
			paragraph.append("%s%s " % (phrase_gen(random.randint(3, 15)).capitalize(), punc))
		else:
			paragraph.append("%s%s " % (phrase_gen(random.randint(3, 15)), punc))
		prev_punc = punc
		punc = random.choice(punct).strip()
	punc = '.'
	paragraph.append("%s%s\n\n" % (phrase_gen(random.randint(3, 15)).capitalize(), punc))
	
	return paragraph

def epilogue_gen(wordcount):
	"""Generates an epilogue of a given lenth, with just regular sentences."""

	sentence_length = []
	while wordcount >= 7:
		n = random.randint(3, 13)
		sentence_length.append(n)
		wordcount = wordcount - n
	sentence_length.append(wordcount)

	epilogue = []

	for i in sentence_length:
		epilogue.append("%s" % phrase_gen(i).capitalize())

	return epilogue

try:
	script, novel = argv
except ValueError:
	usage()

if exists(novel):
	print "'%s' exists, shall we wipe it? (Y,n)" % novel
	quit = raw_input("> ").lower()
	acquiesce = ['y', 'yes'] 

	if quit in acquiesce or not quit:
		open(novel, 'w').truncate()
	else:
		print "You appear to be experiencing writer's block. Goodbye."
		exit(0)

words = open("/usr/share/dict/words", 'r').readlines()
output = open(novel, 'w')

print "Locating quill..."
print "Furiously capturing stream of conciousness..."

book_title = phrase_gen(3).upper()
output.write("###%s\n" % book_title)
output.write("\n%s\n" % byline)
output.write("#####%s:\n" % toc)

remainder = remainder - len(book_title.split(" "))

table_contents = []
for i in range(1, random.randint(9, 13)):
	table_contents.append(phrase_gen(random.randint(1, 6)).upper())

remainder = remainder - len(table_contents)

for n, i in enumerate(table_contents):
	output.write("\t%2d%s %s  \n" % (n + 1, "." * 10, i))
	remainder = remainder - len(i.split(" "))

while remainder >= 500:
	paragraph = para_gen()
	for i in paragraph:
		output.write(i),
		remainder = remainder - len(i.strip().split(" "))

output.write("\n  \n#####%s  \n\n" % the_end)

output.write("%s:  \n\n" % epilogue_title)

epilogue = epilogue_gen(remainder)
for i in epilogue:
	output.write("%s. " % i)

print "Sending to publisher..."

output.close()

print "Congratulations! Your new masterpiece, %s,\nhas been listed atop the New York Times best sellers list!" % book_title
