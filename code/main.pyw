from customtkinter import *
from PIL import Image, ImageTk
from usercolor import get_windows_theme_color, get_image, get_windows_theme
from imageres import create_circular_image_with_round_border
from pcinfo import *
import warnings

# mute warning
warnings.filterwarnings("ignore", message="CTkLabel Warning: Given image is not CTkImage*")

# SETUP
set_appearance_mode("dark")
set_default_color_theme("green")


root = CTk()
root.attributes("-topmost", True)
height = 500
width = 800
x = (root.winfo_screenwidth()//2) - (width//2)
y = (root.winfo_screenheight()//2) - (height//2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.overrideredirect(True)
root.attributes("-transparentcolor", root.cget("bg"))

root.bind("<Escape>", lambda event: root.destroy())


my_tab = CTkTabview(
    root,
    width=700,
    height=400,
    corner_radius=20,
    state="disabled"
)
my_tab.pack(pady = 3)
tab_1 = my_tab.add("Overview")

# WALLPAPER IMAGE 
image_path = get_image()
photo = create_circular_image_with_round_border(image_path, size=200, border_width=8, border_color=(210, 210, 210))

label = CTkLabel(tab_1, image=photo, text="")
label.place(x=10, y=50)

# TEXT

# windows version
win_label = CTkLabel(tab_1, text='Windows', font=("San Francisco", 30, "bold"))
win_number = CTkLabel(tab_1, text=os_version[:2], font=("San Francisco", 30))
win_label.place(x=220, y=10)
win_number.place(x=355, y=10)

ver_text = f'Version{os_version}'
ver_label = CTkLabel(tab_1, text=ver_text, font=("San Francisco", 15))
ver_label.place(x=220, y=43)

# machine model
model_text = get_model_windows()
model_label = CTkLabel(tab_1, text=model_text, font=("San Francisco", 15, "bold"))
model_label.place(x=220, y=100)

# processor name
proc_text = f'Processor | {processor_name}'
proc_label = CTkLabel(tab_1, text=proc_text, font=("San Francisco", 15))
proc_label.place(x=220, y=130)

# memory count
mem_text = f'Memory | {total_memory} GB'
mem_label = CTkLabel(tab_1, text=mem_text, font=("San Francisco", 15))
mem_label.place(x=220, y=160)

# drive name
disc_text = f'Startup Disk | {cleaned_output}'
disc_label = CTkLabel(tab_1, text=disc_text, font=("San Francisco", 15))
disc_label.place(x=220, y=193)

# graphics card
gpu_text = f'Graphics | {gpu_name}'
gpu_label = CTkLabel(tab_1, text=gpu_text, font=("San Francisco", 15))
gpu_label.place(x=220, y=219)

# greeting
gtext = f'Hi, {user_name}!'
greeting_text = CTkLabel(tab_1, text=gtext, font=("San Francisco", 14))
greeting_text.place(x=65, y=240)


root.mainloop()
