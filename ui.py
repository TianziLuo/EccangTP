import tkinter as tk
from tkinter import messagebox
from Eccang_ui import create_eccang_section
from TP_ui import create_tp_section
import TP_tasks
from styles import title_font

# ======= Utils Func =======
def run_safe(func, name):
    try:
        func()
        messagebox.showinfo("Success", f"{name} completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"{name} failed ❌\n{e}")


# ======= 主窗口 =======
def create_main_window():
    window = tk.Tk()
    window.title("🍉 Subarashii Melon 🍉")
    window.geometry("843x605")
    window.configure(bg="#EDFCA6")

    # ======= 标题 =======
    tk.Label(
        window,
        text="🍉 EccangTP Watermelon 🍉",
        font=title_font,
        fg="#072020",
        bg="#EDFCA6"
    ).pack(pady=6)

    # ======= 主容器，使用 grid 布局划分左右两块 =======
    main_frame = tk.Frame(window, bg="#EDFCA6")
    main_frame.pack(fill="both", expand=True, padx=23, pady=10)

    main_frame.columnconfigure(0, weight=1)  # 左列权重1
    main_frame.columnconfigure(1, weight=1)  # 右列权重1
    main_frame.rowconfigure(0, weight=1)

    # ======= 左侧区域 (Eccang) =======
    left_frame = tk.Frame(main_frame, bg="#EDFCA6")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

    # ======= 右侧区域 (Inventory) =======
    right_frame = tk.Frame(main_frame, bg="#EDFCA6")
    right_frame.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

    # ======= 内容调用 =======
    create_eccang_section(left_frame)
    create_tp_section(right_frame)

    return window

''''
if __name__ == "__main__":
    create_main_window().mainloop()
'''