from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/finance', methods=['POST'])
def receive_finance():
    data = request.json
    # TODO: Process and store the data
    return jsonify({'status': 'success', 'data': data}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
