from flask import Flask
from flask_socketio import (
    SocketIO,
    emit,
    join_room
)

from datetime import (
    datetime,
    timedelta
)

import threading
import time
import os


app = Flask(__name__)

app.config['SECRET_KEY'] = 'darksms'

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)


# =========================
# JOIN ROOM
# =========================

@socketio.on('join')

def on_join(data):

    room = data['room']

    join_room(room)

    emit('message', {

        'nickname': 'SYSTEM',

        'text': f"{data['nickname']} joined"

    }, room=room)


# =========================
# SEND MESSAGE
# =========================

@socketio.on('send_message')

def handle_message(data):

    nickname = data['nickname']

    room = data['room']

    text = data['text']

    created = datetime.utcnow()

    expires = (
        created + timedelta(hours=24)
    )

    message_data = (

        f"{nickname}|"

        f"{room}|"

        f"{text}|"

        f"{created.isoformat()}|"

        f"{expires.isoformat()}\n"
    )

    with open(
        "messages.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(message_data)

    emit('message', {

        'nickname': nickname,

        'text': text

    }, room=room)


# =========================
# AUTO DELETE
# =========================

def auto_delete_messages():

    while True:

        if not os.path.exists(
            "messages.txt"
        ):

            time.sleep(60)

            continue

        new_lines = []

        now = datetime.utcnow()

        with open(
            "messages.txt",
            "r",
            encoding="utf-8"
        ) as file:

            lines = file.readlines()

            for line in lines:

                try:

                    parts = (
                        line.strip().split("|")
                    )

                    expires_at = (
                        datetime.fromisoformat(
                            parts[4]
                        )
                    )

                    if expires_at > now:

                        new_lines.append(line)

                except:

                    pass

        with open(
            "messages.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.writelines(new_lines)

        time.sleep(60)


# =========================
# MAIN
# =========================

if __name__ == '__main__':

    thread = threading.Thread(
        target=auto_delete_messages
    )

    thread.daemon = True

    thread.start()

    socketio.run(

        app,

        host='0.0.0.0',

        port=5000
    )