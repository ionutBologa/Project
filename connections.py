import mysql.connector

connect=mysql.connector.connect(
        host="localhost",
        user="root",
        password="p0r0dica",
        database="project",
        auth_plugin='mysql_native_password'
    )
cursor=connect.cursor()