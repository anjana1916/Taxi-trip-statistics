#!/bin/bash
# Set the number of reduce tasks - we're using 3 here
# The fields is to tell Hadoop that our key that is the output from the mapper has two parts: taxi_id and trip_type
# The partitioner to use both parts of our key (taxi_id and trip_type) when deciding which reducer should process each record
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-D stream.num.map.output.key.fields=2 \
-D mapred.text.key.partitioner.options=-k1,2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file ./mapper.py \
-mapper "python3 ./mapper.py" \
-file ./reducer.py \
-reducer "python3 ./reducer.py" \
-input /Input/Trips.txt \
-output /Output/Task1








