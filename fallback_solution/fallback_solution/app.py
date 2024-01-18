from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def predict():
    # Fallback solution always predicts 42
    return jsonify({'prediction': 42})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
