from customtkinter import *
from usercolor import get_image
from imageres_textconf import create_circular_image_with_round_border, basic_image_conf, basic_text_conf
from pcinfo import get_model_windows, printRefreshRate, get_drive_name, device, os_version, processor_name, total_ram_memory, gpu_name, user_name, os_release, resolut
from disk_memory import totalmem, get_disks_count
import warnings


# mute warning
warnings.filterwarnings("ignore", message="CTkLabel Warning: Given image is not CTkImage*")

# SETUP
set_appearance_mode("dark")
set_default_color_theme("green")


def overview_page(my_tab):
    tab_1 = my_tab.add("Overview")
    # WALLPAPER IMAGE
    image_path = get_image()
    photo = create_circular_image_with_round_border(image_path, size=200, border_width=8, border_color=(210, 210, 210))

    label = CTkLabel(tab_1, image=photo, text="")
    label.place(x=10, y=50)

    # TEXT
    # windows version
    basic_text_conf(tab_1, 'Windows', font_size=30, bold="bold", x=220, y=10)
    basic_text_conf(tab_1, os_release, font_size=30, x=355, y=10)
    
    ver_text = f'Version{os_version}'
    basic_text_conf(tab_1, ver_text, x=220, y=43)

    # machine model
    model_text = get_model_windows()
    basic_text_conf(tab_1, model_text, bold="bold", x=220, y=100)

    # processor name
    proc_text = f'Processor | {processor_name}'
    basic_text_conf(tab_1, proc_text, x=220, y=130)

    # memory count
    mem_text = f'Memory | {total_ram_memory} GB'
    basic_text_conf(tab_1, mem_text, x=220, y=160)

    # drive name
    disk_name = get_drive_name() 
    disk_text = f'Startup Disk | {disk_name}'
    basic_text_conf(tab_1, disk_text, x=220, y=190)

    # graphics card
    gpu_text = f'Graphics | {gpu_name}'
    basic_text_conf(tab_1, gpu_text, x=220, y=219)

    # greeting
    gtext = f'Hi, {user_name}!'
    greeting_text = CTkLabel(tab_1, text=gtext, font=("San Francisco", 14))
    greeting_text.place(x=100, y=240, anchor='center')



def displays_page(my_tab):
    tab_2 = my_tab.add("Monitors")
    
    # monitor icon
    monitor_png = "iconsimages/monitor.png"
    monitor_icon_image = basic_image_conf(monitor_png, 250, 250)
    monitor_label = CTkLabel(tab_2, text='', image=monitor_icon_image)
    monitor_label.pack(pady=5)
    
    # graphics card name
    gpu_label = CTkLabel(tab_2, text=gpu_name, font=("San Francisco", 15, 'bold'))
    gpu_label.pack(pady=6)
    
    # refreshrate + resolution
    joint_text = f'{printRefreshRate(device)[0]} @ {resolut}'
    monitor_info_text = CTkLabel(tab_2, text=joint_text, font=("San Francisco", 15))
    monitor_info_text.pack(pady=7)
   
    
    
def storage_page(my_tab):
    tab_3 = my_tab.add("Storage")
    
    # disk icon
    disk_png = "iconsimages/hard-disk.png"
    disk_icon_image = basic_image_conf(disk_png, 100, 100)
    disk_label2 = CTkLabel(tab_3, text='', image=disk_icon_image)
    disk_label2.place(x=20, y=20)
    
    # disk drive name
    disk_name = get_drive_name()
    basic_text_conf(tab_3, disk_name, x=125, y=40)
    
    # storage usage bar
    main_progress = CTkProgressBar(tab_3, orientation="horizontal", width=500, height=20)
    main_progress.set(int(totalmem()[0]) / 100)
    main_progress.place(x=125, y=70)
    
    all_mem = int(totalmem()[1] / (1024**3))
    used_mem = int(totalmem()[2] / (1024**3))
    
    # disk usage text
    disk_usage_text_fomat = f'{used_mem}/{all_mem} GB'
    # basic_text_conf(tab_3, disk_usage_text_fomat, bold='bold', x=25, y=120)
    disk_usage_text_label = CTkLabel(tab_3, text=disk_usage_text_fomat, font=("San Francisco", 15, 'bold'))
    disk_usage_text_label.place(x=60, y=120, anchor='center') 
    
    # disk sections
    main_scroll = CTkScrollableFrame(tab_3, width=500, height=150)
    main_scroll.place(x=120, y=110)
    
    disks = get_disks_count()
    for item in disks:
        label = CTkLabel(main_scroll, text=item, anchor="w", justify="left")
        label.pack(padx=10, pady=5, fill="x")
        
           

root = CTk()
root.title('GUIfetch(system info)')
root.attributes("-topmost", True)
root.after(1, root.wm_state, 'zoomed')
root.overrideredirect(True)
root.attributes("-transparentcolor", root.cget("bg"))
root.bind("<Escape>", lambda event: root.destroy())


my_tab = CTkTabview(
    root,
    width=700,
    height=400,
    corner_radius=20,
)
my_tab.pack(pady = 3)


overview_page(my_tab)
displays_page(my_tab)
storage_page(my_tab)


root.mainloop()
