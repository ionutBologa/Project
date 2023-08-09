import threading
from connections import cursor,connect
from flask import Flask, request, render_template

'''This file contain the endpoint and the html interface for adding users from browser '''


app=Flask(__name__,static_folder='/Users/bologaionut/PycharmProjects/Final_Project/static')

@app.route('/register', methods=['POST'])
def insert_users():
    try:
        nume = request.form['nume']
        prenume = request.form['prenume']
        companie = request.form['companie']
        id_manager = request.form['idManager']

        cursor.execute(f"INSERT INTO USERS VALUES (null,'{nume}','{prenume}','{companie}','{id_manager}');")
        connect.commit()

        return "Persoana inserata cu succes!", 201

    except KeyError as e:
        return f"Date incomplete sau incorecte{e}", 400
    except Exception as e:
        print("Eroare la inserarea persoanei:", e)
        return "Eroare la inserarea persoanei", 500


@app.route('/', methods=['GET'])
def serve_register_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

t2=threading.Thread(app.run())
