from tkinter import messagebox
from FBA_diary.open_diary import step1_clear_diary, step2_open_fba_copy
from FBA_diary.diary_output import save_excel_as_csv_custom
import time
from config_paths import get_diary_paths


# Load all configured paths
paths = get_diary_paths()


def open_files():
    """
    Step 1: Clear diary (2.8 core file) 
    Step 2: Open FBA copy (3.1_FBA.xlsx)
    """
    try:
        print("🍉 Running: Open 2.8 & 3.1")
        step1_clear_diary()
        time.sleep(2)  # Wait for Excel operations to complete
        step2_open_fba_copy()

        messagebox.showinfo("Done", "Diary process completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Diary process failed:\n{e}")


def run_output():
    """
    Export the core 2.8 diary workbook as CSV (custom save logic).
    """
    print("🍉 Running: Diary Output")
    try:
        save_excel_as_csv_custom(paths["core_2_8"])  # ✅ fixed dict access
        print("✔ Saved as CSV completed")

        messagebox.showinfo("Done", "Diary exported ✅")
    except Exception as e:
        messagebox.showerror("Error", f"❌ Diary export failed:\n{e}")
