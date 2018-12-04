from error_dialog import ErrorDialog
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile1 = "problem.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class MainWindow1(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_btn.clicked.connect(self.solve)
        self.clear_btn.clicked.connect(self.clear)
        self.change_prob_btn.clicked.connect(self.switch)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow1()
    window.show()
    sys.exit(app.exec_())
