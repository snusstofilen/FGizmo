import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import random, string

def base_str():
    return random.choice(string.ascii_letters)+ random.choice(string.digits)

class CustomSortModel(QtGui.QSortFilterProxyModel):
    def lessThan(self, left, right):
        #USE CUSTOM SORTING LOGIC HERE
        lvalue = left.data().toString()
        rvalue = right.data().toString()
        return lvalue[::-1] < rvalue[::-1]

class CustomTableWidget(QtGui.QWidget):
    def __init__(self, parent):
        super(CustomTableWidget, self).__init__(parent)
        self.model = QtGui.QStandardItemModel(rows, columns)
        self.table = QtGui.QTableView()
        self.proxy_model = CustomSortModel()
        self.setItems()
        self.table.setSortingEnabled(True)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.table)

        self.model.itemChanged.connect(self.update_proxy)

        self.update_proxy()

    def setItems(self):
        self.model.setHorizontalHeaderLabels([str(x) for x in range(1, columns+1)])
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QStandardItem(str(base_str()))
                self.model.setItem(row, column, item)

    def update_proxy(self, item=None):
        self.proxy_model.setSourceModel(self.model)
        self.table.setModel(self.proxy_model)

class StandardTableWidget(QtGui.QTableWidget):
    def __init__(self, parent):
        super(StandardTableWidget, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setRowCount(rows)
        self.setColumnCount(columns)
        self.setSortingEnabled(True)
        self.setItems()

    def setItems(self):
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QTableWidgetItem()
                item.setText(str(base_str()))
                self.setItem(row, column, item)

if ( __name__ == '__main__' ):

    rows = 10
    columns = 5
    useCustomSorting = True


    app = None
    if ( QtGui.QApplication.instance() is None ):
        app = QtGui.QApplication([])

    if useCustomSorting:
        widget = CustomTableWidget(None)
    else:
        widget = StandardTableWidget(None)

    widget.show()

    if (app):
        app.exec_()
