from PyQt5 import Qt, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QTextEdit, QPushButton, QTableWidget, QTableWidgetItem
import sys
from library import *

app = QtWidgets.QApplication([])
win = uic.loadUi("C:\\Users\\NeAlexS\\Desktop\\Proekt2\\stu.ui")

Gr = Grup()
Gr.read_data_from_file("C:\\Users\\NeAlexS\\Desktop\\Proekt2\\text.txt")

def btnLoadTable():
    win.tableWidget.setRowCount(Gr.count)
    row = 0
    for x in Gr.A:
        if x in Gr.A:
            win.tableWidget.setItem(row, 0, QTableWidgetItem(Gr.A[x].fam))
            win.tableWidget.setItem(row, 1, QTableWidgetItem(Gr.A[x].name))
            win.tableWidget.setItem(row, 2, QTableWidgetItem(Gr.A[x].otchestvo))
            win.tableWidget.setItem(row, 3, QTableWidgetItem(Gr.A[x].rabdni))
            win.tableWidget.setItem(row, 4, QTableWidgetItem(Gr.A[x].podr))
            win.tableWidget.setItem(row, 5, QTableWidgetItem(Gr.A[x].zp))
            row += 1

def btnAppendPerson():
    List = [str(win.lineEdit_4.text()), str(win.lineEdit_5.text()), str(win.lineEdit_6.text()),
            str(win.lineEdit_7.text()), str(win.lineEdit_8.text()), str(win.lineEdit_9.text())]

    Gr.appendPerson(List)

    win.tableWidget.clear()
    btnLoadTable()

def btnEditPerson():
    if win.lineEdit_2.text() == '':
        win.lineEdit_2.setText('1')

    if win.lineEdit_3.text() == '':
        win.lineEdit_3.setText('1')

    x = int(win.lineEdit_2.text()) - 1
    y = int(win.lineEdit_3.text()) - 1

    if x <= win.tableWidget.rowCount() and y <= win.tableWidget.columnCount():
        List = []
        for i in range(win.tableWidget.columnCount()):
            item = win.tableWidget.item(x, i)
            if item is not None:
                List.append(item.text())
            else:
                List.append('')

        key = Gr.find_keyPerson(List)

        if key != -1:
            win.tableWidget.setItem(x, y, QTableWidgetItem(str(win.lineEdit.text())))

            List = []
            for i in range(win.tableWidget.columnCount()):
                item = win.tableWidget.item(x, i)
                if item is not None:
                    List.append(item.text())
                else:
                    List.append('')

            Gr.editPerson(key, List)

def btnDelPerson():
    List = [str(win.lineEdit_4.text()), str(win.lineEdit_5.text()), str(win.lineEdit_6.text()),
            str(win.lineEdit_7.text()), str(win.lineEdit_8.text()), str(win.lineEdit_9.text())]

    key = Gr.find_keyPerson(List)

    if key != -1:
        del Gr.A[key]
        Gr.count -= 1

    win.tableWidget.clear()
    btnLoadTable()

win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendPerson)
win.pushButton_4.clicked.connect(btnEditPerson)
win.pushButton_5.clicked.connect(btnDelPerson)

win.show()
sys.exit(app.exec_())