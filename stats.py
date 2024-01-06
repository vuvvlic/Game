import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sql/stats_window.ui', self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())