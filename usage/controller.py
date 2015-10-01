import psutil
import model
import view

class Usage(object):

	def __init__(self):
		self.aModel=model.Model()
		self.updateModel()

	def readUsage(self):
		"""
		Uses psutil to get CPU and RAM usage as list of tuples ('component', percentage).
		"""
		cpuUsage = ('CPU', psutil.cpu_percent(interval=0.1, percpu=False))
		memory = psutil.virtual_memory()
		ramUsage = ('RAM', memory.percent)

		return [cpuUsage, ramUsage]

	def updateModel(self):
		"""
		Uses readUsage to update the current model.data. Returns the same values as readUsage.
		"""
		updateList = self.readUsage()
		self.aModel.data = {}
		for item in updateList:
			self.aModel.data[item[0]] = item[1]

		return updateList
			


def main():
	usageObj = Usage()
	view.main(usageObj)

if __name__ == '__main__':
	main()
