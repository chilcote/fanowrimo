#!/usr/bin/env python

import random

words = open("/usr/share/dict/words", 'r').readlines()
output = open("/tmp/tmpnovel", 'w')
for i in range(50000):
#	print(random.choice(words)).strip()
	output.write("%s " % random.choice(words).strip())
output.close()
