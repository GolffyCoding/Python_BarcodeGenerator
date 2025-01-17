import tkinter as tk
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter
from PIL import Image as PILImage, ImageTk


def generate_barcode():
    barcode_number = entry.get()
    if len(barcode_number) != 13:
        messagebox.showerror("Invalid Input", "EAN-13 barcode must be 13 digits long")
        return

    
    barcode_format = barcode.get_barcode_class('ean13')
    barcode_image = barcode_format(barcode_number, writer=ImageWriter())
    
    
    barcode_filename = f'barcode_{barcode_number}'
    barcode_image.save(barcode_filename)
    
    
    pil_image = PILImage.open(f'{barcode_filename}.png')
    photo = ImageTk.PhotoImage(pil_image)
    
    
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo  

    
    save_button.config(state=tk.NORMAL)  


def save_barcode():
    barcode_number = entry.get()
    barcode_filename = f'barcode_{barcode_number}.png'
    messagebox.showinfo("Saved", f"Barcode image saved as {barcode_filename}")
    

root = tk.Tk()
root.title("Barcode Generator")


label = tk.Label(root, text="Enter Barcode Number (EAN-13):\nEAN-13 barcode must be 13 digits long")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Barcode", command=generate_barcode)
generate_button.pack(pady=5)


canvas = tk.Canvas(root, width=600, height=300)
canvas.pack(pady=2, padx=160)


save_button = tk.Button(root, text="Save Barcode", state=tk.DISABLED, command=save_barcode)
save_button.pack(pady=5)


root.mainloop()
