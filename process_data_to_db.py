import sys
import io
import pandas as pd
from bs4 import BeautifulSoup
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
def pre_read_html(name):
    html_text=""
    with open(name, 'r',encoding='utf-8') as f:
        for line in f:
            html_text+=line
        f.close()
    return html_text

# build sql
def build_insert_sql(table_name,dataframe):
    one_sql=''
    sql_i = "INSERT INTO `" + table_name + "` (sheng, shi, xian, name, post_code, address, finance, phone, `time`) VALUES "
    for i in range(len(dataframe)):
        if i==0: 
            continue
        sql_v=''
        sql_v += "("
        for j in range(len(dataframe.columns)):
            sql_v+="'" + str(dataframe.iloc[i,j])+ "',"
        one_sql+=(sql_i+sql_v[:-1]+");\n")
    return one_sql

def parse_html_to_df(html_text):
    soup = BeautifulSoup(html_text,'lxml')
    content = soup.select('.wangd2')[0]
    tbl = pd.read_html(content.prettify())
    table_data = tbl[0]
    return table_data

range_list = [str(i)+"0" for i in range(1,5514)]
sql_list=[]
for i in range_list:
    html_name = 'postoffice/post_pos_'+i+'.html'
    html_text = pre_read_html(html_name)
    table_data = parse_html_to_df(html_text)
    insert_sql=build_insert_sql("china_post_office",table_data)
    sql_list.append(insert_sql)

with open('post_sql.sql','w',encoding='utf-8') as f:
    for insert_sql in sql_list:
        f.write(insert_sql+'\n')
    f.close()
