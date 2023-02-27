import time
import psutil
import win32api
import json
import os
from datetime import datetime
import socket
import matplotlib.pyplot as plt

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

path = f'C:/Users/shiha/OneDrive/Desktop/maria_apu_project/pc_info/{hostname}_{ip_address}/'
os.mkdir(path)

x=0

while True:
	time1 = datetime.now().strftime("%H:%M:%S")
	date = datetime.now().strftime("%Y-%m-%d")
	file_obj = open(f'{path}/pc_data{date}{x}.json','w')
	array = []
	array_cpu = []
	array_mem = []
	array_disk = []
	a=0
	

	def alert(str,element):
		win32api.MessageBox(0, f'\r {str}: {element}%', 'There is a WARNING !!!')
		
	def display(cpu, mem, disk):
		if(cpu>90):	
			alert('CPU',cpu)
		elif(mem>90):	
			alert('MEMORY',mem)
		elif(disk>90):	
			alert('DISK',disk)


		dict = {
			'CPU':cpu,
			'MEMORY':mem,
			'DISK':disk,
			'TIME':time1

		}

		array.append(dict)
		array_cpu.append(cpu)
		array_mem.append(mem)
		array_disk.append(disk)

		print(f'\r CPU: {cpu}% | Memory: {mem}% | DISK: {disk}%')
		
	
	

	while a<6:
	
		display(psutil.cpu_percent(),psutil.virtual_memory().percent,psutil.disk_usage('/').percent) 
		time.sleep(0.5)
		a+=1
	

	max_cpu = max(array_cpu)
	max_mem = max(array_mem)
	last_disk = array_disk[-1]
	
	avg_cpu = sum(array_cpu)/len(array_cpu)
	avg_mem = sum(array_mem)/len(array_mem)

	print(f'\r MAX CPU: {max_cpu}% | MEMORY: {max_mem}%')

	json_obj = json.dumps(array, indent=4)
	file_obj.write(json_obj)
	file_obj.close()


	x_axis = ['Max CPU Usage', 'Max Memory Usage', 'Used Space']
	y_axis = [max_cpu, max_mem, last_disk]
	colors = ['purple', 'teal', 'orange']


	# Create a bar chart
	plt.bar(x_axis, y_axis,color=colors)

	# Create a line plot

	# Set x and y axis limits
	plt.xlim(-1, 3)
	plt.ylim(0, 100)


	# Set chart title and axis labels
	plt.title(f'Utility Used on {date}')
	plt.xlabel('Utilities', fontsize=14)
	plt.ylabel('Max usage', fontsize=14)

	plt.xticks(rotation = 10)

	# Save chart as PNG image
	plt.savefig(f'{path}my_chart{x}.png')

	x+=1
