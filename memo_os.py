import os

#获取当前路径
path=os.getcwd()
print("os.getcwd(): ",path)
#想获取当前的路径的上一级路径的集中方法
print("os.path.dirname(path): ",os.path.dirname(path))

#os.path.dirname(path)获取了path所在的路径，其实是split()函数返回值的第一个参数
#会将给予的路径分成head[末尾目录名]+tail[其他剩余部分]两部分
#注意path不要以slash(斜杠)结尾，否则tail将会为空
print(os.path.split(path))

