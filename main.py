#main.py
from flask import Flask, jsonify, request
from db import get_songs, add_songs

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def songs():
    if request.method == 'POST':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400  

        add_songs(request.get_json())
        return 'Register Sukses' 

if __name__ == '__main__':
    app.run()