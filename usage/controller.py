import psutil
import model

def readUsage():
	cpuUsage = psutil.cpu_percent(interval=0.1, percpu=False)
	memory = psutil.virtual_memory()
	ramUsage = memory.percent

	return [cpuUsage, ramUsage]

def updateModelObject(modelObject):
	updateList = readUsage()
	print  ##
	for item in updateList:
		pass """add code here that loops through the updateList adding 
		its values to the corresponding items in aModel.data"""

def updateView():
	pass


if __name__ == "__main__":
	aModel = model.Model()
	updateModelObject(aModel)
	print aModel.data ##