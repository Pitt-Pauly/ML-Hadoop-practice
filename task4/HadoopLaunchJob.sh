# launch the job on the hadoop cluster
# run task 3 on the target file to create feature sets
#ssh hcrc1425n30 "hadoop fs -copyFromLocal ~/exc/task4/test-file-features/* /user/s0836497/data/input"
#ssh hcrc1425n30 "hadoop fs -copyFromLocal ~/exc/task4/TrainingSet/* /user/s0836497/data/input"
ssh hcrc1425n30 "hadoop fs -rmr /user/s0836497/data/output"
ssh hcrc1425n30 "hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
-input /user/s0836497/data/input/ \
-output /user/s0836497/data/output \
-mapper Task4-mapper.py \
-file ~/exc/task4/Task4-mapper.py \
-reducer Task4-reducer.py \
-file ~/exc/task4/Task4-reducer.py"
ssh hcrc1425n30 "hadoop fs -copyToLocal /user/s0836497/data/output ~/exc/task4/CapitalizedOutput/"
