import requests
import urllib
class HTMLDownloader(object):
#下载网页
 def Download(self,url):
    if url is None:
        return

    sessions = requests.session()
    sessions.headers[
        'User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    r=sessions.get(url)
    r.raise_for_status()  # 如果状态不是200,引发HTTPError异常
    r.encoding = r.apparent_encoding
    #print(r.status_code)
    print(url)
   # print(r.headers)
    return r.text

