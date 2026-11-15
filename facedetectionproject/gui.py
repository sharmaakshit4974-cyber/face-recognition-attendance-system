import tkinter as tk
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def register():
    subprocess.run(["python", "register.py"], cwd=BASE_DIR)

def recognize():
    subprocess.run(["python", "main.py"], cwd=BASE_DIR)

root = tk.Tk()
root.title("Face Recognition System")
root.geometry("400x300")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Face Recognition System",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=20)

btn1 = tk.Button(root, text="Register Face",
                 command=register,
                 width=20, height=2,
                 bg="#4CAF50", fg="white")
btn1.pack(pady=10)

btn2 = tk.Button(root, text="Start Recognition",
                 command=recognize,
                 width=20, height=2,
                 bg="#2196F3", fg="white")
btn2.pack(pady=10)

btn3 = tk.Button(root, text="Exit",
                 command=root.quit,
                 width=20, height=2,
                 bg="#f44336", fg="white")
btn3.pack(pady=10)

root.mainloop()