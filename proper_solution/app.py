from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def predict():
    prediction = random.randint(1, 100)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
