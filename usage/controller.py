import psutil
import view


def readUsage():
	"""
	Uses psutil to get CPU and RAM usage as list of tuples ('component', percentage).
	"""
	cpuUsage = ('CPU', psutil.cpu_percent(interval=0.1, percpu=False))
	memory = psutil.virtual_memory()
	ramUsage = ('RAM', memory.percent)

	return [ramUsage, cpuUsage]

def main():
	view.main()

if __name__ == '__main__':
	main()
