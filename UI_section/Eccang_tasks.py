from tkinter import messagebox


import time
from Eccang.unzip import unzip
from Eccang.copy_download import copy_download


def step2_to_4_all():
    print("🍉 Running: Step 2 ➜ 4 (Unzip ➜ Convert ➜ Rename)")
    try:
        unzip()
        print("✔ Step 2 completed")
        
        messagebox.showinfo("Done", "All Steps (2 ➜ 4) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 2-4 error:\n{e}")

def step5_copy():
    print("🍉 Running: Copy downloaded files")
    try:
        copy_download()
        messagebox.showinfo("Done", "Step 5 (Copy downloaded files) completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"Step 5 error:\n{e}")
