"""Module that contains implementation for a ChatWindow
"""
import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QRect, QMetaObject, QSize, QCoreApplication, Qt, QThread
from PyQt5.QtGui import QColor, QFont, QIcon, QPixmap

from login_window import LoginDialog
from connect_dialog import ConnectDialog

import assets_rc

"""UI code generated from QtDesigner, slightly edited
"""


class ChatUI(object):
    def initUI(self, ChatUI):
        ChatUI.setObjectName("ChatUI")
        ChatUI.resize(800, 600)
        self.centralwidget = QWidget(ChatUI)
        self.centralwidget.setObjectName("centralwidget")

        textFont = QFont("Sans Serif", 14)
        uiFont = QFont("Sans Serif", 12)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/icon.jpeg"), QIcon.Normal, QIcon.Off)
        ChatUI.setWindowIcon(icon)

        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.windowScrollArea = QScrollArea(self.centralwidget)
        self.windowScrollArea.setWidgetResizable(True)
        self.windowScrollArea.setObjectName("windowScrollArea")

        self.windowScrollAreaContents = QWidget()
        self.windowScrollAreaContents.setGeometry(QRect(0, 0, 778, 536))
        self.windowScrollAreaContents.setObjectName("windowScrollAreaContents")
        self.gridLayout_2 = QGridLayout(
            self.windowScrollAreaContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.recipients = QComboBox(self.windowScrollAreaContents)
        self.recipients.setFont(textFont)
        sizePolicy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.recipients.sizePolicy().hasHeightForWidth())
        self.recipients.setSizePolicy(sizePolicy)
        self.recipients.setMinimumSize(QSize(80, 60))
        self.recipients.setMaximumSize(QSize(160, 100))
        self.recipients.setLayoutDirection(Qt.LeftToRight)
        self.recipients.setObjectName("recipients")
        self.recipients.addItem("")
        self.gridLayout_2.addWidget(self.recipients, 2, 2, 1, 1)

        self.sendButton = QPushButton(
            self.windowScrollAreaContents)
        self.sendButton.setFont(textFont)
        self.sendButton.setAutoDefault(True)
        sizePolicy = QSizePolicy(
            QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QSize(60, 60))
        self.sendButton.setMaximumSize(QSize(120, 60))
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_2.addWidget(self.sendButton, 2, 1, 1, 1)

        self.chatBox = QLineEdit(self.windowScrollAreaContents)
        self.chatBox.setFont(textFont)
        sizePolicy = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.chatBox.sizePolicy().hasHeightForWidth())
        self.chatBox.setSizePolicy(sizePolicy)
        self.chatBox.setMinimumSize(QSize(100, 40))
        self.chatBox.setMaximumSize(QSize(16777215, 60))
        self.chatBox.setObjectName("chatBox")
        self.gridLayout_2.addWidget(self.chatBox, 2, 0, 1, 1)

        self.connectionStatusLabel = QLabel(
            self.windowScrollAreaContents)
        self.connectionStatusLabel.setFont(uiFont)
        sizePolicy = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.connectionStatusLabel.sizePolicy().hasHeightForWidth())
        self.connectionStatusLabel.setSizePolicy(sizePolicy)
        self.connectionStatusLabel.setObjectName("connectionStatusLabel")
        self.gridLayout_2.addWidget(self.connectionStatusLabel, 0, 0, 1, 2)

        self.chatLog = QListWidget(self.windowScrollAreaContents)
        self.chatLog.setFocusPolicy(Qt.ClickFocus)
        self.chatLog.setFont(textFont)
        self.chatLog.setVerticalScrollMode(
            QAbstractItemView.ScrollPerItem)
        self.chatLog.setResizeMode(QListWidget.Adjust)
        self.chatLog.setSelectionRectVisible(False)
        self.chatLog.setObjectName("chatLog")
        self.gridLayout_2.addWidget(self.chatLog, 1, 0, 1, 3)
        self.windowScrollArea.setWidget(self.windowScrollAreaContents)
        self.gridLayout.addWidget(self.windowScrollArea, 0, 0, 1, 1)
        ChatUI.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(ChatUI)
        self.menubar.setGeometry(QRect(0, 0, 800, 40))
        self.menubar.setObjectName("menubar")

        self.optionMenu = QMenu(self.menubar)
        self.optionMenu.setObjectName("optionMenu")
        ChatUI.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(ChatUI)
        self.statusbar.setObjectName("statusbar")
        ChatUI.setStatusBar(self.statusbar)

        self.actionMute = QAction(ChatUI)
        self.actionMute.setCheckable(True)
        self.actionMute.setObjectName("actionMute")
        # self.actionEncryption = QAction(ChatUI)
        # self.actionEncryption.setCheckable(True)
        # self.actionEncryption.setObjectName("actionEncryption")
        self.actionConnect = QAction(ChatUI)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QAction(ChatUI)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionQuit = QAction(ChatUI)
        self.actionQuit.setObjectName("actionQuit")

        self.optionMenu.addAction(self.actionMute)
        # self.optionMenu.addAction(self.actionEncryption)
        self.optionMenu.addSeparator()
        self.optionMenu.addAction(self.actionConnect)
        self.optionMenu.addAction(self.actionDisconnect)
        self.optionMenu.addSeparator()
        self.optionMenu.addAction(self.actionQuit)

        self.menubar.addAction(self.optionMenu.menuAction())

        self.retranslateUi(ChatUI)
        QMetaObject.connectSlotsByName(ChatUI)

    def retranslateUi(self, ChatUI):
        _translate = QCoreApplication.translate
        ChatUI.setWindowTitle(_translate("ChatUI", "SLAC Chat"))
        self.recipients.setToolTip(_translate(
            "ChatUI", "Choose a user to send your message to:"))
        self.recipients.setWhatsThis(_translate(
            "ChatUI", "Choose a user to send your message to:"))
        self.recipients.setAccessibleName(
            _translate("ChatUI", "Recipients"))
        self.recipients.setItemText(0, _translate("ChatUI", "ALL"))

        self.sendButton.setText(_translate("ChatUI", "Send"))

        self.chatBox.setPlaceholderText(
            _translate("ChatUI", "Type here..."))

        self.connectionStatusLabel.setText(_translate(
            "ChatUI", "SLAC Chat Connection Status:"))

        self.optionMenu.setTitle(_translate("ChatUI", "Menu"))

        self.actionMute.setText(_translate("ChatUI", "Mute Notifications"))
        # self.actionEncryption.setText(
        #     _translate("ChatUI", "Encrypt Messages"))
        self.actionConnect.setText(_translate("ChatUI", "Connect"))
        self.actionDisconnect.setText(_translate("ChatUI", "Disconnect"))
        self.actionQuit.setText(_translate("ChatUI", "Quit SLAC Chat"))


"""Subclasses ChatUI, contains all chat window functionality.
"""
class ChatWindow(QMainWindow, ChatUI):

    def __init__(self, client, parent=None):
        QMainWindow.__init__(self, parent=parent)

        self.name = ""  # Client name
        self.client = client
        self.login_window = LoginDialog(self)

        # Setting up UI
        self.encrypting = False
        self.muted = False
        self.initUI(self)

        # Connect signals and slots
        self.chatBox.returnPressed.connect(self.on_sendButton_clicked)
        # self.actionEncryption.toggled.connect(self.toggle_encryption)
        self.actionMute.toggled.connect(self.toggle_mute)
        self.actionConnect.triggered.connect(self.action_connect)
        self.actionDisconnect.triggered.connect(self.action_disconnect)
        self.actionQuit.triggered.connect(self.quit_button_event)

        # Connect signals from qthread that handles incoming messages
        self.client.msg_recieved.connect(self.got_msg)
        self.client.update_widgets.connect(self.update_info)
        self.client.conn_status.connect(self.update_conn)

        # Setup thread for running client connection
        self.client_thread = QThread()

        self.prompt_login()

    # ---------------------------PyQt slots----------------------------------------#
    """Slot that listens for a "msg_recieved" signal from the client. Adds messages to chat log
    msg: string passed along with the signal.  Used to add a message item to the log.
    """
    @pyqtSlot(object)
    def got_msg(self, msg):
        self.add_msg_item(msg)
        if not self.muted:
            print('\a')

    """Slot that listens for a "update_widgets" signal from the client.  Updates widgets with info.
    """
    @pyqtSlot()
    def update_info(self):
        # Ensure that this client is not on the list
        people = [user for user in self.client.users if user != self.client.name]
        self.recipients.clear()
        self.recipients.addItems(people)

    """Slot that detects the status of the connection the the server, and updates a label accordingly
    """
    @pyqtSlot(object)
    def update_conn(self, status):
        if status:
            connection = "Connected"
            self.actionConnect.setEnabled(False)
            self.actionDisconnect.setEnabled(True)
            self.chatBox.setEnabled(True)
            self.sendButton.setEnabled(True)
            self.recipients.setEnabled(True)
        else:
            connection = "Disconnected"
            self.add_msg_item("Goodbye!")  # Say goodbye on disconnect
            self.actionConnect.setEnabled(True)
            self.actionDisconnect.setEnabled(False)
            self.chatBox.setEnabled(False)
            self.sendButton.setEnabled(False)
            self.recipients.setEnabled(False)

        self.connectionStatusLabel.setText(
            "SLAC Chat Connection Status: %s" % connection)

    """Sends message on "Send" button press.  The return/enter key is also set up to trigger this function.
    """
    @pyqtSlot()
    def on_sendButton_clicked(self):
        if self.chatBox.text() != "":
            self.send_chat_message()

    """Menu option that toggles encryption
    """
    @pyqtSlot()
    def toggle_encryption(self):
        self.encrypting = not self.encrypting

    """Menu option that toggles notification beep on message recieved events
    """
    @pyqtSlot()
    def toggle_mute(self):
        self.muted = not self.muted

    @pyqtSlot()
    def action_connect(self):
        if not self.client.is_connected:
            confirm = ConnectDialog(self.client)
            confirm.exec_()
            self.prompt_login()
            

    @pyqtSlot()
    def action_disconnect(self):
        if self.client.is_connected:
            confirm = QMessageBox.question(
            self, "Disconnect", "Are you sure you want to disconnect?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            if confirm == QMessageBox.Yes:
                if self.client.is_connected:
                    # send {QUIT} message to server
                    self.client.disconnect()
                    self.client_thread.quit()
                    self.client_thread.wait()
            else:
                confirm.hide()

    """Menu option that quits the application.  Functions identically to window "x" button
    """
    @pyqtSlot()
    def quit_button_event(self):
        # Triggered when close is chosen in the menu
        self.close()

    """Overides closeEvent().  Checks if user truly wishes to close the application.
    Cleans up socket connection.
    """
    def closeEvent(self, event):
        confirm = QMessageBox.question(
            self, "Logout", "Are you sure you want to quit?", QMessageBox.No | QMessageBox.Yes, QMessageBox.No)

        if confirm == QMessageBox.Yes:
            if self.client.is_connected:
                 # send {QUIT} message to server
                    self.client.disconnect()
                    self.client_thread.quit()
                    self.client_thread.wait()
            print("Closing...")
            QCoreApplication.quit()
        else:
            event.ignore()

    # ----------------------------------UI Functionality-------------------------------------------#
    """Prompts the user to login with a username through a QDialog window.
    """

    def prompt_login(self):
        self.client.moveToThread(self.client_thread)
        self.client_thread.started.connect(self.client.run)
        self.client_thread.start()
        self.login_window.exec_()

    """Adds recieved messages to the chat log (QListWidget).  Alternates between grey and white entries.
    Automatically scrolls to last item added to the list.
    """

    def add_msg_item(self, content):
        date = datetime.datetime.now()  # Append
        msg_item = QListWidgetItem("(%s) %s" % (date.strftime("%X"), content))
        # msg_item = QtWidgets.QLabel('%s<b>%s</b> %s' % )
        if self.chatLog.count() % 2 == 0:
            msg_item.setBackground(QColor('#e8e8e8'))
        else:
            msg_item.setBackground(QColor('#ffffff'))

        self.chatLog.addItem(msg_item)
        # Automatically scroll to newest message
        self.chatLog.scrollToItem(msg_item)

    """Takes existing text from chat box (QLineEdit) and sends it to the recipient (QComboBox) through
    the server.
    """

    def send_chat_message(self):
        message = self.chatBox.text()
        recipient = str(self.recipients.currentText())

        if self.client.is_connected:
            # Send message via client
            self.client.send_message(message, prefix="{%s}" % recipient)
            # Clear Chat box
            self.chatBox.setText("")
        else:
            message = "SLAC Chat Bot: Message not sent, SLAC Chat Client not connected!"

        # add message to chat log
        if recipient != "ALL":
            self.add_msg_item("%s: %s" % (self.client.name, message))
