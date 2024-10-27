from flask import Flask, request, jsonify
from call import CallForHelp #uses the CallForHelp function in call.py
from MasterAgent import Startup #so i can call the startup in masteragent when i recieve the 
import json

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_Data():
    data = request.json # Recieving the JSON data from C# Unity App
    print(f"Received data: {data}")

    if data['type'] == 'Journey_Started':
        MasterAgent.Startup()
        # Start MasterAgent when journey starts
    elif data['type'] == 'Crash_Detected':
        call.CallForHelp() #Run Call.py's CallForHelp Method 
    
    #Need to Convert the data to a string to write to a txt file here, the CrashData will only have name and acceleration.
    json_data_string = json.dumps(data, indent=4)
    with open('received_data.txt', 'w') as file:
        file.write(json_data_string)  # Write the string to the file

    call.CallForHelp() #Refer to call.py to CallForHelp.

    response = {'status': 'success', 'message': 'Data received'}
    return jsonify(response)

@app.route('/data/weather', methods=['GET'])
def sendWeatherData():
    response_data = {
        'type': 'weather',
        'message': '(PUT UAGENT OUTPUT HERE TO SEND TO THE APP)',
        'info': 'IDK IF YOU NEED THIS BUT YOU CAN GET RID OF THIS IF YOU ONLY NEED TO SEND ONE PIECE OF DATA.'
    }
    return jsonify(response_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)