import psutil
import view

class Reader(object):

	def __init__(self):
		self.data=self.readUsage()

	def readUsage(self):
		"""
		Uses psutil to get CPU and RAM usage as list of tuples ('component', percentage).
		"""
		cpuUsage = ('CPU', psutil.cpu_percent(interval=0.1, percpu=False))
		memory = psutil.virtual_memory()
		ramUsage = ('RAM', memory.percent)

		return [ramUsage, cpuUsage]

def main():
	readerObj = Reader()
	view.main(readerObj)

if __name__ == '__main__':
	main()
