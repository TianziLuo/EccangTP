import tkinter as tk
from tkinter import messagebox
from Eccang_ui import create_eccang_section
from TP_ui import create_inventory_section
import TP_tasks
from styles import btn_params, header_font, title_font

# ======= Utils Func =======
def run_safe(func, name):
    try:
        func()
        messagebox.showinfo("Success", f"{name} completed ✅")
    except Exception as e:
        messagebox.showerror("Error", f"{name} failed ❌\n{e}")

def make_step_frame(parent, text):
    frame = tk.Frame(
        parent,
        bg="#fadee3",  
        bd=2,
        relief="ridge",
        padx=2,
        pady=3
    )
    label = tk.Label(
        frame,
        text=text + " 🍉",
        font=header_font,
        fg="#143b3b",
        bg="#fadee3"
    )
    label.pack(anchor="w", pady=(0, 1))
    return frame

def add_task_buttons(frame, tasks):
    for label, func in tasks:
        tk.Button(
            frame,
            text=label,
            command=lambda f=func, l=label: run_safe(f, l),
            **btn_params
        ).pack(padx=4, pady=2)

# ======= 主窗口 =======
def create_main_window():
    window = tk.Tk()
    window.title("🍉 Subarashii Melon 🍉")
    window.geometry("880x700")
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
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

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
    create_inventory_section(right_frame)

    return window

# ======= 入口 =======
if __name__ == "__main__":
    create_main_window().mainloop()
