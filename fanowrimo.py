#!/usr/bin/env python

from sys import argv
from os.path import exists
import random

script, novel = argv

def title_gen(wordcount):
	title = random.choice(words).title().strip()
	for i in range(1, wordcount):
		title = title + " " + random.choice(words).title().strip()
	return title.upper()

if exists(novel):
	print "%s exists, shall we wipe it? (RETURN, CTRL-C)" % novel
	raw_input("> ")
	open(novel, 'w').truncate()

words = open("/usr/share/dict/words", 'r').readlines()
output = open(novel, 'w')

print "Locating quill..."
print "Furiously capturing stream of conciousness..."

book_title = title_gen(3)
output.write("###%s " % book_title)
output.write("\na novel by Ernst Hummingway\n")
output.write("#####Table of Contents:\n")

table_contents = {}
for i in range(1, 13):
	table_contents[i] = title_gen(random.randint(1, 6))
	output.write("\t%2d........... %s  \n" % (i, table_contents[i]))

output.write("\n__%s__ " % random.choice(words).upper().strip())

for i in range(50000):
	output.write("%s " % random.choice(words).strip())

output.write("%s. " % random.choice(words).strip())
output.write("\n  \n#####THE END  ")

print "Sending to publisher..."
output.close()
print "\nCongratulations! Your new novel, %s,\nhas been listed atop the New York Times best sellers list." % book_title

