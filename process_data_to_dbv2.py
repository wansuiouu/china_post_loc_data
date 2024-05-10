import sys
import io
import pandas as pd
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
'''
读取html文件，返回html文本数据
'''
def pre_read_html(file_name):
    html_text=""
    with open(file_name, 'r',encoding='utf-8') as f:
        for line in f:
            html_text+=line
        f.close()
    return html_text

'''

读取html文本，返回dataframe
'''
def parse_html_to_df(html_text):
    soup = BeautifulSoup(html_text,'lxml')
    content = soup.select('.wangd2')[0]
    p_content=content.prettify()
    p_soup = BeautifulSoup(p_content,'lxml')
    p_soup_list=[]
    for i in range(1,11):
        p_soup=soup.select('td')[11+i*9]
        p_soup_list.append(str(p_soup))
    tbl = pd.read_html(p_content)
    table_data = tbl[0]
    return table_data,p_soup_list
def process_time(time_list):
    time_s_list=[]
    time_h_list=[]
    for time in time_list:
        time=str(time)
        time_h=time.replace('<img src="/tea/image/other/xz.png"/>','').replace('<img src="/tea/image/other/wxz.png"/>','')
        time_h=time_h[time_h.find('<br/>'):-5]
        time_h=time_h[5:]
        time_h_list.append(time_h)
        time_s=time.replace('<td align="center">','').replace('</td>','')[:time.find('<br/>')].replace('<img src="/tea/image/other/xz.png"/>',';').replace('<img src="/tea/image/other/wxz.png"/>',';!')[1:].split(';')
        time_flag=''
        for i in range(len(time_s)):
            if('!' in time_s[i]):
                time_flag+='0,'
            else:
                time_flag+='1,'
        time_s_list.append(time_flag[:-1])
    return time_s_list,time_h_list
time_sql='insert into china_post_office (`sheng`, `shi`, `xian`, `name`, `post_code`, `address`, `finance`, `phone`,`time_s`,`time_h`) values'
range_list = [str(i)+"0" for i in range(1,5514)]
with open('dml/post_sql_to_dbv2.sql','w',encoding='utf-8') as f:
    for file_index in range_list:
        if(file_index.find("000")!=-1):
            print("1000")
        file_name='postoffice/post_pos_'+file_index+'.html'
        table_data,p_time_soup_list=parse_html_to_df(pre_read_html(file_name))
        time_s_list,time_h_list=process_time(p_time_soup_list)
        for row_index in range(1,11):
            sql_str=time_sql+"("
            for col_index in range(0,9):
                if(col_index==(len(table_data.columns)-2)):
                    sql_str+=('\''+table_data.iloc[:,7][col_index+1]+'\',')
                    sql_str+=('\''+time_s_list[row_index-1]+'\',')
                elif(col_index==(len(table_data.columns)-1)):
                      sql_str+=('\''+time_h_list[row_index-1]+'\',')
                else:
                    sql_str+=('\''+table_data.iloc[row_index][col_index]+'\',')
            sql_str=sql_str[:-1]+");\n"
            f.write(sql_str)
    f.close()