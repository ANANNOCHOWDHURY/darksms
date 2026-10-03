<div align="center">
  <a href="https://www.anannochowdhury.com/">
    <img src="https://capsule-render.vercel.app/api?type=rect&height=150&color=0:0b1020,60:1a1240,100:5a46e0&text=DARKSMS&fontColor=ffc857&fontSize=44&fontAlignY=45&desc=Powered%20by%20ANANNO%20CHOWDHURY&descColor=e8ebf7&descSize=16&descAlignY=72" alt="DarkSMS" width="100%"/>
  </a>

<br/>

<a href="https://github.com/ANANNOCHOWDHURY">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1100&color=5A46E0&center=true&vCenter=true&width=640&lines=%24+whoami;Real-time+chatroom+app;Flask+%2B+Socket.IO+%7C+Auto-deleting+messages">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1100&color=FFC857&center=true&vCenter=true&width=640&lines=%24+whoami;Real-time+chatroom+app;Flask+%2B+Socket.IO+%7C+Auto-deleting+messages" alt="$ whoami" />
  </picture>
</a>

<br/>

<img src="https://img.shields.io/badge/python-3.8+-0b1020?style=for-the-badge&labelColor=0b1020&color=5a46e0" alt="python 3.8+"/>
<img src="https://img.shields.io/badge/flask-socketio-0b1020?style=for-the-badge&labelColor=0b1020&color=5a46e0" alt="flask socketio"/>
<img src="https://img.shields.io/badge/status-ready-0b1020?style=for-the-badge&labelColor=0b1020&color=5a46e0" alt="status: ready"/>

</div>

<br/>

## `> about`

**DarkSMS** is a real-time chatroom web app built with Flask and Flask-SocketIO. People join a named room and chat instantly — messages are pushed to everyone in the room over WebSockets. Every message is auto-deleted 24 hours after it's sent, so nothing sticks around.

## `> features`

- 💬 Real-time messaging with Socket.IO (no page refresh)
- 🚪 Room-based chat — join any room by name
- 🔔 System join notifications (`"X joined"`)
- 🕒 Messages auto-expire and delete after 24 hours
- 🧹 Background cleanup thread runs every 60 seconds
- 🪶 Lightweight — messages are stored in a plain `messages.txt` file, no database needed

## `> tech stack`

- **Python 3.8+**
- **Flask** — web server
- **Flask-SocketIO** — real-time WebSocket communication
- **Threading** — background auto-delete worker

## `> project structure`

```bash
.
├── app.py              # Flask + Socket.IO server, message handling, auto-delete worker
├── templates/          # HTML templates (chat UI)
├── static/             # CSS / JS / assets for the chat UI
├── messages.txt         # Message log (auto-created, auto-cleaned)
└── README.md
```

## `> installation`

Clone the repository:

```bash
git clone https://github.com/ANANNOCHOWDHURY/darksms.git
```

Enter the directory:

```bash
cd darksms
```

Install dependencies:

```bash
pip install flask flask-socketio
```

Run the server:

```bash
python app.py
```

The app will start on:

```
http://0.0.0.0:5000
```

## `> how it works`

1. A client connects and emits a `join` event with a `room` and `nickname`.
2. The server adds them to that Socket.IO room and broadcasts a system join message.
3. Sending a message emits `send_message` with `nickname`, `room`, and `text`.
4. The server timestamps the message, appends it to `messages.txt` with a 24-hour expiry, and broadcasts it live to everyone in the room.
5. A background thread checks `messages.txt` every 60 seconds and removes any message past its expiry time.

## `> license`

All Rights Reserved — © 2026 Ananno Chowdhury. See [`LICENSE`](./LICENSE) for the full terms. No part of this source code, design, or content may be copied, reused, or redistributed without written permission.

## `> contact`

<div align="center">

<a href="mailto:mdnowmihayatchowdhuryananno@gmail.com"><img src="https://img.shields.io/badge/Email-8b7bff?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
<a href="https://www.linkedin.com/in/ananno-chowdhury-6482a3378"><img src="https://img.shields.io/badge/LinkedIn-0b1020?style=for-the-badge&logo=linkedin&logoColor=ffc857" alt="LinkedIn"/></a>
<a href="https://github.com/PK-BIGBOY"><img src="https://img.shields.io/badge/GitHub-0b1020?style=for-the-badge&logo=github&logoColor=ffc857" alt="GitHub"/></a>
<a href="https://www.anannochowdhury.com/"><img src="https://img.shields.io/badge/Portfolio-0b1020?style=for-the-badge&logo=googlechrome&logoColor=ffc857" alt="Portfolio"/></a>

<br/><br/>

```bash
ananno@bigboy:~$ echo "Stay curious. Hack ethically."
Stay curious. Hack ethically.
```

<a href="https://www.anannochowdhury.com/">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=80&color=0:5a46e0,40:1a1240,100:0b1020&text=Created%20by%20ANANNO%20CHOWDHURY&fontColor=ffc857&fontSize=18&fontAlignY=50" width="100%" alt="Created by ANANNO CHOWDHURY"/>
</a>

</div>
