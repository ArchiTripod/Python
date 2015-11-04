import requests
from bs4 import BeautifulSoup
import re
def get_link(key):
#通过key构造形如“/collection/123456”、“/athour/123456”这样的正则表达式
    key_str = "/" + key + "/" + "\\d+$"
    return re.compile(key_str)

class Link:
    root_link = 'http://www.zhihu.com'
    link = ""
    __SESSION_HANDLE = None
    target = None
    soup = None
    @staticmethod
    def create_session(config):
        #Todo:创建session，这里以后应该可以穿登录所需要的参数(url,邮箱,密码 etc)
        Link.__SESSION_HANDLE = requests.Session()
        login = Link.__SESSION_HANDLE.post(config["login_link"],
           data={'_xsrf': BeautifulSoup(Link.__SESSION_HANDLE.get(config["root_link"]).content).find(type='hidden')['value'],
                 'email': config["email"], 'password':config["password"], 'rememberme': 'y'})
        if Link.__SESSION_HANDLE is None:
            print("Session has not been created.")
        else:
            print("Session has been created successfully!")
        
    def __init__(self , sub_link):
        self.link = self.root_link + sub_link
        self.access()
        print("Initialize link:{0}".format(self.link))
    
    def access(self, sub_link = None):
        if sub_link is None:
            sub_link = self.link
        print("Trying access link:{0}".format(sub_link))
        self.target = Link.__SESSION_HANDLE.get(sub_link)
        self.soup = BeautifulSoup(self.target.text)

    def get_sorted_targets(self,parten):
        if self.target is None:
             print("target does not exist")
             return None  
        print("self.target is {0}".format(self.target.text))
        return [link.get('href') for link in self.soup.find_all('a',href = parten)]
        

class Collection(Link):
    question_list = []
    total_page = 0
    
    def __init__(self, sub_link):
        Link.__init__(self, sub_link)
        __get_pageno()

    def __get_pageno(self):
        list_page_no = super.get_sorted_targets(re.compile('page=(\d+)'))
        self.total_page = max([ int(re_pageno.search(no).group(1)) for no in list_page_no ])
        print("collection\t: total page \t:",self.total_page)

    def get_question_list(self):
        page_no = 1
        while True:
            list_question_link = super.get_sorted_targets(get_link('question'))
            if list_question_link:
                question_list.extend(list_question_link)
                print(page_no,":",list_question_link)
                i += 1
                if page_no > self.total_page:
                    return
                link = self.link + "?page=" + str(page_no)
                super.access(link)
                question_list.extend(super.get_sorted_targets(get_link('question')))
                
#class question(link):   
    
