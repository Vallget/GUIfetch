import platform
import cpuinfo
import getpass
import psutil
import subprocess
import win32api


def is_laptop():
    global laptop
    laptop = False
    battery = psutil.sensors_battery()
    if battery is not None:
        laptop = True
    else:
        laptop = False
    return laptop


def get_model_windows():
    lap = is_laptop()
    if lap:
            output = subprocess.check_output("wmic computersystem get model")
            return output.decode().splitlines()[2].strip()
    else:
        return "desktop PC"


def get_system_info():
    uname = platform.uname()
    print("Система:", uname.system)
    print("Виробник:", uname.node)
    print("Реліз:", uname.release)
    print("Версія:", uname.version)
    print("Машина:", uname.machine)
    print("Процесор:", uname.processor)


def printRefreshRate(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    # Вивести тільки частоту оновлення екрану
    return [str("%s Hz" % getattr(settings, 'DisplayFrequency')), str(device.DeviceString)]


os_version = platform.version()
user_name = getpass.getuser()
os_name = platform.system()
processor_name = cpuinfo.get_cpu_info()['brand_raw']
device = win32api.EnumDisplayDevices()
gpu_name = printRefreshRate(device)[1]

# memory amount
memory = psutil.virtual_memory()
total_memory = round(memory.total / (1024 ** 3))

# use the WMIC command to get information about the drive
command = "wmic diskdrive get model"
result = subprocess.run(command, capture_output=True, text=True)
output_lines = result.stdout.splitlines()[2:]
cleaned_output = "\n".join(output_lines)



