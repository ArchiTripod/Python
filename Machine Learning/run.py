import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

group, labels = kNN.createDataSet()
#print(kNN.group)
#print(kNN.labels)

#print(kNN.classify0([0,0],group,labels,3))

#datingDataMat,datingLabels = kNN.file2matrix('datingTestSet.txt')
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
print("+++++++++++++++++++++++++++++++++")
print("datingDataMat",datingDataMat)
print("+++++++++++++++++++++++++++++++++")
print("datingDataMat[:,1]",datingDataMat[:,1])
print("+++++++++++++++++++++++++++++++++")
#display data graph
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],
           s = 15.0*array(datingLabels).astype(float),
           #astype(float):Copy of the array, cast to a specified type.
           c = 15.0*array(datingLabels).astype(float))
plt.show()
#normData
normMat, ranges, minVals =  kNN.autoNorm(datingDataMat)
print(normMat)
print(ranges)
print(minVals)

