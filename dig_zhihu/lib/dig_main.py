import dig_byrequests as dig
config = {
    "root_link" : "http://www.zhihu.com",
    "login_link" : 'http://www.zhihu.com/login',
    "email" : 'theforgived@163.com',
    "password" : '1216235ztd',
    }
dig.Link.create_session(config)
mine_collections = dig.Link("/collections/mine")
print(mine_collections.get_sorted_targets(dig.get_link('collection')))
