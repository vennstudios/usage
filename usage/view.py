import sys
import controller
from PySide import QtGui, QtCore

class Viewer(QtGui.QWidget):

	def __init__(self,readerObj):	
		super(Viewer, self).__init__()
		
		self.readerObj = readerObj

		self.initUI()

	def initUI(self):

		titleLabel = QtGui.QLabel("usage",self) 
		titleLabel.setAlignment(QtCore.Qt.AlignCenter) 
		titleLabel.move(155,8)

		self.initData()

		self.ramLabel.move(76, 60)
		self.cpuLabel.move(236,60)	

		refreshBtn = QtGui.QPushButton('Refresh',self)
		quitBtn = QtGui.QPushButton('Quit',self)
		refreshBtn.setShortcut('Ctrl+R')
		quitBtn.setShortcut('Ctrl+Q')
		refreshBtn.setToolTip('Cmd+R')
		quitBtn.setToolTip('Cmd+Q')
		refreshBtn.move(190, 250)
		quitBtn.move(80,250)

		quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
		refreshBtn.clicked.connect(self.update) 


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
                min-width: 5em;
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

		self.refreshData()

		self.ramLabel = QtGui.QLabel(self.data[0][0], self)
		self.cpuLabel = QtGui.QLabel(self.data[1][0], self)


	def refreshData(self):
		self.data = self.readerObj.readUsage()

	def paintEvent(self,event):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.refreshData()
		self.draw(event,qp,40,100, self.data[0][1])
		self.draw(event,qp,195,100, self.data[1][1])
		qp.end()

	def draw(self, event, qp, x, y, percentage):
		w=100
		h=100
		startA=0
		spanA=percentage
		qp.setRenderHint(QtGui.QPainter.Antialiasing)

		qp.setPen(QtCore.Qt.red)
		self.drawPiePiece(event, x, y, w, h, startA, spanA, qp)

		spanA=-(360-spanA)
		qp.setPen(QtCore.Qt.green)
		self.drawPiePiece(event, x, y, w, h, startA, spanA, qp)

	def drawPiePiece(self, event, x, y, w, h, startA, spanA, qp):
		spanA=spanA*16
		qp.drawPie(x, y, w, h, startA, spanA)

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