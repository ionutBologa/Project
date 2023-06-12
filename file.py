import os
import csv
intrari='/Users/bologaionut/PycharmProjects/Final_Project/intrari/'
backup_intrari='/Users/bologaionut/PycharmProjects/Final_Project/backup_intrari'

csv = []
txt = []
def readFolder():
    for element in os.listdir(intrari):
        type=element.split(".")[1]
        if type=="csv":
            csv.append(element)
        if type=="txt":
            txt.append(element)
    print(csv)
    print(txt)


readFolder()

def read_files():
    for i in txt:
        with open(intrari+i,'r')as f:
            continut=f.read()
            print(continut)
read_files()
