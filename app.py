from flask import Flask  # type: ignore
from flask_socketio import SocketIO  # type: ignore

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def hello_world():
    return 'Hello, World!'

@socketio.on('send_command')
def handle_command(command):
    print(f"Command received: {command}")
    socketio.emit('execute_command', command, to=None)  

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)



























