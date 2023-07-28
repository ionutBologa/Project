from datetime import datetime
from connections import connect




from datetime import datetime

from datetime import datetime

def worked_hours():
    mycursor = connect.cursor()
    mycursor.execute("SELECT * FROM check_times")
    mydata = mycursor.fetchall()

    id_entries = []
    entry_worked_hours = {}


    for entry in mydata:
        entry_id = entry[0]
        entry_date_time = entry[1]
        entry_way = entry[2]

        date_time_obj = datetime.strptime(str(entry_date_time), "%Y-%m-%d %H:%M:%S")


        entries = {
            "id": entry_id,
            "date_time": date_time_obj,
            "way": entry_way
        }
        id_entries.append(entries)

    # Process the data to calculate and print the worked hours for each entry_id

    for entry in id_entries:
        entry_id = entry["id"]
        date_time_obj = entry["date_time"]
        entry_way = entry["way"]


        if entry_id not in entry_worked_hours:
            entry_worked_hours[entry_id] = {"in_time": date_time_obj, "out_time": date_time_obj}

            if entry_way == 'in':
                entry_worked_hours[entry_id]["in_time"] = date_time_obj
            elif entry_way == 'out':
                 entry_worked_hours[entry_id]["out_time"] = date_time_obj

    print(entry_worked_hours)
    # Calculate and print the worked hours for each entry_id
    for entry_id, timestamps in entry_worked_hours.items():
        time_in = timestamps["in_time"]
        time_out = timestamps["out_time"]

        if time_in and time_out:
            worked_hours = time_out - time_in
            print(f"ID: {entry_id}, Worked Hours: {worked_hours.total_seconds() / 3600:2} hours")
        else:
            print(f"ID {entry_id} has missing 'in' or 'out' event.")


worked_hours()

