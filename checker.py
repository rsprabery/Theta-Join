#!/usr/bin/env python

in_file = open('output.txt')
lines = set()
count = 0
for line in in_file:
  lines.add(line)
  count += 1

print "Count: %s" % count
print "Set: %s" % len(lines)
