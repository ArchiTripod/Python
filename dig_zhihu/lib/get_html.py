import urllib.request
import os
import output_precheck

loginurl = 'http://www.zhihu.com/login'
#chrome下按F12呼出自带插件可以查看到需要的浏览器信息
headers = {
    'Accept':'*/*',
    #'Accept-Encoding':'gzip, deflate',
    #返回的数据是经过压缩的,客户端底层会再解码,所以不能加
    'Connection':'keep-alive',
    'Content-Length':'99',
    'Accept-Language':'en,zh-CN;q=0.8,zh;q=0.6,ja;q=0.4',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'host':'www.zhihu.com',
    'Referer':'http://www.zhihu.com/',}
print(headers)
org_postdata={
 '_xsrf': '54e31d7ed4c210ca320e04127bf422f1',
 'email': 'theforgived@163.com',
 'password': '1216235ztd',
 'rememberme':'y' 
}

def login_zhihu():
    """用来登陆知乎"""
    postdata = urllib.parse.urlencode(org_postdata).encode('utf-8')
    #把要传的数据转换成合适的编码
    #先告诉我要是url的->传送过成中还要知道utf-8的文本传输" data should be bytes!"
    req = urllib.request.Request(loginurl, postdata, headers)
    #浏览器识别自己是通过User-Agent头，所以在创建request请求时把模拟的浏览器头加入
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    if the_page is None:      
        return False
    with open(output_precheck.output,'wb') as f:
        #不知为什么，这里要采用byte方式写文件
        f.write(the_page);
    return True
login_zhihu()



