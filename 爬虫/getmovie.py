import requests,bs4
from urllib.request import quote
moive = '水形物语'
gbkmovie = moive.encode('gbk')
urlmovie = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword='+quote(gbkmovie)
res = requests.get(urlmovie)
#print(type(res))
bsmovie = bs4.BeautifulSoup(res.text,'html.parser')
#print(type(bsmovie))
link = bsmovie.select('.co_content8 b a')
# print(type(link))
# print(len(link))
# print(type(link[0]))
finallink = 'http://www.ygdy8.com'+link[0].get('href')
#print(finallink)
xiazai = requests.get(finallink).content.decode('gbk')
bsxiazai = bs4.BeautifulSoup(xiazai,'html.parser')
download = bsxiazai.select('table tbody tr a')
print(download[0].get('href'))
print(download[1].get('href'))