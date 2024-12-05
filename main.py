import sys
import sqlite3
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from PyQt6 import uic
from collections import defaultdict


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = None
        self.roasting_translate = defaultdict(str)
        self.variation_translate = defaultdict(str)
        self.setGeometry(0, 0, 600, 600)
        uic.loadUi("main.ui", self)
        self.ui()

    def ui(self):
        self.button.clicked.connect(self.reset_table)
        self.con = sqlite3.connect("coffee")
        roasting = self.con.execute("select * from Roasting").fetchall()
        view = self.con.execute("select * from View").fetchall()
        for i in roasting:
            self.roasting_translate[str(i[0])] = i[1]
        for i in view:
            self.variation_translate[str(i[0])] = i[1]

    def reset_table(self):
        header = ['Name', 'Degree of roasting', 'Variation', 'Description of taste',
                  'Cost', 'Size of package']
        res = self.con.execute("select * from Coffees").fetchall()
        self.table.setColumnCount(len(res[0]) - 1)
        self.table.setRowCount(len(res) + 1)
        for i, el in enumerate(header):
            self.table.setItem(0, i, QTableWidgetItem(el))
        for i, row in enumerate(res):
            for j, el in enumerate(row):
                cur = str(el)
                if j == 2:
                    cur = self.roasting_translate[cur]
                if j == 3:
                    cur = self.variation_translate[cur]
                if j != 0:
                    self.table.setItem(i + 1, j - 1, QTableWidgetItem(cur))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())