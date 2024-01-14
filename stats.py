import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QAbstractItemView, QMenu, QAction
from PyQt5 import QtCore
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.note_deleteAction = None
        self.current_row = None
        uic.loadUi('sql/stats_window.ui', self)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.on_note_view_click)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.contextNotes)

    def contextNotes(self, point):
        self.on_note_view_click()
        menu = QMenu()
        self.note_deleteAction = QAction('Удалить запись', menu)
        self.note_deleteAction.triggered.connect(self.delete_note)
        if self.tableWidget.itemAt(point):
            menu.addAction(self.note_deleteAction)
        else:
            pass
        menu.exec(self.tableWidget.mapToGlobal(point))

    def on_note_view_click(self):
        self.current_row = self.tableWidget.currentRow()
        self.tableWidget.clearSelection()
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.tableWidget.selectRow(self.current_row)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

    def delete_note(self):
        self.tableWidget.removeRow(self.current_row)
        con = sqlite3.connect('sql/database.db')
        cur = con.cursor()
        cur.execute(f"DELETE FROM solo WHERE id = {self.current_row + 1}")
        cur.execute(f"UPDATE solo SET id = id - 1 WHERE id > {self.current_row + 1}")
        con.commit()
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())