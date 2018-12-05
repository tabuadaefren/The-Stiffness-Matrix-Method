from error_dialog import ErrorDialog
import sys
from PyQt4 import QtCore, QtGui, uic
import numpy as np
import math

global A, E, I, x1, x2, x3, y1, y2, L, cosTheta, sinTheta, AL2I, EIL3

qtCreatorFile1 = "problem.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile1)

class ProblemWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calc_btn.clicked.connect(self.Process)
        self.clear_btn.clicked.connect(self.clear)
        
    def clear(self):
    	self.elastic_modulus.clear()
        self.inertia.clear()
        self.area.clear()
        self.x1.clear()
        self.x2.clear()
        self.x3.clear()
        self.y1.clear()
        self.y2.clear()
        self.P.clear()
        self.w.clear()
        self.M.clear()

    def Process(self):
    	E = self.elastic_modulus.text()
        I = self.inertia.text()
        A = self.area.text()
        x1 = self.x1.text()
        x2 = self.x2.text()
        x3 = self.x3.text()
        y1 = self.y1.text()
        y2 = self.y2.text()
        P = self.P.text()
        w = self.w.text()
        M = self.M.text() 

        param = [E, I, A, x1, x2, x3, y1, y2, P, w, M]
        blank_inputs = self.checkBlanks(param)

        if(blank_inputs == 1):
            if(('-' not in E)&('-' not in I)&('-' not in A)&('-' not in x1)&('-' not in x2)&('-' not in x3)&('-' not in y1)&('-' not in y2)):
                ss = self.compute(float(E), float(I), float(A), float(x1)*1000, float(x2)*1000, float(x3)*1000, float(y1)*1000, float(y2)*1000, float(P), float(w), float(M))
                n = 3
                m = 0
                for i in ss:
                    if (round(ss.item(m), n) == -0.0):
                        ss[m] = 0.0
                        m +=1
                    else:
                        m +=1
                self.d1.setText(str(round(ss.item(0), n)))
                self.d2.setText(str(round(ss.item(1), n)))
                self.d3.setText(str(round(ss.item(2), n)))
                self.d4.setText(str(round(ss.item(3), n)))
                self.d5.setText(str(round(ss.item(4), n)))
                self.d6.setText(str(round(ss.item(5), n)))
                self.p1.setText(str(round(ss.item(6), n)))
                self.p2.setText(str(round(ss.item(7), n)))
                self.p3.setText(str(round(ss.item(8), n)))
                self.p4.setText(str(round(ss.item(9), n)))
                self.p5.setText(str(round(ss.item(10), n)))
                self.p6.setText(str(round(ss.item(11), n)))
                self.r7.setText(str(round(ss.item(12), n)))
                self.r8.setText(str(round(ss.item(13), n)))
                self.r9.setText(str(round(ss.item(14), n)))
                self.r10.setText(str(round(ss.item(15), n)))
                self.r11.setText(str(round(ss.item(16), n)))
                self.r12.setText(str(round(ss.item(17), n)))
            else:
                self.showErrorDialog()
        else:
            self.showErrorDialog()

        
    def Calculations():
    	Xb = [0, x1, x1+x2]
        Xe = [ x1, x1+x2, x1+x2+x3]
        Yb = [0, y1, y1]
        Ye = [y1, y1, y1-y2]

        xd = [ Xe[0]-Xb[0], Xe[1]-Xb[1], Xe[2]-Xb[2] ]
        yd = [ Ye[0]-Yb[0], Ye[1]-Yb[1], Ye[2]-Yb[2] ]

        L = [sqrt( (xd[0])^2 + (yd[0])^2), sqrt( (xd[1])^2 + (yd[1])^2 ), sqrt( (xd[2])^2 + (yd[2])^2 )]
        
        cosTheta = [xd[0]/L[0], xd[1]/L[1], xd[2]/L[2]]
        sinTheta = [yd[0]/L[0], yd[1]/L[1], yd[2]/L[2]]
        
        AL2I = [(A*L[0]**2)/I, ((A*L[1]**2)/I), ((A*L[2]**2)/I)]
        EIL3 = [((E*I)/(L[0]**3)), ((E*I)/(L[1]**3)), ((E*I)/(L[2]**3))]



    def showErrorDialog(self):
        self._new_window = ErrorDialog()
        self._new_window.show()

    def checkBlanks(self, param):
        t = 1
        for n in param:
            if (' ' in n) or (n == ''):
                self._new_window = ErrorDialog()
                self._new_window.show()
                t = 0
                break
        return t

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = ProblemWindow()
    window.show()
    sys.exit(app.exec_())
