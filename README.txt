Readme

There are totally 14 code files. And 3 text files - Taxis, Trips and initialization
- For Task 1 there are 3 files - mapper.py, reducer.py and Task1-run.sh
- For Task 2 there are 4 files - mapper2.py, reducer2.py, reader.py and Task2-run.sh
- For Task 3 there are 7 files - join_mapper.py, join_reducer.py, count_mapper.py, count_reducer.py, sort_mapper.py, sort_reducer.py and Task3-run.sh

For Tasks to run :
- copy the text files - Taxis and Trips to /Input after creating Input directory
hadoop fs -mkdir /Input 
hadoop fs -copyFromLocal ./Trips.txt /Input/ 
hadoop fs -copyFromLocal ./Taxis.txt /Input/ 

The output will be in /Output
hadoop fs -cat /Output/Task1/part*
hadoop fs -cat /Output/Task2/part*
hadoop fs -cat /Output/Task3/part*

For Task 1 to run you'll need the following files :
- Trips.txt, mapper.py, reducer.py and Task1-run.sh

For Task 2 to run you'll need the following files : 
- Trips.txt, Taxis.txt, mapper2.py, reducer2.py, reader.py and Task2-run.sh

For Task 3 to run you'll need the following files : 
- Trips.txt, Taxis.txt, join_mapper.py, join_reducer.py, count_mapper.py, count_reducer.py, sort_mapper.py, sort_reducer.py and Task3-run.sh