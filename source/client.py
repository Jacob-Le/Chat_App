"""Module that contains an implementation of a Client that can connect to a server
"""

from socket import AF_INET, socket, SOCK_STREAM, gaierror
from threading import Thread
from collections import defaultdict

from PyQt5.QtCore import QObject, pyqtSignal

BUFSIZE = 2048  # Socket buffer size

class Client(QObject):
    def __init__(self, host, port):
        QObject.__init__(self)
        # Set up the client
        self.is_connected = False  # Handy connection flag
        self.address = (host, int(port))  # Address tuple

        self.server = None  # server socket connection
        self.delim = "^"  # Delimiter for message recieving over TCP
        self.name = ""  # Name of client

        self.public_key = None  # Cipher Key from server

        self.recv_error = None  # Records error recieved

        self.users = []  # Set of users in the chatroom

    # Setup signals
    msg_recieved = pyqtSignal(object)
    conn_status = pyqtSignal(object)
    vet_username = pyqtSignal(object)
    update_widgets = pyqtSignal()

    """Main thread loop for recieving and handling messages from the server.
    """
    def run(self):
        # Main loop for handling server - client messages
        if not self.is_connected:
            self.connect()

        while self.is_connected:
            try:
                # Get messages from socket
                for msg in self.read_msg():
                    
                    if self.is_connected and msg == "":
                        self.disconnect()
                        print("Empty/Invalid message!")
                        break

                    # Client list, should be recieved on login, and any subsequent user logins
                    if msg.startswith("{CLIENTS}"):
                        msg_params = msg.split("}")
                        self.users = msg_params[1].split("|")
                        self.users.append("ALL")
                        # Update recipients
                        self.update_widgets.emit()
                        msg = ""
                        continue

                    # Message broadcasted to all users
                    if msg.startswith("{MSG}"):
                        msg_params = msg.split("}")
                        contents = msg_params[1]
                        self.msg_recieved.emit(contents)
                        continue

                    # Accept and process any errors
                    if msg.startswith("{ERROR}"):
                        msg_params = msg.split("}")
                        self.recv_error = int(msg_params[1])

                        if self.recv_error == 1:  # Rejected username
                            print("Username is taken!")
                            #self.name = ""
                        else:
                            print("Error number %d encountered!" % self.recv_error)
                        continue

                    try:
                        self.msg_recieved.emit(msg)
                    except:
                        print("Error parsing the message: %s" % msg)
            except (ConnectionError, OSError) as e:
                print(e)
                self.disconnect()
                break

    """ Helper function that reads messages from the socket. Separates messages via a delimter
    to ensure there is no message overflow.
    """
    def read_msg(self):
        buffer = ""
        data = True
        while data:
            global BUFSIZE
            data = self.server.recv(BUFSIZE)
            buffer += str(data.decode("utf-8"))

            while buffer.find(self.delim) != -1:
                msg, buffer = buffer.split(self.delim, 1)
                print(msg)
                yield msg
        return

    """Helper function that sets the address that the client will connect to next
    """
    def set_address(self, host, port):
        self.address = (host, int(port))

    """Helper function that attempts to connect to the server.
    addr: (string, int) Tuple that contains (host, port) 
    """
    def connect(self):
        if not self.is_connected:
            print("Connecting...")
            try:
                self.server = socket(AF_INET, SOCK_STREAM)
                self.server.connect(self.address)
                self.is_connected = True
                self.conn_status.emit(self.is_connected)
                print("Connected to: %s %s" % (self.address[0], str(self.address[1])))
            except ConnectionError as e:
                print("Unable to connect")
                self.is_connected = False
                self.conn_status.emit(self.is_connected)

    """ Helper function that disconnects from the server.
    """
    def disconnect(self):
        if self.is_connected:
            self.send_message("", "{QUIT}")
            self.is_connected = False
            self.conn_status.emit(self.is_connected)
            print("Disconnecting from SLAC Chat server...")
            self.server.close()

    """Helper function that sends a a {REGISTER} message to the server, along with a username
    username: 
    """
    def register(self, username):
        self.send_message(username, prefix="{REGISTER}")
        self.name = username
        print("Registering with %s" % self.name)

    """Send a message to the server. 
    msg: string message
    prefix: string protocol/recipient encapsulated by {} 
    """
    def send_message(self, msg, prefix=""):
        send_msg = bytes(prefix + msg, "utf-8")
        self.server.send(send_msg)
