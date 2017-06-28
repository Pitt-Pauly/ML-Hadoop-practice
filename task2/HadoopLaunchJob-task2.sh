# launch the job on the hadoop cluster
rm -r ~/exc/task2/output ~/exc/task2/output-Feats ~/exc/task2/output-Props 
#ssh hcrc1425n30 "hadoop fs -mkdir /user/s0836497/data/input/small /user/s0836497/data/input/second"
ssh hcrc1425n30 "hadoop fs -copyFromLocal ~/exc/files/small.txt /user/s0836497/data/input/"
ssh hcrc1425n30 "hadoop fs -rmr /user/s0836497/data/output /user/s0836497/data/input/*"
###### Task 2
#ssh hcrc1425n30 "hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
#-input /user/s0836497/data/input/small/ \
#-output /user/s0836497/data/output \
#-mapper FeaturesEmitter-mapper.py \
#-file ~/exc/task2/FeaturesEmitter-mapper.py \
#-reducer Features-reducer.py \
#-file ~/exc/task2/Features-reducer.py"

