from flask import request
import time
from connections import connect,app,send_email
from datetime import datetime


def worked_hours():
    mycursor = connect.cursor()
    mycursor.execute("SELECT * FROM check_times")
    mydata = mycursor.fetchall()

    today=datetime.today().date()
    check_in = []
    check_out= []
    entry_worked_hours = {}
    worked=""

    for entry in mydata:
        entry_id = entry[0]
        entry_date_time = entry[1]
        entry_way = entry[2].strip(";")

        date_time_obj = datetime.strptime(str(entry_date_time), "%Y-%m-%d %H:%M:%S")
        entries = {
            "id": entry_id,
            "date_time": date_time_obj,
            "way": entry_way
        }

        if entries["way"] == "in":
            check_in.append(entries)
        if entries["way"] == "out":
            check_out.append(entries)

    # Process the data to calculate the worked hours for each entry_id

    for entry in check_in:
        entry_id = entry["id"]
        date_time_obj = entry["date_time"]

        if entry_id not in entry_worked_hours:
            entry_worked_hours[entry_id] = {"in_time": date_time_obj, "out_time": None}
        else:
            entry_worked_hours[entry_id]["in_time"] = date_time_obj

    for entry in check_out:
        entry_id = entry["id"]
        date_time_obj = entry["date_time"]

        if entry_id not in entry_worked_hours:
            entry_worked_hours[entry_id] = {"in_time": None, "out_time": date_time_obj}
        else:
            entry_worked_hours[entry_id]["out_time"] = date_time_obj

    # Calculate  the worked hours for each entry_id
    for entry_id, timestamps in entry_worked_hours.items():
        time_in = timestamps["in_time"]
        time_out = timestamps["out_time"]

        if time_in and time_out:
            worked_hours = (time_out - time_in).total_seconds() / 3600
            if worked_hours < 28799/3600:
                worked+=f"ID: {entry_id} on date :{today} worked {worked_hours} hours\n"
                mycursor.execute(f"Insert into lessThen8Hours value('{entry_id}','{today}','{worked_hours}')")
                connect.commit()
    email="bologaionutviorel@gmail.com"
    email1="bologa.raluca@gmail.com"
    content=" Employees that worked  less then 8 hours today"
    subject = ""+worked


    send_email((email,email1),content,subject)



worked_hours()
