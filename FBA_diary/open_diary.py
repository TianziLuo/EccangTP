import os
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import win32com.client as win32
from config_paths import get_diary_paths



# Load paths from config file
paths = get_diary_paths()


def get_excel_app():
    """
    Get or create an Excel application instance.
    - If Excel is already running, reuse the existing instance.
    - Otherwise, start a new one.
    """
    try:
        excel = win32.GetActiveObject("Excel.Application")
    except Exception:
        excel = win32.Dispatch("Excel.Application")
    excel.Visible = True
    return excel


def step1_clear_diary():
    """
    Step 1: Open the core workbook and clear the contents of a given range.
    Target: Worksheet '读取原始记录', range F2:CW6000
    """
    try:
        excel = get_excel_app()
        workbook = excel.Workbooks.Open(str(paths["core_2_8"]))
        sheet = workbook.Sheets("读取原始记录")
        sheet.Range("F2", "CW6000").ClearContents()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open or clear workbook: {e}")


def step2_open_fba_copy():
    """
    Step 2: Let user choose one of the latest backup folders (up to 5).
    Open the FBA workbook (3.1_FBA.xlsx), activate 'FBA_易仓' sheet,
    select cell J2, then apply optional key actions.
    """
    base_path = paths["backup_folder"]

    # Collect folders sorted by last modified time
    folders = [(f, f.stat().st_mtime) for f in base_path.iterdir() if f.is_dir()]
    folders.sort(key=lambda x: x[1], reverse=True)
    top_folders = folders[:5]  # Keep the latest 5

    # Create popup window
    root = tk.Tk()
    root.title("Select Folder to Open FBA_易仓")
    root.geometry("400x350")

    label = tk.Label(root, text="Please select a folder:", font=("Arial", 12))
    label.pack(pady=10)

    def open_excel_with_keys(folder: Path):
        """
        Inner function to open Excel workbook inside the selected folder.
        Then, navigate to sheet 'FBA_易仓' and select cell J2.
        """
        file_path = folder / "公用核心" / "3.1_FBA.xlsx"
        if not file_path.exists():
            messagebox.showerror("Error", f"File does not exist: {file_path}")
            return
        try:
            excel = get_excel_app()
            workbook = excel.Workbooks.Open(str(file_path))
            sheet = workbook.Sheets("FBA_易仓")
            sheet.Activate()
            sheet.Range("J2").Select()

            # Use Excel API instead of SendKeys whenever possible
            sheet.Cells.Select()  # Equivalent to Ctrl+A (select all cells)

            # If Alt+5 is needed for add-ins or Excel features, keep SendKeys
            shell = win32.Dispatch("WScript.Shell")
            shell.AppActivate(excel.Caption)
            shell.SendKeys("%5")  # Alt+5

        except Exception as e:
            messagebox.showerror("Error", f"Failed to open workbook: {e}")

    # Create buttons for top folders
    for i, (folder, mtime) in enumerate(top_folders, 1):
        btn = tk.Button(
            root,
            text=f"{i}. {folder.name}",
            width=40,
            command=lambda f=folder: open_excel_with_keys(f),
        )
        btn.pack(pady=5)

    root.mainloop()
'''
if __name__ == "__main__":
    step1_clear_diary()
    time.sleep(2)
    step2_open_fba_copy()
'''