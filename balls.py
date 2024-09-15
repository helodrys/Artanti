import tkinter
import customtkinter as ctk
from PIL import Image

root_tk = tkinter.Tk()
root_tk.geometry("375x667")
root_tk.title("OCD")

welcome_image = Image.open("che_thief.jpg")
img_ctk = ctk.CTkImage(welcome_image, size=(375, 300))

image_label = ctk.CTkLabel(root_tk, image=img_ctk, text="")
image_label.pack(pady=20)

root_tk.mainloop()