import sys
import sqlite3
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QWidget
from PyQt6 import uic
from collections import defaultdict
from main2 import Ui_MainWindow
from addEditCoffeeForm import Ui_Form


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.con = None
        self.setupUi(self)
        self.roasting_translate = defaultdict(str)
        self.variation_translate = defaultdict(str)
        self.setGeometry(0, 0, 800, 800)
        # uic.loadUi("main2.ui", self)
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
        self.new_rep.clicked.connect(self.upd)

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

    def upd(self):
        self.upd_table = Upd_Table(self)
        self.upd_table.show()


class Upd_Table(QWidget, Ui_Form):
    def __init__(self, main: Main):
        super().__init__()
        self.cur_main = main
        self.setupUi(self)
        self.ui()

    def ui(self):
        self.pushButton.clicked.connect(self.ins_rep)

    """Добавление записи в таблицу"""
    def ins_rep(self):
        self.lineEdit.setText("Пока не работает :)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())