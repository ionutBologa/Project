import datetime
import os
import csv
import shutil
from connections import cursor,connect


intrari='/Users/bologaionut/PycharmProjects/Final_Project/intrari/'
backup_intrari='/Users/bologaionut/PycharmProjects/Final_Project/backup_intrari/'

csv = []
txt = []
def readFolder():
    for element in os.listdir(intrari):
        type=element.split(".")[1]
        if type=="csv":
            csv.append(element)
        if type=="txt":
            txt.append(element)
    return csv,txt


readFolder()

def read_files():
    input=intrari+str(txt[0])
    date=datetime.date.today()
    output=str(date)+"-"+ str(txt[0])
    with open(input,'r') as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            line=line.split(',')
            date=line[1].split('T')
            time=line[1].split('T',8)
            time=time[1].split('.')
            date_time=date[0]+' '+time[0]
            print(line[0]+' '+date_time+' '+line[2])
            cursor.execute(f"Insert into check_times values ('{line[0]}','{date_time}','{line[2]}')")
            connect.commit()



    # shutil.move(input,backup_intrari+output)

read_files()


