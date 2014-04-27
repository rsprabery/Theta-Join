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

  # ignore if there are no clicks
  if '1' in columns[3]:
    output.append(columns[0]) # ymdh
    output.append(columns[1]) # user_id
    output.append(columns[3]) # clicks
    output.append(columns[19]) # query_string

    # Since this is a self join, then x is in both S & T

    # S part
    matrixRowS = random.randint(1, height)
    begin_S_ID = (matrixRowS * (matrixRowS -1)) + 1
    # ERROR HERE
    end_S_ID = (matrixRowS * (matrixRowS)) + 1
    #rowSIDS = range(begin_S_ID, end_S_ID)

    rowSIDS = range((matrixRowS -1) * width + 1, matrixRowS * width + 1)

    for region_id in rowSIDS:
      print '%s\t%s,S' % (region_id, ','.join(output))

    # T Part
    rows = range(1, height)
    matrix_column = random.randint(1, width)
    column_T_ids = []
    for row in rows:
      region_id = ((row - 1) * width) + matrix_column
      column_T_ids.append(region_id)

    for region_id in column_T_ids:
      print '%s\t%s,T' % (region_id, ','.join(output))

