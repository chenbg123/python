# 主页.     http;//www.renren.com/880151247/profile
# 人人登录url.  http://www.renren.com/PLogin.do
from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

def get_opener():
    # 1. 登录
    # 1.1 创建一个cookiejar 对象
    cookiejar=CookieJar()
    # 1.2 使用cookiejar 创建一个HTTPCookieProcessor对象
    handler=request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步的handler创建一个opener
    opener=request.build_opener(handler)
    # 1.4 使用opener 发送登录的请求（人人网·的邮箱和密码）
    return opener

def login_renren(opener):

    data={
        'email':'your renren"s email',
        'password':'your password'
    }
    url='http://www.renren.com/PLogin.do'
    req=request.Request(url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2. 访问个人主页
    url_s='http;//www.renren.com/880151247/profile'
    # 获取个人主页页面，不要新建opener, 之前openner已经包含之前登录的cookie信息
    req=request.Request(url_s,headers=headers)
    resp=opener.open(req)
    with open('renren.html','w',encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener=get_opener()
    login_renren(opener)
    visit_profile(opener)