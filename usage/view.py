import sys
import controller
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

	def __init__(self,usageObj):
		super(Window, self).__init__()
		self.usageObj=usageObj

		self.initUI(usageObj)


	def initUI(self, usageObj):

		ramLabel = QtGui.QLabel(usageObj.data[0][0])
		cpuLabel = QtGui.QLabel(usageObj.data[1][0])

		ramUsage = QtGui.QLabel(str(usageObj.data[0][1]))
		cpuUsage = QtGui.QLabel(str(usageObj.data[1][1]))

		refreshBtn = QtGui.QPushButton('Refresh')
		quitBtn = QtGui.QPushButton('Quit',self)

		refreshBtn.setShortcut('R')
		quitBtn.setShortcut('Q')

		quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		#refreshBtn.clicked.connect(data)
		
		grid = QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(ramLabel, 0, 0)
		grid.addWidget(cpuLabel, 0, 1)

		grid.addWidget(ramUsage, 1, 0)
		grid.addWidget(cpuUsage, 1, 1)

		grid.addWidget(quitBtn,2,0)
		grid.addWidget(refreshBtn,2,1)

		self.setLayout(grid)

		self.setGeometry(300,300,350,300)
		self.setWindowTitle('Usage')
		self.show()


def main(usageObj):

	app = QtGui.QApplication(sys.argv)
	ex = Example(usageObj)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()