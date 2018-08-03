"""Module that contains implementation for a LoginDialog
"""
import re

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, QRect, QMetaObject, QSize, QCoreApplication, Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap, QFont
#from fbs_runtime.application_context import cached_property

import assets_rc

"""UI code generated from QtDesigner, slightly edited.
"""


class LoginUI(object):
    def initUI(self, LoginUI):
        LoginUI.setObjectName("LoginUI")
        LoginUI.resize(480, 260)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/images/icon.jpeg"), QIcon.Normal, QIcon.Off)
        LoginUI.setWindowIcon(icon)

        self.gridLayout_2 = QGridLayout(LoginUI)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.scrollArea = QScrollArea(LoginUI)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 458, 238))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Title = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout.addWidget(self.Title)

        self.Subtitle = QLabel(self.scrollAreaWidgetContents)
        self.Subtitle.setAlignment(Qt.AlignCenter)
        self.Subtitle.setObjectName("Subtitle")
        self.verticalLayout.addWidget(self.Subtitle)

        self.usernameBox = QLineEdit(self.scrollAreaWidgetContents)
        self.usernameBox.setText("")
        self.usernameBox.setAlignment(Qt.AlignCenter)
        self.usernameBox.setObjectName("usernameBox")
        self.verticalLayout.addWidget(self.usernameBox)

        self.loginButton = QPushButton(self.scrollAreaWidgetContents)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)

        self.infoLabel = QLabel(self.scrollAreaWidgetContents)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setStyleSheet("color: red")
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(LoginUI)
        QMetaObject.connectSlotsByName(LoginUI)

    def retranslateUi(self, LoginUI):
        _translate = QCoreApplication.translate
        LoginUI.setWindowTitle(_translate(
            "LoginUI", "SLAC Chat Login"))

        self.Title.setText(_translate("LoginUI", "SLAC Chat"))

        self.Subtitle.setText(_translate(
            "LoginUI", "The Unofficial Chat Service of SLAC"))

        self.loginButton.setText(_translate("LoginUI", "Login"))

        self.infoLabel.setText(_translate("LoginUI", ""))

        self.usernameBox.setPlaceholderText(_translate(
            "LoginUI", "Enter username here..."))


"""Login dialog window displayed whenever first entering SLAC Chat.
Handles username registration.
"""


class LoginDialog(QDialog, LoginUI):

    def __init__(self, chat_window, parent=None):
        QDialog.__init__(self, parent=parent)
        self.chat_window = chat_window
        self.initUI(self)

        self.default_info = ""
        self.u_rules = re.compile(
            r'[^a-zA-Z\d]', re.IGNORECASE)  # Rules for username
        self.bad_names = re.compile(r'\ball\b', re.IGNORECASE)

    """Helper slot function that returns the info back to it's default message
    """
    @pyqtSlot()
    def default_inform(self):
        self.inform(self.default_info)

    """Helper function that changes the (QLabel) below the connectButton to display a message
    """

    def inform(self, msg, error=False):
        if error:
            self.infoLabel.setStyleSheet("color: red")
            QTimer.singleShot(7000, self.default_inform)
        else:
            self.infoLabel.setStyleSheet("color: black")
        self.infoLabel.setText(msg)

    """Passes the username entered in the (QLineEdit) to the server for username registration
    Rejects invalid usernames
    """
    @pyqtSlot()
    def on_loginButton_clicked(self):
        username = self.usernameBox.text()

        # Match using regex: reject any non alphanumeric characters,
        #  spaces, the word 'all', and usernames longer than 24 characters
        if self.u_rules.match(username) is not None or self.bad_names.match(username) is not None or len(username) > 24 or len(username) == 0:
            self.inform(
                "Please enter a valid username.\n(At least one character, maximum 24 characters, no special characters,\n and no spaces)", True)
        elif self.chat_window.client.is_connected:
            # Pass to client
            self.chat_window.client.register(username)
            self.inform("Registering with SLAC Chat server...")

            # Check if name is taken
            # if self.chat_window.client.name == "":
            #     self.inform("The username ""%s"" is taken!" % username, True)
            #     return

            # Proceed to chat window
            self.accept()
        else:
            self.inform(
                "Not connected to SLAC Chat Server,\nplease try again later", True)

