#!/bin/bash


echo "hello world"


#head -2 ../../data/The_Man_of_Property.txt | python map_new.py | sort | python red_new.py | wc -l
cat ../../data/The_Man_of_Property.txt | python map_new.py | sort | python red_new.py | wc -l

