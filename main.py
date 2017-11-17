# *_* coding:utf-8 *_*
#!/usr/bin/python
import urllib2
import time
import json
import initmysql
import socks
import socket
from stem import Signal
from stem.control import Controller
controller=Controller.from_port(port=9151)
controller.authenticate()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9150)
socket.socket=socks.socksocket


def getHtml(url, count=5):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',

        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',

        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    }
    try:
        req = urllib2.Request(url,headers=header)
        html = urllib2.urlopen(req,timeout=5).read()
        return html
    except:
        count -= 1
        if count >= 0:
            getHtml(url, count)


while True:

    ti=str(time.time()).split(".")[0]
    url = 'https://live.dszuqiu.com/ajax/score/data?mt='+ti

    html=getHtml(url)
    data=json.loads(html)
    t1=time.time()
    initmysql.initMysql(data)
    #time.sleep(10)
    controller.signal(Signal.NEWNYM)
    time.sleep(controller.get_newnym_wait())
    t2=time.time()

    with open(r'log.txt','a+') as f:
        f.writelines(time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())+"  "+u"用时:"+str(t2-t1)+'\n')

