#!/bin/bash


HADOOP_CMD="/usr/local/hadoop/bin/hadoop"
STREAM_JAR_PATH="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"

$HADOOP_CMD fs -mkdir -p /booklist

$HADOOP_CMD fs -put ./The_Man_of_Property.txt /booklist

INPUT_FILE_PATH_1="/booklist/The_Man_of_Property.txt"

OUTPUT_PATH="/output"

$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python map_new.py" \
    -reducer "python red_new.py" \
    -file ./map_new.py \
    -file ./red_new.py

