# 🚖 Big Data Processing: Taxi Trip Statistics

![Hadoop](https://img.shields.io/badge/Hadoop-3.1.4-blue?logo=apache) ![Python](https://img.shields.io/badge/Python-3.8+-yellow?logo=python) ![MapReduce](https://img.shields.io/badge/MapReduce-Streaming-green)

## 📌 Overview
This project implements **MapReduce programs** using Python to process taxi trip data on **Hadoop**. The goal is to analyze taxi trip statistics, perform clustering, and rank taxi companies based on trip counts.

## 📂 Datasets
Two datasets stored in **HDFS**:
1. **Trips.txt** - Contains taxi trip details.
2. **Taxis.txt** - Contains taxi information.

### Example Data
#### 🚕 Taxis.txt
Taxi#, company, model, year
470,0,80,2018 332,11,88,2013

#### 📌 Trips.txt
Trip#, Taxi#, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y 
0,354,232.64,127.23,46.069,85.566,10.355,4.83


## 🚀 Tasks Implemented
### Task 1: Trip Statistics (5 Marks)
- Categorize trips into **short (<100 km), medium (100-200 km), and long (>200 km)**.
- Compute:
  - **Total trips per category**
  - **Max, min, and average fare**
- Implements **in-mapper combining**.

🔹 **Scripts**:
- `mapper.py` - Categorizes trips and outputs fares.
- `reducer.py` - Aggregates trip statistics.
- `Task1-run.sh` - Executes the task.

### Task 2: K-Medoid Clustering (10 Marks)
- Cluster trips based on **drop-off locations** using the **Partitioning Around Medoids (PAM)** algorithm.
- Works for **different k and iteration values**.

🔹 **Scripts**:
- `mapper2.py` - Assigns trips to the nearest medoid.
- `reducer2.py` - Updates medoids.
- `reader.py` - Checks convergence.
- `Task2-run.sh` - Runs clustering iteratively.

### Task 3: Taxi Company Ranking (10 Marks)
- Rank taxi companies by **total trips**.
- **Subtasks**:
  1. **Join operation** - Merge `Taxis.txt` & `Trips.txt`.
  2. **Counting operation** - Count trips per company.
  3. **Sorting operation** - Sort companies in ascending order.

🔹 **Scripts**:
- `join_mapper.py` & `join_reducer.py`
- `count_mapper.py` & `count_reducer.py`
- `sort_mapper.py` & `sort_reducer.py`
- `Task3-run.sh` - Runs all subtasks sequentially.

## ⚙️ Setup & Execution
### Prerequisites
- **Hadoop 3.1.4**
- **Python 3.8+**
- HDFS with input files:
  - `/Input/Trips.txt`
  - `/Input/Taxis.txt`

### Running the Tasks
```sh
bash Task1-run.sh   # Run Task 1
bash Task2-run.sh   # Run Task 2
bash Task3-run.sh   # Run Task 3
