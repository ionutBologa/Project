from connections import cursor,connect
from flask import Flask, request, jsonify, render_template

app=Flask(__name__)
class User():
    def __init__(self,Nume,Prenume,Companie,IdManager):
        self.Nume=Nume
        self.Prenume=Prenume
        self.Companie=Companie
        self.IdManager=IdManager

    def insert_user(self):
        cursor.execute(f"INSERT INTO USERS VALUES (null,'{self.Nume}','{self.Prenume}','{self.Companie}','{self.IdManager}');")
        connect.commit()


@app.route('/register_user', methods=['POST'])
def insert_users():
    try:
        data = request.get_json()
        nume = data['Nume']
        prenume = data['Prenume']
        companie = data['Companie']
        id_manager = data['IdManager']

        query = "INSERT INTO persoane (Nume, Prenume, Companie, IdManager) VALUES (?, ?, ?, ?);"
        values = (nume, prenume, companie, id_manager)

        cursor.execute(query, values)
        connect.commit()

        return "Persoana inserata cu succes! ID: " + str(cursor.lastrowid), 201

    except KeyError as e:
        return "Date incomplete sau incorecte", 400
    except Exception as e:
        print("Eroare la inserarea persoanei:", e)
        return "Eroare la inserarea persoanei", 500

@app.route('/register', methods=['GET'])
def serve_register_page():
    return render_template('html/register.html')

if __name__ == '__main__':
    app.run(debug=True)


