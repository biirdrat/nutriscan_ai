"""
This module initializes and starts a PyQt5 application by creating and displaying the main window.

Imports:
    sys: Provides access to some variables used or maintained by the Python interpreter.
    os: Provides a way of using operating system-dependent functionality.
    PyQt5.QtWidgets.QApplication: Manages the GUI application's control flow and main settings.
    GUI.ui.MainWindow: The main window class of the application, defined in the 'GUI.ui' module.
"""
import sys
import os
from PyQt5.QtWidgets import QApplication
from GUI.ui import MainWindow

def main():
    """
    The main entry point of the application.
    
    This function initializes the QApplication, creates the main window,
    displays it, and starts the application's event loop.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# If this module is being run as the main program, execute the main function.
if __name__ == '__main__':
    main()
