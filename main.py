#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : main.py
@Time : 2024/08/28 15:57:36
@Auth : Ming(<3057761608@qq.com>)
@Vers : 1.0
@Desc : Baicizhan 单词导出脚本
@Usag : python main.py
'''

# here put the import lib
import sqlite3
import xlwt
import re
import pandas as pd

def list_tables(db_path):
    """列出数据库中所有以 'ts_learn_offline_dotopic_sync_ids_' 开头的表"""
    try:
        with sqlite3.connect(db_path) as conn:
            print("可导出的单词本id \t 单词数")
            cur = conn.cursor()
            cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cur.fetchall()
            for table in tables:
                if re.match(r'^ts_learn_offline_dotopic_sync_ids_\d+$', table[0]):
                    cur.execute(f"SELECT COUNT(*) FROM {table[0]};")
                    count = cur.fetchone()[0]
                    table_id = table[0].split('_')[-1]
                    print(f"{table_id} \t {count}")
    except Exception as e:
        print(f"无法打开文件或读取数据：{e}")

def get_word_ids(db_path, table_name, random_order=False):
    """从指定的数据库和表中获取单词ID"""
    query = f"SELECT topic_id FROM {table_name}"
    if random_order:
        query += " ORDER BY random()"
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(query)
        return cur.fetchall()

def find_words(db_path, word_ids):
    """在指定的数据库中查找单词"""
    words = []
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        for word_id in word_ids:
            cur.execute("SELECT word, accent, mean_cn FROM dict_bcz WHERE topic_id = ?", (word_id[0],))
            word = cur.fetchone()
            if word:
                words.append(word)
    return words

def export_words(words, filename, format, template='default', blank_cols=3):
    """将单词导出到指定格式的文件"""
    if template == 'default':
        columns = ['单词', '音标', '中文释义']
    elif template == 'writing':
        columns = ['中文释义', '音标'] + [f'空白列{i+1}' for i in range(blank_cols)] + ['单词']
    else:
        print("未知的模板，仍将使用默认模板。")
        columns = ['单词', '音标', '中文释义']

    if format == 'excel':
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('百词斩已背单词')
        for col, label in enumerate(columns):
            worksheet.write(0, col, label=label)
        for row, word in enumerate(words):
            for col, label in enumerate(columns):
                if label in ['单词', '音标', '中文释义']:
                    worksheet.write(row+1, col, label=word[columns.index(label)])
        workbook.save(filename)
        print(f"共{len(words)}个单词，Excel已导出到：{filename}")
    elif format == 'html':
        word_df = pd.DataFrame(words, columns=['单词', '音标', '中文释义'])
        for i in range(blank_cols):
            word_df.insert(i+2, f'空白列{i+1}', '')
        word_df = word_df[columns]
        html = word_df.to_html(justify='center', col_space=50)
        html = html.replace('class', 'cellspacing=\"0\" class')
        with open(filename, 'w') as f:
            f.write(html)
        print(f"共{len(words)}个单词，HTML已导出到：{filename}")


def main():
    """主函数"""
    baicizhantopicproblem = input("请输入baicizhantopicproblem.db的路径（默认：./baicizhantopicproblem.db）：") or './baicizhantopicproblem.db'
    lookup = input("请输入lookup.db的路径（默认：./lookup.db）：") or './lookup.db'

    while True:
        print('--------------------------------')
        list_tables(baicizhantopicproblem)
        table_name = input("请直接输入要导出的单词本id，或输入 'q' 或 'quit' 退出程序（默认：964）：") or '964'
        if table_name.lower() in ['q', 'quit']:
            break
        table_name = f"ts_learn_offline_dotopic_sync_ids_{table_name}"
        format = input("请输入导出文件的格式（默认：html）：") or 'html'
        template = input("请输入使用的模板（默认：default，可选：writing）：") or 'default'
        blank_cols = 3
        if template == 'writing':
            blank_cols = int(input("请输入空白列的数量（默认：3）：") or '3')
        output_filename = input(f"请输入输出文件的名称（默认：output）：") or 'output'
        output_filename = f"{output_filename}.{format}"
        random_order = input("是否随机排序[y/n]（默认：n）：") or 'n'
        if random_order.lower() in ['y', 'yes']:
            random_order = True
        else:
            random_order = False
        word_ids = get_word_ids(baicizhantopicproblem, table_name,random_order)
        words = find_words(lookup, word_ids)
        export_words(words, output_filename, format, template, blank_cols)
        print('--------------------------------')

    print("程序已退出。")


if __name__ == "__main__":
    main()