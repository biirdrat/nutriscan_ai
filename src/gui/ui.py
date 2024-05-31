"""
This module defines the main window for a PyQt5 application and loads its UI from a .ui file.

Imports:
    os: Provides a way of using operating system-dependent functionality,
    including file and directory operations.
    PyQt5.uic: Used for loading UI files created with Qt Designer.
    PyQt5.QtWidgets: Provides classes for creating desktop-style user interfaces.
"""
import os
#Raises the issue "Unable to import PyQt5"
from PyQt5 import uic, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    """
    Represents the main window of the application.
    
    This class initializes the main window by loading its UI from a .ui file
    and sets up the necessary components.
    
    Methods:
        __init__(): Initializes the main window and loads the UI.
        get_ui_path(ui_name): Constructs the absolute path to the specified .ui file.
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = self.get_ui_path("mainwindow.ui")
        uic.loadUi(ui_path, self)

    def get_ui_path(self, ui_name):
        """
        Constructs the absolute path to the specified .ui file
        """
        current_dir = os.path.dirname(__file__)
        relative_path = os.path.join(current_dir, "ui", ui_name)
        return os.path.abspath(relative_path)
    