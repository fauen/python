import psutil
import platform

def _cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    cpu_count = psutil.cpu_count()
    return cpu_usage, cpu_freq, cpu_count

def _memory_info():
    mem_total = psutil.virtual_memory()
    return mem_total

def _disk_info():
    if platform.system() == "Windows":
        disk_usage = psutil.disk_usage('C:\\')
    else:
        disk_usage = psutil.disk_usage('/')
    return disk_usage

def main():
    print(f"CPU information:")
    print(f"CPU usage: {_cpu_info()[0]}%")
    print(f"CPU count: {_cpu_info()[2]}")
    print("\nMemory information:")
    print(f"MEM total: {int(_memory_info()[0] / 1024 ** 2)} GB")
    print(f"MEM usage: {_memory_info()[2]}%")
    print(f"\nDisk information:")
    print(f"Disk total: {int(_disk_info()[0] / 1000 ** 3)} GB")
    print(f"Disk usage: {int(_disk_info()[3] * 10)}%")

if __name__ == "__main__":
    main()