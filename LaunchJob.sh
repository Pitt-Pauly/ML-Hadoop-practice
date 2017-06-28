### ----------------- Task 2 ------------------ ###
# uses a slightly modified version of FeatureEmitter-mapper.py to get
# the features of the words
# Probability-mapper sums those features, counts them and emits them in
# a suitable form for the Probabilty-reducer.py to digest. 
# Probability-reducer.py is used to calculate p(fi|l)
# output of the reducer is the individual p(fi|l) per feature 
#
## transfer mapper, reducer and job config file to the server
#scp ./task2/FeaturesEmitter-mapper.py ./task2/Features-reducer.py ./task2/HadoopLaunchJob-task2.sh s0836497@ssh.inf.ed.ac.uk:~/exc/task2/
## initiate the hadoop job:
#ssh s0836497@ssh.inf.ed.ac.uk "(rm -r ~/exc/task2/output);(sh ~/exc/task2/HadoopLaunchJob-task2.sh)"
#scp -r s0836497@ssh.inf.ed.ac.uk:~/exc/task2/output-Feats ./task2/

### ---------------- Task 3 ------------------ ###
# uses FeaturesEmitter-mapper.py to create frequencies 
# and simple summer reducer
#
## transfer Mapper file and job config file to the server
#scp ./task3/FeaturesEmitter-mapper.py ./task3/task3-Features-reducer.py ./task3/HadoopLaunchJob-task3.sh s0836497@ssh.inf.ed.ac.uk:~/exc/task3/
#ssh s0836497@ssh.inf.ed.ac.uk "(rm -r ~/exc/task4/test-file-features);(sh ~/exc/task3/HadoopLaunchJob-task3.sh)"
#scp -r s0836497@ssh.inf.ed.ac.uk:~/exc/task3/output ./task3/
#scp -r s0836497@ssh.inf.ed.ac.uk:~/exc/task4/test-file-features ./task4/

### ---------------- Task 4 ------------------ ###
scp -r ./task4/TrainingSet ./task4/test-file-features ./task4/Task4-mapper.py ./task4/Task4-reducer.py ./task4/HadoopLaunchJob.sh s0836497@ssh.inf.ed.ac.uk:~/exc/task4/
ssh s0836497@ssh.inf.ed.ac.uk "(rm -r ~/exc/task4/CapitalizedOutput/*);(sh ~/exc/task4/HadoopLaunchJob.sh)"
scp -r s0836497@ssh.inf.ed.ac.uk:~/exc/task4/CapitalizedOutput ./task4/CapitalizedOutput





