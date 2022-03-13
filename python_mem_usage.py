import os
import psutil
import time
from datetime import datetime

while True:
	now = datetime.now()
	cpu = "The CPU usage at {0} is: {1}"
	mem = "The memory usage at {0} is: {1}"
	print(cpu.format(now,psutil.cpu_percent(1)))
	print(mem.format(now,psutil.virtual_memory()[2]))
	#print('The CPU usage at %s is:', datetime.now(), psutil.cpu_percent(1))
	time.sleep(28)
