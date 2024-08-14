from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

task_executed = False

@app.route('/chat', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data['message']
    print("Received message:", message)
    if message == "hii":
        response = "hello sir"
    elif message == "how are you":
        response = "Thank you for asking. I am fine sir."
    else:
        response = {"received": True}
    return jsonify(response)

@app.route('/running_status', methods=['POST'])
def receive_status():
    global task_executed
    message = request.form.get('message')
    if message == "run" and not task_executed:
        print("run command received")
        task_executed = True

        # Run main.py using subprocess
        subprocess.Popen(["python", "main.py"])

        return "Command executed successfully!"
    else:
        return "Invalid command"

if __name__ == '__main__':
    print("Running Flask")
    app.run(debug=True)
