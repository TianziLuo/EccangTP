from tkinter import messagebox
from purchase.func import (
    clean_folder,
    copy_purchase,
    open_excel,
    save_cvs,
    copy_cvs,
)
import time
from Eccang.unzip import unzip
from Eccang.xls2csv import xls2csv
from Eccang.rename import rename
from Eccang.copy_download import copy_download

def run_purchase_files():
    print("🍉 Running: Update purchase folder")
    try:
        clean_folder()
        print("✔ Clean Folder completed")
        time.sleep(2)

        copy_purchase()
        print("✔ Copy Files completed")
        time.sleep(2)

        open_excel()
        print("✔ Open Excel completed")

        messagebox.showinfo("Done", "Folder Updated ✅")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Folder Updated failed:\n{e}")


def run_save_copy_cvs():
    print("🍉 Running: Save CSV")
    try:
        save_cvs()
        print("✔ Save As completed")
        time.sleep(1)

        copy_cvs()
        print("✔ Copy CSV completed")
        
        messagebox.showinfo("Done", "CSV saved and copied✅")
    except Exception as e:
        messagebox.showerror("Error", f"Process CSV failed:\n{e}")

def step2_to_4_all():
    print("🍉 Running: Step 2 ➜ 4 (Unzip ➜ Convert ➜ Rename)")
    try:
        unzip()
        print("✔ Step 2 completed")
        
        xls2csv()
        print("✔ Step 3 completed")
        
        rename()
        print("✔ Step 4 completed")
        
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
