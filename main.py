from flask import *
from flask_socketio import *
import hashlib

app = Flask(__name__)
hash_obj = hashlib.sha512(b'0x9f17cd320d8d4abd9dc18535391dd0b09784dcd9590d9fc11764331eae69f0b1389d3582ab69ef71fa6605dc470b5f3737f581c2807f9f')  #hexa from 60 digit integer
hash_dig = hash_obj.hexdigest() #make hash object become hexa
app.config['SECRET_KEY'] = hash_dig #adding secret key to apps
socketio = SocketIO(app)

# @app.route('/')
# def login():
#     return render_template('login_frm.html')

@app.route('/')
def soon():
    return render_template('soon.html')

@app.route('/main')
def session():
    return render_template('index.html')

def mesgReceived(methods=['GET', 'POST']):
    return 200, 'msg already received'

@socketio.on('evt')
def event_handler(json, methods=['GET', 'POST']):
    socketio.emit('response_return', json, callback=msgReceived)
if __name__ == '__main__':
    socketio.run(app, debug=True, port=80)