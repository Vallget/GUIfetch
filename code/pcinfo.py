import platform
import cpuinfo
import getpass
import psutil
import subprocess
import win32api
from screeninfo import get_monitors


def is_laptop():
    laptop = False
    battery = psutil.sensors_battery()
    if battery is not None:
        laptop = True
    return laptop


def get_model_windows():
    lap = is_laptop()
    if lap:
            output = subprocess.check_output("wmic computersystem get model")
            return output.decode().splitlines()[2].strip()
    else:
        return "desktop PC"


# def get_system_info():
#     uname = platform.uname()
#     print("Виробник:", uname.node)
#     print("Машина:", uname.machine)



def printRefreshRate(device):
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    return [str("%s Hz" % getattr(settings, 'DisplayFrequency')), str(device.DeviceString)]


def get_drive_name():
    # use the WMIC command to get information about the drive
    command = "wmic diskdrive get model"
    result = subprocess.run(command, capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[2:]
    filtered = [line for line in output_lines if "USB" not in line]
    return "".join(filtered)


os_version = platform.version()
os_release = platform.release()
user_name = getpass.getuser()
processor_name = cpuinfo.get_cpu_info()['brand_raw']
device = win32api.EnumDisplayDevices()
gpu_name = printRefreshRate(device)[1]

# memory amount
ram_memory = psutil.virtual_memory()
total_ram_memory = round(ram_memory.total / (1024 ** 3))


monitor = get_monitors()[0]  # Get the first monitor
resolut = f"{monitor.width}x{monitor.height}"