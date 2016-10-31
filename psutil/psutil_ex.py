import psutil
cpu = psutil.cpu_percent(interval=5, percpu=True)
print(cpu)
