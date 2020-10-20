import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout, QHBoxLayout, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator

file_path = '../lib/database/dataset.csv'

class FloatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor

class TableWidget(QTableWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.setStyleSheet('font-size: 35px;')

        # set table dimension
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)

        self.setHorizontalHeaderLabels(df.columns)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.cellChanged[int, int].connect(self.updateDF)

    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text

class DFEditor(QWidget):
    # data = {
    #     'Col X': list('ABCD'),
    #     'col Y': [10, 20, 30, 40]
    # }
    df = pd.read_csv(file_path)
    # df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(1200, 800)

        mainLayout = QVBoxLayout()

        self.table = TableWidget(DFEditor.df)
        mainLayout.addWidget(self.table)

        button_print = QPushButton('Display DF')
        button_print.setStyleSheet('font-size: 30px')
        button_print.clicked.connect(self.print_DF_Values)
        mainLayout.addWidget(button_print)

        button_export = QPushButton('Export to CSV file')
        button_export.setStyleSheet('font-size: 30px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)

        button_new = QPushButton('New entry')
        button_new.setStyleSheet('font-size: 30px')
        button_new.clicked.connect(self._addRow)
        mainLayout.addWidget(button_new)

        button_remove = QPushButton('Remove')
        button_remove.setStyleSheet('font-size: 30px')
        button_remove.clicked.connect(self._removeRow)
        mainLayout.addWidget(button_remove, alignment=Qt.AlignTop)

        self.setLayout(mainLayout)

    def print_DF_Values(self):
        print(self.table.df)

    def export_to_csv(self):
        self.table.df.to_csv('Data export.csv', index=False)
        print('CSV file exported.')

    def _addRow(self):
        rowCount = self.table.rowCount()
        self.table.insertRow(rowCount )

    def _removeRow(self):
        if self.table.rowCount() > 0:
            self.table.removeRow(self.table.rowCount()-1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    demo = DFEditor()
    demo.show()

    sys.exit(app.exec_())
