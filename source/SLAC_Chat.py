"""Main program for the SLAC Chat client.
"""

import os, sys
import argparse
#import datetime

# from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QApplication

from chat_window import ChatWindow
from client import Client

if __name__ == "__main__":
    #Setup host and port for client connection using args
    parser = argparse.ArgumentParser(description="SLAC Chat Client")
    parser.add_argument("--host", help="Host IP", default="127.0.0.1")
    parser.add_argument("--port", help="Port number", default="33002")
    args = parser.parse_args()

    app = QApplication(sys.argv)
    chat_client = Client(args.host, args.port)
    window = ChatWindow(chat_client)
    window.show()
    sys.exit(app.exec_())
