import io
import random
import sys
import requests
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# 初始化pos范围 10-55130
pos_list=[str(i)+"0" for i in range(1,5514)]
# 初始化url header
url = 'http://iframe.chinapost.com.cn/jsp/type/institutionalsite/SiteSearchJT.jsp?community=ChinaPostJT&pos='
headers = {
    'User-Agent':'PostmanRuntime/7.37.0'
}
for i in pos_list:
    url_i=url+i
    page=requests.get(url_i,headers=headers)
    page.encoding='utf-8'
    file_name='postoffice/post_pos_'+i+'.html'
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(page.text)
        f.close
    time.sleep(random.randint(7,15))