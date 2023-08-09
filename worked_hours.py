import threading
import time

from connections import connect,app,send_email,cursor
from datetime import datetime


def worked_hours():

    '''This function calculate the worked of hours of every employee,based on the check-in and check-out on different gates
     and send an email whit the id's of thouse that not worked 8 hours a day and save in database the id,the date of unfulfilled
      worked time and the time they worked'''

    mycursor = connect.cursor()
    mycursor.execute("SELECT * FROM check_times")
    mydata = mycursor.fetchall()

    check_in = {}
    check_out = {}
    entry_worked_hours = {}

    for entry in mydata:
        entry_id = entry[0]
        entry_date_time = entry[1]
        entry_way = entry[2].strip(";")

        date_time_obj = datetime.strptime(str(entry_date_time), "%Y-%m-%d %H:%M:%S")

        if entry_way == "in":
            if entry_id not in check_in:
                check_in[entry_id] = []
            check_in[entry_id].append(date_time_obj)
        elif entry_way == "out":
            if entry_id not in check_out:
                check_out[entry_id] = []
            check_out[entry_id].append(date_time_obj)

    for entry_id, in_times in check_in.items():
        if entry_id not in check_out:
            continue

        out_times = check_out[entry_id]

        total_worked_hours = 0.0

        for in_time in in_times:
            for out_time in out_times:
                if out_time > in_time:
                    worked_hours = (out_time - in_time).total_seconds() / 3600
                    if worked_hours < 28799 / 3600:
                        total_worked_hours += worked_hours

        entry_worked_hours[entry_id] = total_worked_hours

    return entry_worked_hours
worked_hours_data = worked_hours()
uncompleteHours= ""

for entry_id, total_worked_hours in worked_hours_data.items():
    if total_worked_hours < 28799 / 3600:

        uncompleteHours+=(f"ID: {entry_id} on date: {datetime.today().date()} worked {total_worked_hours} hours\n")

        cursor.execute(f"Insert into under8hours value('{entry_id}','{datetime.today().date()}','{total_worked_hours}')")
        connect.commit()

if uncompleteHours!= "":
    time.sleep(2)
    email="bologaionutviorel@gmail.com"
    # email1="bologa.raluca@gmail.com"
    content=" Employees that worked  less then 8 hours today"
    subject =uncompleteHours

    send_email((email),content,subject)
    print("email sent")

worked_hours()



