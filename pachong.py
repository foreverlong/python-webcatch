from multiprocessing.connection import wait
import requests
import csv
from csv import writer
from bs4 import BeautifulSoup

import os
import sys
from pprint import pprint
from notion_client import Client


req = requests.get(url="https://testnumber.bjchp.gov.cn/")
req.encoding = "utf-8"
html=req.text
soup = BeautifulSoup(req.text,features="html.parser")

company_item = soup.find("div",class_="tab-content")
dd = company_item.text.strip()

update_time_weizhi = dd.find('最近更新：')
update_time_pos = update_time_weizhi + 5
#print(dd[update_time_pos:(update_time_pos+16)])
real_ut = dd[update_time_pos:(update_time_pos+16)]
real_date = real_ut[:10]
real_time = real_ut[11:]
print(real_date)
print(real_time)

#龙泽园街道160龙泽园街道智慧社(time_pose)4分钟10人1个龙泽园街道智慧社西一门南侧09:00-11:5013:00-18:50
#weizhi=dd.find('龙泽园街道智慧社') #找到位置
weizhi=dd.find('北七家镇八仙庄（潮鹏）') 
#print(weizhi)
time_pos = weizhi + 11
if dd[time_pos:(time_pos+1)]=='无':
    time = 0
    people = 0
else:
    time_end = dd.find('分钟',time_pos) #找到分钟的位置
    time = int(dd[time_pos:time_end])
    people_pos = dd.find('人',time_end)
    people = int(dd[(time_end+2):people_pos])
#str = dd[time_pos:(time_pos+10)]
print(time)
print(people)
#print(type(dd))
#在td里面

with open('龙泽园街道智慧社.csv', 'a', newline='') as f_object:  
    # Pass the CSV  file object to the writer() function
    writer_object = writer(f_object)
    # Result - a writer object
    # Pass the data in the list as an argument into the writerow() function
    writer_object.writerow([real_date, real_time, time, people])  
    # Close the file object
    f_object.close()


# Initialize the client
notion = Client(auth='secret_XsLZcIj2ZJqXyK0b35zhWyMzZn7OUgZOzWiULUBgSlu')

# Create a new page
new_page = {
    "日期": {"title": [{"text": {"content": str(real_date)}}]},
    "时间": {
        "type": "rich_text",
        "rich_text": [
            {
                "type": "text",
                "text": {"content": str(real_time)},
            },
        ],
    },
    "等候时间": {
        "type": "rich_text",
        "rich_text": [
            {
                "type": "text",
                "text": {"content": str(time)},
            },
        ],
    },
    "等候人数": {
        "type": "rich_text",
        "rich_text": [
            {
                "type": "text",
                "text": {"content": str(people)},
            },
        ],
    }
}
notion.pages.create(parent={"database_id": 'dc4633a949f546d1ab1e24d305343cbf'}, properties=new_page)


#with open("file.csv", "w", encoding="gbk", newline="") as f:
#    # 2. 基于文件对象构建 csv写入对象
#    csv_writer = csv.writer(f)
#    # 3. 构建列表头
#    csv_writer.writerow(["时间", "时长"])
#    # 4. 写入csv文件内容
#    csv_writer.writerow([real_ut, time])
#    #csv_writer.writerow(["jack", "18"])
#    #csv_writer.writerow(["alex", "20"])
#    print("写入数据成功")
#    # 5. 关闭文件
#    f.close()