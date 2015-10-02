import sys
import controller
from PySide import QtGui, QtCore

class Viewer(QtGui.QWidget):

	def __init__(self,readerObj):
		super(Viewer, self).__init__()
		
		self.readerObj = readerObj

		self.initUI()

	def initUI(self):

		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(10)

		self.titleLabel = QtGui.QLabel("usage")
		self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

		self.initData()

		refreshBtn = QtGui.QPushButton('Refresh')
		quitBtn = QtGui.QPushButton('Quit',self)

		refreshBtn.setShortcut('Ctrl+R')
		quitBtn.setShortcut('Ctrl+Q')
		refreshBtn.setToolTip('Cmd+R')
		quitBtn.setToolTip('Cmd+Q')

		quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		refreshBtn.clicked.connect(self.refreshData) 

		self.grid.addWidget(self.ramLabel, 0, 0)
		self.grid.addWidget(self.cpuLabel, 0, 1)

		self.grid.addWidget(self.ramUsage, 1, 0)
		self.grid.addWidget(self.cpuUsage, 1, 1)

		self.grid.addWidget(quitBtn,2,0)
		self.grid.addWidget(refreshBtn,2,1)

		self.setLayout(self.grid)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setStyleSheet("""
                QWidget
                {
                background-color: rgba(50,50,50, 190); 
                border-radius: 10px;
                }
                QLabel 
                {
                color: rgb(250,250,250);
                background-color: rgba(50, 50, 50, 0);
                max-height: 10em;
                }
                QPushButton 
                {
                background-color: rgba(50,50,50,0); 
                color: rgb(200,200,200);
                border: 1px solid rgba(188, 188, 188, 130);
                border-radius: 3px;
                max-width: 5em;
                padding: 6px;
                }
                QPushButton:pressed
                {
                background-color: rgba(50,50,50,0); 
                color: rgb(250,250,250);
                border: 1px solid rgba(250, 250, 250, 170);
                border-radius: 3px;
                max-width: 5em;
                padding: 6px;
                }
             """)
		self.setGeometry(50,50,350,300)
		self.setWindowTitle('Usage')
		self.show()


	def initData(self):
		self.ramUsage = QtGui.QLabel("")
		self.cpuUsage = QtGui.QLabel("")
		self.ramUsage.setAlignment(QtCore.Qt.AlignCenter)
		self.cpuUsage.setAlignment(QtCore.Qt.AlignCenter)

		self.refreshData()

		self.ramLabel = QtGui.QLabel(self.data[0][0])
		self.cpuLabel = QtGui.QLabel(self.data[1][0])
		self.ramLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.cpuLabel.setAlignment(QtCore.Qt.AlignCenter)


	def refreshData(self):
		self.data = self.readerObj.readUsage()

		self.ramUsage.setText(str(self.data[0][1]))
		self.cpuUsage.setText(str(self.data[1][1]))

	def initDataViz(self):
		pass

	def mousePressEvent(self, event):
		self.offset = event.pos()

	def mouseMoveEvent(self, event):
		x=event.globalX()
		y=event.globalY()
		x_w = self.offset.x()
		y_w = self.offset.y()
		self.move(x-x_w, y-y_w)
		



def main(readerObj):

	app = QtGui.QApplication(sys.argv)
	win = Viewer(readerObj)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main(usageObj)