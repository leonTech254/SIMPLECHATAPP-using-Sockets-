from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(data):
    emit("received", data, broadcast=True)


@socketio.on('my event')
def hello(data):
    print(data)


@socketio.on('from_flask')
def leon(data):
    print("hellow rolf")
    emit("name", {"name": "martin"}, broadcast=True)


@socketio.on("typing")
def typing(data):
    emit("typer", data, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")
