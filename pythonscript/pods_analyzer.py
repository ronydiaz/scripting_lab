#!/usr/bin/env python3

import json

with open('pods.json','r') as file:
    data = json.load(file)
#print(data)

all_cpu = []
all_ram = []

for pod in data:
    for container in pod["containers"]:
        # Extraemos los valores de CPU y memoria
        cpu_str = container["cpu_usage"]
        ram_str = container["memory_usage"]

        cpu_int = int(cpu_str.replace('m',''))
        ram_int = int(ram_str.replace('Mi',''))

        all_cpu.append(cpu_int)
        all_ram.append(ram_int)


total_cpu = sum(all_cpu)
total_ram = sum(all_ram)
average_cpu = total_cpu/len(all_cpu)
average_ram = total_ram/len(all_ram)

print(f"The total CPU is {total_cpu}m")
print(f"The total RAM is {total_ram}Mi")
print(f"The average CPU is {average_cpu}m")
print(f"The average RAM is {average_ram}Mi")
