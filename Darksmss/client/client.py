import socketio
import threading
import os


sio = socketio.Client()


print("""

██████╗  █████╗ ██████╗ ██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
██║  ██║███████║██████╔╝█████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗
██████╔╝██║  ██║██║  ██║██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

""")

nickname = input("Nickname : ")

room = input("Room : ")


# =========================
# CONNECT
# =========================

@sio.event

def connect():

    print("\n[ Connected ]\n")

    sio.emit('join', {

        'nickname': nickname,

        'room': room
    })


# =========================
# RECEIVE MESSAGE
# =========================

@sio.on('message')

def on_message(data):

    print(
        f"\n[{data['nickname']}] "
        f"{data['text']}"
    )


# =========================
# SEND LOOP
# =========================

def send_loop():

    while True:

        text = input()

        sio.emit('send_message', {

            'nickname': nickname,

            'room': room,

            'text': text
        })


# =========================
# CONNECT SERVER
# =========================

sio.connect(
    "http://YOUR_SERVER_IP:5000"
)

thread = threading.Thread(
    target=send_loop
)

thread.start()

sio.wait()