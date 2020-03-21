import requests
import json
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
r = requests.get(url)
jsoner = json.loads(r.text)
print(type(r))
music = jsoner['data']['song']['list']  
for x in music:
#music是一个列表，x是它里面的元素
    print('歌名：'+x['name'])
    #以name为键，查找歌曲名。
    print('所属专辑：'+x['album']['name'])
    #查找专辑名
    print('播放时长：'+str(x['interval'])+'秒')
    #查找播放时长
    print('播放链接：https://y.qq.com/n/yqq/song/'+x['file']['media_mid']+'.html\n\n')
    #查找播放链接