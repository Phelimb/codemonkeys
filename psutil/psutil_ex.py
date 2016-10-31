import psutil
cpus = psutil.cpu_percent(interval=1, percpu=True)

for cpu in cpus:
    print(cpu)
