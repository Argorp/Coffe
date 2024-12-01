import sys
from PyQt6.QtWidgets import QWidget, QTableWidgetItem


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 600, 600)
        self.ui()

    def ui(self):
        self.table = QTableWidgetItem(self)