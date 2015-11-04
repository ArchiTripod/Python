import kNN
from numpy import *
print("""The standard rules of Python slicing apply to arrays, on aper-dimension
basis. Assuming a 3x3 array:""")
a = reshape(arange(9),(3,3))
print(a)

print("The plain [:] operator slices from beginning to end:")
print(a[:,:])

print("""In other words, [:] with no arguments is the same as [:] for lists --
it can be read ``all indices along this axis''. (Actually, there is animportant
distinction; see below.) So, to get the second row along thesecond dimension:""")

print("a[1] is\n",a[1])

print("a[1:] is\n",a[1:])

print("a[1,:] is\n",a[1,:])

print("a[,1:] is not allowed")

print("a[:1] is\n",a[:1])

print("a[:1,] is\n",a[:1,])

print("a[:2,] is\n",a[:2,])

print("a[:,0] is\n",a[:,0])

print("a[:,1] is\n",a[:,1])

print("a[:,2] is\n",a[:,2])

index = 0
b = zeros((shape(a)[0],2))
print("before copy b is\n",b)
for raw in a:
    print("raw",index,raw[0:2],type(raw))
    b[index,:] = raw[0:2]
    index += 1
print("after copy b is\n",b,)
print("b[:1,1] is\n",b[:1,1],type(b[:1,1]))
