import os

output_name = '1.txt'
path = os.getcwd()

output_path = os.path.dirname(path) + os.sep + 'output'
if os.path.isdir(output_path):
    #如果存在路径，则万事大吉
    print("output_path:OK")
else:
    #如果不存在，创建路径
    os.mkdir(output_path)

output1 = output_path + os.sep + output_name

    
def mkfile(filename,content):
    filepath = output_path + os.sep + filename + ".html"
    with open(filepath,'w',encoding='utf-8') as f:
    #windows下新文件的默认编码是gbk，所以python解释器会用gkb编码去解释我们的网络数据流
    #因此这里要指定utf-8方式打开
        f.write(content)
    return

