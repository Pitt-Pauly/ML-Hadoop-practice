# launch the job on the hadoop cluster
ssh hcrc1425n30 "hadoop fs -rmr /user/s0836497/data/input/* /user/s0836497/data/output"
ssh hcrc1425n30 "hadoop fs -copyFromLocal ~/exc/files/small.txt /user/s0836497/data/input/"
#ssh hcrc1425n30 "hadoop fs -rmr /user/s0836497/data/output"
ssh hcrc1425n30 "hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
-input /user/s0836497/data/input/ \
-output /user/s0836497/data/output \
-mapper FeaturesEmitter-mapper.py \
-file ~/exc/task3/FeaturesEmitter-mapper.py \
-reducer task3-Features-reducer.py \
-file ~/exc/task3/task3-Features-reducer.py"
#ssh hcrc1425n30 "hadoop fs -copyToLocal /user/s0836497/data/output ~/exc/task3/"
ssh hcrc1425n30 "hadoop fs -copyToLocal /user/s0836497/data/output ~/exc/task4/test-file-features/"
