from flask import Flask, request, jsonify
from connections import connect,cursor
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST'])
def gate_entry():
    try:
        data = request.json['data']
        sens = request.json['sens']
        idPersoana = request.json['idPersoana']
        idPoarta = request.json['idPoarta']

        data = datetime.strptime(data, '%Y-%m-%dT%H:%M:%S.%fZ')

        cursor.execute(f"INSERT INTO gate_entry values('{data}','{sens}', '{idPersoana}','{idPoarta}')")
        connect.commit()

        return jsonify(message="Entry saved successfully")

    except Exception as e:
        return jsonify(error=str(e))

if __name__ == '__main__':
    app.run(port=8000, debug=True)
