#!/bin/bash

hadoop dfs -rmr /home/spraber2/mp3_output

hadoop jar ${HADOOP_HOME}/contrib/streaming/hadoop-0.19.0-streaming.jar \
         -D mapred.reduce.tasks=625 \
         -file ./mapper.py    -mapper ./mapper.py \
         -file ./reducer.py   -reducer ./reducer.py \
         -input /home/bendre1/yahoo/sample/part-r-00000.gz \
         -output /home/spraber2/mp3_output
         
