import datetime,time,os,csv,shutil
import threading
from connections import cursor,connect
from worked_hours import worked_hours

intrari='/Users/bologaionut/PycharmProjects/Final_Project/intrari/'
backup_intrari='/Users/bologaionut/PycharmProjects/Final_Project/backup_intrari/'

csv_files = []
txt_files = []

def readFolder():
    '''This function read's the folder for files and sort them by type'''

    for element in os.listdir(intrari):
        type=element.split(".")[1]
        if type=="csv":
            csv_files.append(element)
        if type=="txt":
            txt_files.append(element)

    return csv_files,txt_files

def read_files_txt():

    '''This function read's txt files , write the file content in the database
    and move the file after it was processed in a backup folder and add's the date when the file was processed to
    the file's output name'''

    txt_input=intrari+str(txt_files[0])
    date=datetime.date.today()
    output=str(date)+"-"+ str(txt_files[0])
    try:
        with open(txt_input,'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(',')
                date = line[1].split('T',1)
                time = date[1].split('.')
                date_time = date[0] + ' ' + time[0]
                cursor.execute(f"Insert into check_times values ('{line[0]}','{date_time}','{line[2]}')")
                connect.commit()
    except:
        pass
    shutil.move(txt_input, backup_intrari + output)
    print("file moved txt")
    txt_files.clear()

def read_files_csv():

    '''This function read's csv files , write the file content in the database
    and move the file after it was processed in a backup folder and add's the date when the file was processed to
    the file's output name'''

    fisier=[]
    csv_input = intrari + str(csv_files[0])
    date = datetime.date.today()
    output = str(date) + "-" + str(csv_files[0])
    try:
        with open(csv_input,'r') as c:
            content=csv.reader(c)
            next(content,None)
            for rows in content:
                fisier.append(rows)
            for element in fisier:
                result = element[1].split(',')
                date = result[0].split('T', 1)
                time = date[1].split('.')
                date_time = date[0] + ' ' + time[0]
                cursor.execute(f"Insert into check_times values ('{element[0]}','{date_time}','{element[2]}')")
                connect.commit()
    except:
        pass

    shutil.move(csv_input, backup_intrari + output)
    csv_files.clear()
    print("file moved csv")
def check_new_files():

    '''This function check's the folder for new files at given time of the day'''

    while True:
        csv_files, txt_files = readFolder()
        try:
            if datetime.datetime.now().hour == 19:
                if csv_files or txt_files:
                    if csv_files:
                        read_files_csv()
                    if txt_files:
                        read_files_txt()
                else:
                    print("no new files")
                worked_hours()
                time.sleep(3)
            else:
                print("Cheack the app starting time")
            break
        except:
            pass


check_new_files()
t1=threading.Thread(check_new_files())




