"""
This module initializes and starts a PyQt5 application by creating and displaying the main window.

Imports:
    sys: Provides access to some variables used or maintained by the Python interpreter 
    and to functions that interact with the interpreter.
    os: Provides a way of using operating system-dependent functionality.
    PyQt5.QtWidgets.QApplication: Manages the GUI application's control flow and main settings.
    gui.ui.MainWindow: The main window class of the application, defined in the 'gui.ui' module.
"""
#Currently raising an issue, "Unable to import PyQt5.QtWidgets"
import sys
import os
from PyQt5.QtWidgets import QApplication
from gui.ui import MainWindow

def main():
    """
    The main entry point of the application.
    
    This function initializes the QApplication, creates the main window,
    displays it, and starts the application's event loop.
    
    Steps:
        1. Initialize the QApplication with command line arguments.
        2. Create an instance of the MainWindow.
        3. Display the main window.
        4. Start the event loop.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
