import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="p0r0dica", database="project")
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



insert=User()
