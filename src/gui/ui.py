import os
from PyQt5 import uic, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui_path = self.get_ui_path("mainwindow.ui")
        uic.loadUi(ui_path, self)

    def get_ui_path(self, ui_name):
        current_dir = os.path.dirname(__file__)
        relative_path = os.path.join(current_dir, "ui", ui_name)
        return os.path.abspath(relative_path)