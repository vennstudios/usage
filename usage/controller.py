import psutil
import view

class Usage(object):

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

	def updateViewData(self):
		"""
		Uses readUsage to update the current model.data. Returns the same values as readUsage.
		"""
		updateList = self.readUsage()
		for item in updateList:
			pass



def main():
	usageObj = Usage()
	view.main(usageObj)

if __name__ == '__main__':
	main()
