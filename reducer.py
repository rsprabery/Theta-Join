#!/usr/bin/env python

from operator import itemgetter
from datetime import datetime
import sys

s_tupes = set()
t_tupes = set()
#output = set()

# input comes from STDIN
for line in sys.stdin:
    #line = line.strip()

    # parse the input we got from mapper.py
    #id, ymdh, user_id, clicks, query_string, origin = line.split(',')
    region_id, value = line.split('\t')
    ymdh, user_id, clicks, query_string, origin = value.split(',')
    x = "%s,%s,%s,%s" % (ymdh, user_id, clicks, query_string)
    #print "origin: %s" % (origin)
    if 'S' in origin:
      s_tupes.add(x)
    else:
      t_tupes.add(x)

#s_tupes = list(s_tupes)
#t_tupes = list(t_tupes)
for s in s_tupes:
  for t in t_tupes:
    s_ymdh, s_user_id,  s_clicks, s_query_string = s.split(',')
    t_ymdh, t_user_id,  t_clicks, t_query_string = t.split(',')
    #print "CLICKS: %s, %s" % (s_clicks, t_clicks)
    if '1' in s_clicks and '1' in t_clicks:
      #print "COUNT FOUND"
      if s_user_id != t_user_id:
        #print "different ids found"
        s_time = datetime.strptime(s_ymdh, '%Y-%m-%d %H:%M:%S')
        t_time = datetime.strptime(t_ymdh, '%Y-%m-%d %H:%M:%S')
        #s_sec = s_ymdh.split(' ')[1].split(':')[-1]
        #t_sec = t_ymdh.split(' ')[1].split(':')[-1]
        #if abs(int(s_sec) - int(t_sec)) < 2:
        if  datetime.timedelta(seconds=-2) < s_time - t_time < datetime.timedelta(seconds=2):
          #print "other found"
          #output.add("%s,%s,%s" % (s_ymdh, s_query_string, t_query_string))
          print "%s,%s,%s" % (s_ymdh, s_query_string, t_query_string)

#for x in output:
  #print x 

#print "s_tupes"
#print s_tupes

#print "t_tupes"
#print t_tupes
