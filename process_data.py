import sys
import io
import pandas as pd
from bs4 import BeautifulSoup
import xlsxwriter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 
def pre_read_html(name):
    html_text=""
    with open(name, 'r',encoding='utf-8') as f:
        for line in f:
            html_text+=line
        f.close()
    return html_text
def parse_html_to_df(html_text):
    soup = BeautifulSoup(html_text,'lxml')
    content = soup.select('.wangd2')[0]
    tbl = pd.read_html(content.prettify())
    table_data = tbl[0]
    return table_data
def write_to_excel(dataframe,worksheet,start_row):
    for i in range(len(dataframe)):
        for j in range(len(dataframe.iloc[i])):
            worksheet.write(start_row+i, j, dataframe.iloc[i][j])

range_list = [str(i)+"0" for i in range(1,5514)]
start_row=1
worksheet_name='p'
workbook = xlsxwriter.Workbook('post_data.xlsx', {'nan_inf_to_errors': True}) 
worksheet = workbook.add_worksheet(worksheet_name) 
num_sheet=0
for i in range_list:
    html_name = 'postoffice/post_pos_'+i+'.html'
    html_text = pre_read_html(html_name)
    dataframe = parse_html_to_df(html_text)
    if start_row>=65536:
        start_row=1
        num_sheet+=1
        worksheet_name+=str(num_sheet)
        worksheet = workbook.add_worksheet(worksheet_name)
    write_to_excel(dataframe,worksheet,start_row)
    start_row=start_row+11
print("start_row: ",start_row)
workbook.close()
