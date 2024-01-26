from flask import Flask, render_template, redirect, url_for, request, session
from serial.tools import list_ports
import serial
from steam import Steam
from decouple import config

app = Flask(__name__)
app.secret_key = "your_secret_key"

# SERIAL DINGETJES
def read_serial(port):
    """Read data from the serial port and return as a string."""
    line = port.read(1000)
    return line.decode()

serial_ports = list_ports.comports()

print("[INFO] Serial ports found:")
for i, port in enumerate(serial_ports):
    print(str(i) + ". " + str(port.device))

pico_port_index = int(input("Which port is the Raspberry Pi Pico connected to? "))
pico_port = serial_ports[pico_port_index].device

serial_port = serial.Serial(port=pico_port, baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=1)
if serial_port.isOpen():
    print("[INFO] Using serial port", serial_port.name)
else:
    print("[INFO] Opening serial port", serial_port.name, "...")
    serial_port.open()

users = [
    {'username': 'MaxxieMax', 'password': 'root'},
    {'username': 'GarnetOcean', 'password': 'root2'},
    {'username': 'MisschienMarien', 'password': 'root3'},
]

def authenticate_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            data = "ingelogd\r"
            serial_port.write(data.encode())
            pico_output = read_serial(serial_port)
            # pico_output = pico_output.replace('\r\n', ' ')
            return render_template('index.html')
            return True
    return False

# #################################
# STEAM API DINGEN
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)
def NaamNaarId(username):
    test = steam.users.search_user(username)
    playerId = test['player']['steamid']
    return playerId

def online(Steamnaam):
    online_users = []
    friends_data = steam.users.get_user_friends_list(Steamnaam)
    for friend in friends_data['friends']:
        if 'personaname' in friend and friend['personastate'] == 1:
            online_users.append(friend['personaname'])
    return online_users

def offline(Steamnaam):
    offline_users = []
    friends_data = steam.users.get_user_friends_list(Steamnaam)
    for friend in friends_data['friends']:
        if 'personaname' in friend and friend['personastate'] == 0:
            offline_users.append(friend['personaname'])
    return offline_users
# EIND STEAM API DINGEN
# #################################

@app.route('/')
def index():
    data = "start_scherm\r"
    serial_port.write(data.encode())
    pico_output = read_serial(serial_port)
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            session['username'] = username  # Store the username in the session
            return redirect(url_for('dashboard', username=username))

    data = "login\r"
    serial_port.write(data.encode())
    pico_output = read_serial(serial_port)
    return render_template('login.html')

@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

# New route for the Games Library page
@app.route('/games_library')
def games_library():
    data = "games_library\r"
    serial_port.write(data.encode())
    pico_output = read_serial(serial_port)
    return render_template('games_library.html')
@app.route('/friends')
def friends():
    if 'username' in session:
        usernamevaningelogdaccount = session['username']
        if usernamevaningelogdaccount == "GarnetOcean":
            online_users = online("76561199186683253")
            offline_users = offline("76561199186683253")
        elif usernamevaningelogdaccount == "MisschienMarien":
            online_users = online("76561199058472552")
            offline_users = offline("76561199058472552")
        else:
            playerId = NaamNaarId(usernamevaningelogdaccount)
            online_users = online(playerId)
            offline_users = offline(playerId)
        return render_template('friends.html', online_users=online_users, offline_users=offline_users)

if __name__ == '__main__':
    data = "clear\r"
    serial_port.write(data.encode())
    pico_output = read_serial(serial_port)
    app.run(debug=True, threaded=True)
