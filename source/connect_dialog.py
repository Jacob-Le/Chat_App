# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QRect, Qt, QSize, QCoreApplication, QMetaObject, QTimer
import assets_rc


class ConnectUI(object):
    def initUI(self, ConnectUI):
        ConnectUI.setObjectName("ConnectUI")
        ConnectUI.resize(400, 175)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.jpeg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConnectUI.setWindowIcon(icon)

        self.gridLayout = QtWidgets.QGridLayout(ConnectUI)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(ConnectUI)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 153))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.infoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout_2.addWidget(self.infoLabel, 3, 0, 1, 2)

        self.connectButton = QtWidgets.QPushButton(
            self.scrollAreaWidgetContents)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout_2.addWidget(self.connectButton, 2, 0, 1, 2)

        self.hostLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.hostLabel.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.hostLabel.setObjectName("hostLabel")
        self.gridLayout_2.addWidget(self.hostLabel, 0, 0, 1, 1)

        self.hostLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.hostLineEdit.setMinimumSize(QSize(0, 30))
        self.hostLineEdit.setToolTip("")
        self.hostLineEdit.setWhatsThis("")
        self.hostLineEdit.setText("")
        self.hostLineEdit.setMaxLength(13)
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.gridLayout_2.addWidget(self.hostLineEdit, 1, 0, 1, 1)

        self.portLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.portLineEdit.setMinimumSize(QSize(0, 30))
        self.portLineEdit.setObjectName("portLineEdit")
        self.gridLayout_2.addWidget(self.portLineEdit, 1, 1, 1, 1)

        self.portLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.portLabel.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.portLabel.setObjectName("portLabel")
        self.gridLayout_2.addWidget(self.portLabel, 0, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ConnectUI)
        QMetaObject.connectSlotsByName(ConnectUI)

    def retranslateUi(self, ConnectUI):
        _translate = QCoreApplication.translate
        ConnectUI.setWindowTitle(_translate(
            "ConnectUI", "Connect to SLAC Chat"))
        self.infoLabel.setText(_translate(
            "ConnectUI", "Default is: 127.0.0.1 (Host) and 33002 (Port)"))
        self.connectButton.setText(_translate("ConnectUI", "Connect"))
        self.hostLabel.setText(_translate("ConnectUI", "Host IP address:"))
        self.portLabel.setText(_translate("ConnectUI", "Port number:"))


class ConnectDialog(QtWidgets.QDialog, ConnectUI):

    def __init__(self, client):
        QtWidgets.QDialog.__init__(self)
        self.initUI(self)
        self.client = client

        self.default_info = "Default is: 127.0.0.1 (Host) and 33002 (Port)"


    @pyqtSlot()
    def on_connectButton_clicked(self):
        host = self.hostLineEdit.text()
        port = self.portLineEdit.text()

        if len(host) <= 0:
            host = '127.0.0.1'
        if len(port) <= 0:
            port = '33002'

        try:
            if self.valid_address(host) and int(port) < 65535:
                self.client.set_address(host, port)
                self.client.connect()
                self.accept()
            else:
                self.inform(
                    "Invalid address: Host: %s and Port: %s" % (host, port), error=True)
        except Exception as e:
            print(e)
            self.inform("Invalid address: Host: %s and Port: %s" % (host, port), error=True)

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

    """Helper function that checks if host address is valid
    """
    def valid_address(self, address):
        try:
            numbers = address.split('.')
            valid = [int(b) for b in numbers]
            valid = [b for b in valid if b >= 0 and b <= 255]
            return len(numbers) == 4 and len(valid) == 4
        except:
            return False
