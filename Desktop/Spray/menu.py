import urllib
import urllib.request
access_token=''
baseurl='https://api.weixin.qq.com/cgi-bin/menu/create?access_token={0}'.format(access_token)
jsonstr={}

urlencode=urllib.parse.urlencode(jsonstr)
req=urllib.request.Request(url=baseurl,data=urlencode)
res=urllib.request.urlopen(req).read()
print(res)
