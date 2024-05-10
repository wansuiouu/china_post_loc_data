with open('dml/post_sql_to_dbv2.sql','r',encoding='utf-8') as f:
    sql_lines = f.readlines()
    len_sql = len(sql_lines)
    mid_len=len(sql_lines)//2
    with open('dml/post_sql_to_dbv2_1.sql','w',encoding='utf-8') as f1:
        for each in range(0,mid_len):
            f1.write(sql_lines[each])
        f1.close()
    with open('dml/post_sql_to_dbv2_2.sql','w',encoding='utf-8') as f2:
        for each in range(mid_len,len(sql_lines)):
            f2.write(sql_lines[each])
        f2.close()
    f.close()

with open('dml/post_sql_to_dbv2_1.sql','r',encoding='utf-8') as f:
    sql_lines = f.readlines()
    len_sql = len(sql_lines)
    mid_len=len(sql_lines)//2
    with open('dml/post_sql_to_dbv2_1_1.sql','w',encoding='utf-8') as f1:
        for each in range(0,mid_len):
            f1.write(sql_lines[each])
        f1.close()
    with open('dml/post_sql_to_dbv2_1_2.sql','w',encoding='utf-8') as f2:
        for each in range(mid_len,len(sql_lines)):
            f2.write(sql_lines[each])
        f2.close()
    f.close()

with open('dml/post_sql_to_dbv2_2.sql','r',encoding='utf-8') as f:
    sql_lines = f.readlines()
    len_sql = len(sql_lines)
    mid_len=len(sql_lines)//2
    with open('dml/post_sql_to_dbv2_2_1.sql','w',encoding='utf-8') as f1:
        for each in range(0,mid_len):
            f1.write(sql_lines[each])
        f1.close()
    with open('dml/post_sql_to_dbv2_2_2.sql','w',encoding='utf-8') as f2:
        for each in range(mid_len,len(sql_lines)):
            f2.write(sql_lines[each])
        f2.close()
    f.close()