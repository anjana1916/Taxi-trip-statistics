#!/bin/bash

# I read the number of iterations from initialization.txt. We copy the initilaization.txt to medoid.txt and remove the first line
# as it has the interation which is not required
v=$(head -n 1 initialization.txt)
cp initialization.txt medoid.txt
sed -i '1d' medoid.txt

# Here we pass medoid.txt. The mapper uses medoid.txt. Once new_medoids.txt is created we check if the values have converged. If not we continue the iteration 
# or else we stop the iteration and save the values to a text file finally.
i=1
while [ $i -le $v ]
do
    hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=3 \
    -D mapred.text.key.partitioner.options=-k1 \
    -file medoid.txt \
    -file ./mapper2.py \
    -mapper "python3 ./mapper2.py" \
    -file ./reducer2.py \
    -reducer "python3 ./reducer2.py" \
    -input /Input/Trips.txt \
    -output /mapreduce-output$i \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

    hadoop fs -getmerge /mapreduce-output$i/part-* new_medoids.txt

    converged=$(python reader.py)

    if [ $converged -eq 1 ]
    then
        echo "Clustering converged after $i iterations"
        hadoop fs -mkdir -p /Output/Task2
        hadoop fs -cp /mapreduce-output$i/part-* /Output/Task2/ # here we copy the final reslts after converging to Task2 directory inside output
        break
    else
        cp new_medoids.txt medoid.txt # here we are updating the medoid.txt with the new_medoids since its not converged.
    fi

    i=$((i+1))
done

# Copy the final results to a local file
hadoop fs -getmerge /mapreduce-output$i/part-* final_clusters.txt

echo "Clustering completed. Results are in final_clusters.txt"