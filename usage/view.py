import sys
import controller
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

	def __init__(self,usageObj):
		super(Example, self).__init__()
		self.usageObj=usageObj
		self.initUI()

	def initUI(self):

		ramLabel = QtGui.QLabel('RAM')
		cpuLabel = QtGui.QLabel('CPU')

		refreshBtn = QtGui.QPushButton('Refresh')
		quitBtn = QtGui.QPushButton('Quit',self)

		refreshBtn.setShortcut('R')
		quitBtn.setShortcut('Q')

		quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		refreshBtn.clicked.connect(self.initDataViz)
		
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(ramLabel, 1, 0)
		grid.addWidget(cpuLabel, 1, 1)

		grid.addWidget(quitBtn,2,0)
		grid.addWidget(refreshBtn,2,1)

		self.setLayout(grid)

		self.setGeometry(300,300,350,300)
		self.setWindowTitle('Usage')
		self.show()

	
	def initDataViz(self):
		pass
	# 	data = self.usageObj.updateModel()
	# 	ramUsage = QtGui.QLabel(str(data[0][0]))
	# 	cpuUsage = QtGui.QLabel(str(data[1][0]))



def main(usageObj):

	app = QtGui.QApplication(sys.argv)
	ex = Example(usageObj)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()