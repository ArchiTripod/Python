from numpy import *
#import numpy as np
import operator
from os import listdir

COMMENT_SHARP_LEFT = ">>>>---->>>> "
COMMENT_SHARP_RIGHT = "<<<<----<<<< "

print("""
######function here we get:
####tile():Construct an array by repeating A reps times
####argsort():returns the indices that would sort an array in a ascending order 
""")

def createDataSet():
    group = array([[1.0 , 1.1],
                   [1.0 , 1.0],
                   [0   , 0  ],
                   [0   , 0.1],])
    #only 2 non-keyword arguments accepted,so two labels "[]" is necessary
    labels = ['A','A','B','B']
    #including information for every data node
    return group, labels

def classify0(inX, dataSet, labels, k):
    print(COMMENT_SHARP_LEFT+"""THE INPUT STARTS:
inX: #vector to compare to existing dataset (1xN) 
{0}
dataSet: #size m data set of known vectors (NxM)
{1}
labels: #data set labels (1xM vector)
{2}
k: #number of neighbors to use for comparison 
{3}
""".format(inX, dataSet, labels, k)+COMMENT_SHARP_RIGHT+"THE INPUTS ENDS")
    dataSetSize = dataSet.shape[0]# shape[0] stands for the num of row
    print("the num of row in dataSet(dataSet.shape[0]):", dataSetSize)

    print(COMMENT_SHARP_LEFT+"STEP 1: calculate Euclidean distance")
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy numSamples rows for dataSet
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    print("the diff matrix:\n",diffMat)
    sqDiffMat = diffMat**2
    print("the quare diff matrix:\n",sqDiffMat)
    sqDistances = sqDiffMat.sum( axis = 1 )
    #"axis = 1" means Axis or axes along which a sum is performed, negative OK
    print("the quare disatance matrix:\n",sqDistances)
    distances = sqDistances**0.5
    print(COMMENT_SHARP_LEFT+"STEP 2: sort the distance"+COMMENT_SHARP_RIGHT)
    sortedDistIndicies = distances.argsort()
    # argsort() returns the indices that would sort an array in a ascending order 
    print("the sorted disatance matrix:\n",sortedDistIndicies)
    classCount = {}
    print(COMMENT_SHARP_LEFT+"STEP 3: choose the min k distance"+COMMENT_SHARP_RIGHT)
    for i in range(k):# define a dictionary (can be append element)
        voteIlabel = labels[sortedDistIndicies[i]]
        print(i,":",voteIlabel)
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print(COMMENT_SHARP_LEFT+"STEP 4: count the times labels occur"+COMMENT_SHARP_RIGHT)
    print("classCount:",classCount)
    print("classCountitems():",classCount.items())
    print(COMMENT_SHARP_LEFT+"STEP 5: the max voted class will return"+COMMENT_SHARP_RIGHT)
    sortedClassCount = sorted(classCount.items(),
                              key = operator.itemgetter(1),
                              reverse = True)
    #the way sort the keylist is so essential that should get used to it!
    #sorted(iterable[, key][, reverse])
    #key specifies a function of one argument that is used to extract a comparison key
    #from each list element: key=str.lower. The default value is None (compare the
    #elements directly).
    return sortedClassCount[0][0]

print("""
######function here we get:
####zeros():
####strip():
####comma in slice operator(see demo_array_slice.py in memo_numpy )
""")
def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        #get the the [index]th row from the listFromLine[0:3]
        returnMat[index,:] = listFromLine[0:3]
        #the meaning of comma in array's slice operator  
        #       >>> print a[:,:]
        #       [[0 1 2]
        #       [3 4 5]
        #       [6 7 8]]
        #[:] with no arguments is the same as [:] for lists --
        #it can be read ``all indices along this axis''. (Actually, there is an important
        #distinction; see below.) So, to get the second row along the second dimension:
        #       >>> print a[:,1]
        #       [1 4 7]
        #Note that what was a ``column'' vector is now a ``row'' vector any ``integer slice''
        #(as in the 1 in the example above) results in a returned array with rank one less
        #than the input array. There is one important distinction between slicing arrays and
        #slicing standard Python sequence objects. 
        classLabelVector.append(listFromLine[-1])
        index += 1
    return returnMat,classLabelVector

def autoNorm(dataSet):
    #dataSet.min(0) get the min/max in every single column
    #dataSet.min(1) get the min/max in every single raws
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, ( m, 1))
    normDataSet = normDataSet / tile(ranges, ( m , 1))
    return normDataSet, ranges, minVals
