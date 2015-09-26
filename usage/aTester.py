import psutil

cpuUsage = psutil.cpu_percent(interval=0.1, percpu=False)
memory = psutil.virtual_memory()

ramUsage = memory.percent

print cpuUsage
print ramUsage 