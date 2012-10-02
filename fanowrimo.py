#!/usr/bin/env python

""" fanowrimo.py
	by Joseph Chilcote
	chilcote@gmail.com
	last modified: 2012-9-30 """

from sys import argv
from sys import exit
from os.path import exists
import random

script, novel = argv

byline = "a novel by Ernst Hummingway"
toc = "Table of Contents"
the_end = "THE END"
remainder = 50000 - len(byline.split(" ")) - len(toc.split(" ")) - len(the_end.split(" "))

def title_gen(wordcount):
	"""Generates a string of given length (wordcount), using Title Case."""
	title = random.choice(words).title().strip()
	for i in range(1, wordcount):
		title = title + " " + random.choice(words).title().strip()
	return title.upper()

if exists(novel):
	print "'%s' exists, shall we wipe it? (Y,n)" % novel
	quit = raw_input("> ").lower()
	acquiesce = ['y', 'yes'] 
	if quit in acquiesce or not quit:
		open(novel, 'w').truncate()
	else:
		print "You appear to be experiencing writer's block. Goodbye."
		exit(1)

words = open("/usr/share/dict/words", 'r').readlines()
output = open(novel, 'w')

print "Locating quill..."
print "Furiously capturing stream of conciousness..."

book_title = title_gen(3)
output.write("###%s " % book_title)
output.write("\n%s\n" % byline)
output.write("#####%s:\n" % toc)

remainder = remainder - len(book_title.split(" "))

table_contents = []
for i in range(1, random.randint(9, 13)):
	table_contents.append(title_gen(random.randint(1, 6)))

remainder = remainder - len(table_contents)

for n, i in enumerate(table_contents):
	output.write("\t%2d%s %s  \n" % (n + 1, "." * 10, i))
	remainder = remainder - len(i.split(" "))

output.write("\n__%s__ " % random.choice(words).upper().strip())

remainder = remainder - 2

for i in range(remainder):
	output.write("%s " % random.choice(words).strip())

output.write("%s. " % random.choice(words).strip())
output.write("\n  \n#####%s  " % the_end)

print "Sending to publisher..."

output.close()

print "Congratulations! Your new masterpiece, %s,\nhas been listed atop the New York Times best sellers list." % book_title

