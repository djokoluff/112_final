# from flask import Flask, render_template, request

# app = Flask(__name__, static_folder='static')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     audio_file = request.files['audio']

#     return '音檔已接收'

# if __name__ == '__main__':
#     app.run(debug=True)

#-------------------------------------------------
from flask import Flask, render_template, request, jsonify , url_for
import random

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    print('url: ', url_for('static', filename='music/babyshark.mp3'))
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['audio']
    return jsonify({'message': 'Audio file received and processed'})

@app.route('/get_baby_state', methods=['GET']) # fake api for testing idf
def get_baby_state():
    return {'state': random.choice([True, False])}

if __name__ == '__main__':
    app.run(debug=True)



