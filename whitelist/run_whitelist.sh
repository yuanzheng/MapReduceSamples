#!/bin/bash

HADOOP_CMD="/usr/local/hadoop/bin/hadoop"
STREAM_JAR_PATH="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"

hdfs dfs -mkdir -p /booklist
hdfs dfs -put ../data/The_Man_of_Property.txt /booklist

INPUT_FILE_PATH_1="/booklist/The_Man_of_Property.txt"
OUTPUT_PATH="/output_cachearchive_broadcast"

$HADOOP_CMD fs -rm -r -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -D mapred.reduce.tasks=3 \
    -D "stream.non.zero.exit.is.failure=false" \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map.py mapper_func white_list.txt" \
    -reducer "python reduce.py reduce_func" \
    -file "./map.py" \
    -file "./reduce.py" \
    -file "./white_list.txt"


#-jobconf "mapred.reduce.tasks=3" \
