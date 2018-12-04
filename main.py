import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile1 = "main.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class WelcomeWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(WelcomeWindow,self).__init__()
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.prob1_btn.clicked.connect(self.openProb1)
        self.prob2_btn.clicked.connect(self.openProb2)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = WelcomeWindow()
 
    window.show()
    sys.exit(app.exec_())