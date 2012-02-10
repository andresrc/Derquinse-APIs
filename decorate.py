# API File Decorator

import fnmatch
import os

# Read snippet
f = open('gatc1.txt', 'r')
gatc1 = f.read()
f.close()


# Fetch files names to analyze
files = []
for root, dirnames, filenames in os.walk('.'):
	for filename in fnmatch.filter(filenames, '*.html'):
		files.append(os.path.join(root, filename))

begin = '<!-- Begin GATC1 -->'
chead = '</HEAD>'
sub = gatc1 + chead

for file in files:
	f = open(file, 'r')
	text = f.read()
	f.close()
	if text.find(begin) >= 0:
		print 'Leaving %s unmodified...' % file
	else:
		r = text.replace(chead, sub, 1)
		print 'Inserting GATC1 in %s...' % file
		f = open(file, 'w')
		f.write(r)
		f.close()


