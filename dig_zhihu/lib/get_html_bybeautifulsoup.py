import requests
from bs4 import BeautifulSoup
import output_precheck
import re
import output_precheck

#todolit：
#1.在实现功能的基础上，做到处理逻辑与代码的分离
#2.实现更新功能，在1.的基础上，实现先得到整个collection的所有question列表，
#  和现有文件夹下已有的问题进行对比，如果没有该元素，再去在去 访问question
url_base = 'http://www.zhihu.com'
def get_link(key):
#通过key构造形如“/collection/123456”、“/athour/123456”这样的正则表达式
    key_str = "/" + key + "/" + "\\d+$"
    return re.compile(key_str)


def dig_collection_infomation(s, sub_link):
#先得到总的分页页数
#给定一个子字符串，自动的转换成知乎全url，并从链接中迭代地读取需要的信息，读完为止
#首先考虑牵涉到分页问题：
#问题链接就是形如：<a target="_blank" href="/question/19716102">这样的内容
    link = url_base + sub_link
    target = s.get(link).text
    soup = BeautifulSoup(target)
    re_pageno = re.compile('page=(\d+)')
    pageno_max = 1
    list_question = []
    list_page_no = [link.get('href') for link in soup.find_all('a',href = re_pageno)]
    #形如这样的循环写法是一个简洁的样子
    print(sub_link,":",list_page_no)
    if  list_page_no:
        total_page = max([ int(re_pageno.search(no).group(1)) for no in list_page_no ])
    print("total page",":",total_page)
    page_no = 1
    while True:
        list_question_link = [link.get('href') for link in soup.find_all('a',href = get_link("question"))]
        print(sub_link,":",list_question_link)
        for question_link in list_question_link:
            dig_question_infomation(s,question_link)
        page_no += 1
        if(page_no > total_page):
            break
        link = url_base + sub_link + "?page=" + str(page_no)
        target = s.get(link).text
        soup = BeautifulSoup(target)
        
def dig_question_infomation(s, sub_link):
    link = url_base + sub_link 
    target = s.get(link).text 
    output_precheck.mkfile(re.match(r'.*/(\d+)',sub_link).group(1),target)
    print("dig:",sub_link)

    
s = requests.Session()
login = s.post('http://www.zhihu.com/login',
           data={'_xsrf': BeautifulSoup(s.get('http://www.zhihu.com/').content).find(type='hidden')['value'],
                 'email': 'theforgived@163.com', 'password': '1216235ztd', 'rememberme': 'y'})

collection = s.get('http://www.zhihu.com/collections/mine')
target = collection.text
if target:
    print("target exists")
#所有的操作都要在同一个session下才能保证成功
#with open(output_precheck.output1,'w') as f:
    #不知为什么，这里要采用byte方式写文件
#    f.write(target)
soup = BeautifulSoup(target)
list_collection_link = [link.get('href') for link in soup.find_all('a',href = get_link("collection"))]
#for collection_link in list_collection_link:
#    dig_collection_infomation(s,collection_link)
print("there is",len(list_collection_link),"hrefs：", list_collection_link)
#print("start dig list_collection_link[1]:",list_collection_link[1])
#dig_collection_infomation(s,list_collection_link[2])
    
