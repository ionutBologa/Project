import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="p0r0dica", database="project",auth_plugin='mysql_native_password')
cursor=conn.cursor()
class User():
    def __init__(self,Nume,Prenume,Companie,IdManager):
        self.Nume=Nume
        self.Prenume=Prenume
        self.Companie=Companie
        self.IdManager=IdManager

    def insert_user(self):
        cursor.execute(f"INSERT INTO USERS VALUES (null,'{self.Nume}','{self.Prenume}','{self.Companie}','{self.IdManager}');")
        conn.commit()



ionut=User('ionut','bologa','Y',2)
ionut.insert_user()
