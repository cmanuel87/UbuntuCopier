import sys
from PyQt4 import QtCore, QtGui, Qt
from copier import Ui_Form

class MyCopier(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = MyCopier()
	myapp.show()
	sys.exit(app.exec_())

