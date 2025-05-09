import winreg
import ctypes
import shutil
import os


# def get_windows_theme_color():
#     try:
#         # Відкриваємо розділ реєстру
#         with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\DWM") as key:
#             # Зчитуємо значення AccentColor
#             accent_color, _ = winreg.QueryValueEx(key, "AccentColor")
            
#             # Виділяємо кольорові компоненти (формат у реєстрі: 0xAABBGGRR)
#             blue = (accent_color >> 16) & 0xFF
#             green = (accent_color >> 8) & 0xFF
#             red = accent_color & 0xFF
            
#             # Конвертуємо у формат HTML-кольору
#             html_color = f"#{red:02X}{green:02X}{blue:02X}"
            
#             return html_color
#     except FileNotFoundError:
#         return "blue"
    
    

def get_image():
    # Отримуємо поточний шлях до шпалер
    spi_get_desktop_wallpaper = 0x73
    buffer_size = 260
    wallpaper_path = ctypes.create_unicode_buffer(buffer_size)
    ctypes.windll.user32.SystemParametersInfoW(spi_get_desktop_wallpaper, buffer_size, wallpaper_path, 0)

    # Шлях до поточних шпалер
    current_wallpaper = wallpaper_path.value

    # Директорія, куди будемо копіювати
    destination_folder = "/usercache"
    os.makedirs(destination_folder, exist_ok=True)

    # Формуємо шлях для збереження
    wallpaper_filename = os.path.basename(current_wallpaper)
    new_wallpaper_path = os.path.join(destination_folder, wallpaper_filename)

    shutil.copy2(current_wallpaper, new_wallpaper_path)

    # print(f"Шпалери збережено в: {new_wallpaper_path}")
    return new_wallpaper_path


# def get_windows_theme():
#     try:
#         # Відкриваємо розділ реєстру
#         with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize") as key:
#             # Зчитуємо значення AppsUseLightTheme
#             theme, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            
#             # Перевіряємо, яке значення отримали
#             return "sys_light" if theme == 1 else "sys_dark"
#     except FileNotFoundError:
#         return "sys_light"

