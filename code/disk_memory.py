import psutil


def totalmem():
    total_space = 0
    used_space = 0

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            total_space += usage.total
            used_space += usage.used
        except (PermissionError, FileNotFoundError):
            # Ігноруємо диски, до яких немає доступу
            continue

    if total_space > 0:
        percent_used = (used_space / total_space) * 100
        return round(percent_used, 2), total_space, used_space
    else:
        print('access denied')
        return 0, 0, 0


def get_disks_count():
    disk_info_list = []
    partitions = psutil.disk_partitions(all=False)
    
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            info = (
                f"Drive: {partition.device}\n"
                f"  File system type: {partition.fstype}\n"
                f"  Total Size: {usage.total / (1024**3):.2f} GB\n"
            )
            disk_info_list.append(info)
        except (PermissionError, FileNotFoundError):
            continue

    return disk_info_list
