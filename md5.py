import hashlib
import tkinter as tk
from tkinter import filedialog

def calculate_md5(file_path):
    with open(file_path, "rb") as f:
        file_content = f.read()
        md5_hash = hashlib.md5(file_content).hexdigest()
    return md5_hash

def encrypt_to_md5(text):
    md5_hash = hashlib.md5(text.encode()).hexdigest()
    return md5_hash

def decrypt_from_md5(md5_hash):
    return "Decryption not possible. MD5 is a one-way hash function."

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        md5_hash = calculate_md5(file_path)
        result_label.config(text="MD5 hash: " + md5_hash)

def encrypt_text():
    text = input_text.get("1.0", "end-1c")
    if text:
        md5_hash = encrypt_to_md5(text)
        result_label.config(text="MD5 hash: " + md5_hash)

def decrypt_md5():
    md5_hash = input_md5.get()
    if md5_hash:
        result = decrypt_from_md5(md5_hash)
        result_label.config(text="Decrypted text: " + result)
      
window = tk.Tk()
window.title("MD5 Tool")

input_text = tk.Text(window, height=5, width=50)
input_text.pack()

encrypt_button = tk.Button(window, text="Encrypt Text", command=encrypt_text)
encrypt_button.pack()

input_md5 = tk.Entry(window)
input_md5.pack()

decrypt_button = tk.Button(window, text="Decrypt MD5", command=decrypt_md5)
decrypt_button.pack()

browse_button = tk.Button(window, text="Browse File", command=browse_file)
browse_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
