import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import stepic

# This variable remembers the image we select
filepath = ""

def upload_image():
    global filepath
    # Opens a file browser to pick an image
    filepath = filedialog.askopenfilename(title="Select an Image", filetypes=[("PNG Files", "*.png"), ("BMP Files", "*.bmp")])
    if filepath:
        messagebox.showinfo("Success", f"Image selected successfully!\n\n{filepath}")

def hide_data():
    global filepath
    if not filepath:
        messagebox.showwarning("Error", "Please click '1. Select Image' first!")
        return

    # Pop-up box to ask for the secret message
    secret_msg = simpledialog.askstring("Secret Message", "Type the message you want to hide:")
    if not secret_msg:
        return

    try:
        # Open the image and hide the text inside the pixels
        img = Image.open(filepath)
        # stepic requires the message to be converted to bytes
        encoded_img = stepic.encode(img, secret_msg.encode('utf-8'))
        
        # Save the new "hacked" image
        save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Hacked Image As")
        if save_path:
            encoded_img.save(save_path, "PNG")
            messagebox.showinfo("Success 🕵️‍♂️", "Message hidden! The new image looks normal but contains your secret.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to hide data: {e}")

def extract_data():
    global filepath
    if not filepath:
        messagebox.showwarning("Error", "Please select an image first!")
        return

    try:
        # Open the image and extract the hidden data
        img = Image.open(filepath)
        decoded_msg = stepic.decode(img)
        
        # Convert bytes back to normal text
        if isinstance(decoded_msg, bytes):
            decoded_msg = decoded_msg.decode('utf-8')
            
        if decoded_msg:
            messagebox.showinfo("Secret Uncovered! 🔓", f"The hidden message is:\n\n{decoded_msg}")
        else:
            messagebox.showinfo("Clean", "No secret message found in this image.")
    except Exception as e:
        messagebox.showerror("Error", "Could not read any hidden data from this image.")

# --- Create the Main Window ---
root = tk.Tk()
root.title("Steganography Tool - Version 1.0")
root.geometry("450x350")
root.configure(bg="#2c3e50")

# --- UI Elements ---
title_label = tk.Label(root, text="Secret Image Steganography", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=20)

upload_btn = tk.Button(root, text="1. Select Image", command=upload_image, width=25, bg="#3498db", fg="white", font=("Arial", 12))
upload_btn.pack(pady=10)

hide_btn = tk.Button(root, text="2. Hide Secret Message", command=hide_data, width=25, bg="#e74c3c", fg="white", font=("Arial", 12))
hide_btn.pack(pady=10)

extract_btn = tk.Button(root, text="3. Extract Message", command=extract_data, width=25, bg="#2ecc71", fg="white", font=("Arial", 12))
extract_btn.pack(pady=10)

root.mainloop()
