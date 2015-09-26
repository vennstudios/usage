import psutil
import model
import view #will probably be removed

def readUsage():
	"""
	Uses psutil to get CPU and RAM usage percentages
	"""
	cpuUsage = ('CPU', psutil.cpu_percent(interval=0.1, percpu=False))
	memory = psutil.virtual_memory()
	ramUsage = ('RAM', memory.percent)

	return [cpuUsage, ramUsage]

def updateModel(modelObject):
	"""
	Uses readUsage to update the current model.data
	"""
	updateList = readUsage()
	modelObject.data = {}
	for item in updateList:
		modelObject.data[item[0]] = item[1]
		


def renderView(modelObject):
	print modelObject.data


if __name__ == "__main__":
	aModel = model.Model()
	updateModel(aModel)
	renderView(aModel)