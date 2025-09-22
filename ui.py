import tkinter as tk
from tkinter import messagebox
from UI_section.Eccang_ui import create_eccang_section
from UI_section.TP_ui import create_tp_section
from UI_section.refresh_ui import create_refresh_section
from UI_section.Diary_ui import create_diary_section
from styles import title_font

# ======= Utils Func =======
def run_safe(func, name):
    try:
        func()
        messagebox.showinfo("Success", f"{name} completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"{name} failed ❌\n{e}")

# ======= Main Window =======
def create_main_window():
    window = tk.Tk()
    window.title("🍉 Subarashii Melon 🍉")
    window.geometry("1250x720")  # 稍微加高，给 Diary 留空间
    window.configure(bg="#EDFCA6")

    # ======= Title =======
    tk.Label(
        window,
        text="🍉 EccangTP Watermelon 🍉",
        font=title_font,
        fg="#072020",
        bg="#EDFCA6"
    ).pack(pady=6)

    # ======= Main Container =======
    main_frame = tk.Frame(window, bg="#EDFCA6")
    main_frame.pack(fill="both", expand=True, padx=23, pady=10)

    # 3-column layout
    main_frame.columnconfigure(0, weight=1)  # Left column: Eccang
    main_frame.columnconfigure(1, weight=1)  # Middle column: TP
    main_frame.columnconfigure(2, weight=1)  # Right column: Refresh
    main_frame.rowconfigure(0, weight=1)     # Top row
    main_frame.rowconfigure(1, weight=1)     # Diary row

    # ======= Left column (Eccang) =======
    left_frame = tk.Frame(main_frame, bg="#EDFCA6")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
    create_eccang_section(left_frame)

    # ======= Middle column (TP) =======
    middle_frame = tk.Frame(main_frame, bg="#EDFCA6")
    middle_frame.grid(row=0, column=1, sticky="nsew", padx=5)
    create_tp_section(middle_frame)

    # ======= Right column (Refresh) =======
    right_frame = tk.Frame(main_frame, bg="#EDFCA6")
    right_frame.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=(5, 0))
    create_refresh_section(right_frame)

    # ======= Diary Section (col0 + col1, row=1) =======
    diary_frame = tk.Frame(main_frame, bg="#EDFCA6")
    diary_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=(5, 0))
    create_diary_section(diary_frame)

    return window

'''
if __name__ == "__main__":
    create_main_window().mainloop()
'''
