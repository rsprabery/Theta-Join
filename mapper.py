#!/usr/bin/env python

import sys
import random
# 625 unique regions
height = 25 
width = 25 
regionIDS = range(1, (height*width) + 1)

# input comes from STDIN (standard input)
for line in sys.stdin:
  random.seed()
  # remove leading and trailing whitespace
  line = line.strip()
  # split the line into words
  columns = line.split(',')
  output = []
  output.append(columns[0])
  output.append(columns[1])
  output.append(columns[3])
  output.append(columns[19])

  # Since this is a self join, then x is in both S & T

  # S part
  matrixRowS = random.randint(1, height)
  begin_S_ID = (matrixRowS * (matrixRowS -1)) + 1
  # ERROR HERE
  end_S_ID = (matrixRowS * (matrixRowS)) + 1
  #rowSIDS = range(begin_S_ID, end_S_ID)

  rowSIDS = range((matrixRowS -1) * width + 1, matrixRowS * width + 1):

  for id in rowSIDS:
    print '%s\t%s\tS' % (id, '\t'.join(output))

  # T Part
  rows = range(1, height)
  matrix_column = random.randint(1, width)
  column_T_ids = []
  for row in rows:
    id = ((row - 1) * width) + matrix_column
    column_T_ids.append(id)

  for id in column_T_ids:
    print '%s\t%s,T' % (id, '\t'.join(output))

