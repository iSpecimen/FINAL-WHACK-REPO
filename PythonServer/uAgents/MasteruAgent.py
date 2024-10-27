from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Received data: {data}")
    response = {'status': 'success', 'message': 'Data received'}
    return jsonify(response)

@app.route('/data', methods=['GET'])
def send_data():
    response_data = {'message': 'Hello from Python server!'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)