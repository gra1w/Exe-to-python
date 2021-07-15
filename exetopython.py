#exe to python
import sys
import os
from shutil import copyfile
from PyQt5 import uic, QtGui, QtWidgets, QtCore

#define the directory where all widgets
#exports reside

class gui(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = uic.loadUi('gui.ui', self)

        self.ui.btnBrowse.clicked.connect(self.browse)
        self.ui.btnExit.clicked.connect(self.exit)
        self.ui.btnExit.clicked.connect(self.close)

    def browse(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', "", "*.exe")
        copyfile("c:/Python35/", name)
        return True

    def exit(self):
        sys.exit()

    def closeEvent(self, e):
        if e.reason == QtCore.Qt.Close:
            print("Exiting the program")
            sys.exit()
        super(gui, self).closeEvent(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
