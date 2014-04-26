#!/bin/bash
export HADOOP_HOME=/Users/read/software/hadoop-0.20.2

rm -rf ./output

hadoop jar ${HADOOP_HOME}/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -file ./mapper.py  -mapper ./mapper.py \
  -file ./reducer.py -reducer ./reducer.py \
  -input  ./*.csv \
  -output ./output
 
