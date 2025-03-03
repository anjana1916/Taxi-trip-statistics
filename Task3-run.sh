#!/bin/bash

#Subtask 1 - Join operation
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-file ./join_mapper.py \
-mapper "python3 ./join_mapper.py" \
-file ./join_reducer.py \
-reducer "python3 ./join_reducer.py" \
-input /Input/Trips.txt \
-input /Input/Taxis.txt \
-output /Output/join_output

#Subtask 2 - Counting operation
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-file ./count_mapper.py \
-mapper "python3 ./count_mapper.py" \
-file ./count_reducer.py \
-reducer "python3 ./count_reducer.py" \
-input /Output/join_output \
-output /Output/count_output

#Subtask 3 - Sorting operation
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-file ./sort_mapper.py \
-mapper "python3 ./sort_mapper.py" \
-file ./sort_reducer.py \
-reducer "python3 ./sort_reducer.py" \
-input /Output/count_output \
-output /Output/Task3


# delete the intermediate results
hadoop fs -rm -r /Output/join_output
hadoop fs -rm -r /Output/count_output