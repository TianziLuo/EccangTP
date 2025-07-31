import tkinter as tk
from Eccang_tasks import (
    run_purchase_files,
    run_save_copy_cvs,
    step2_to_4_all,
    step5_copy,
)
from styles import btn_params, header_font

def make_step_frame(parent, text, bg_color):
    frame = tk.Frame(
        parent,
        bg=bg_color,
        bd=2,
        relief="ridge",
        padx=2,
        pady=6
    )
    label = tk.Label(
        frame,
        text=text,
        font=header_font,
        fg="#143b3b",
        bg=bg_color
    )
    label.pack(anchor="w", pady=(0, 1))
    return frame

def add_task_buttons(frame, tasks):
    for label, func in tasks:
        tk.Button(
            frame,
            text=label,
            command=func,
            **btn_params
        ).pack(padx=35, pady=5)

def create_eccang_section(parent):
    eccang_container = tk.LabelFrame(
        parent,
        text="🍉 Eccang",
        font=header_font,
        fg="#072020",
        bg="#dbfdfd",
        padx=10,
        pady=10,
        bd=3,
        relief="groove",
        labelanchor="n"
    )
    eccang_container.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

    # 让容器内部自动扩展
    eccang_container.columnconfigure(0, weight=1)

    frame1 = make_step_frame(eccang_container, "🍉 Step 1: Purchase Process", "#fadee3")
    frame1.grid(row=0, column=0, sticky="ew", pady=5)
    add_task_buttons(frame1, [
        ("Update Purchase Folder", run_purchase_files),
        ("Save & Copy CSV", run_save_copy_cvs),
    ])

    frame2 = make_step_frame(eccang_container, "🍉 Step 2 - 4: Unzip ➜ Convert ➜ Rename", "#fadee3")
    frame2.grid(row=1, column=0, sticky="ew", pady=5)
    add_task_buttons(frame2, [
        ("Unzip, Convert, Rename", step2_to_4_all),
    ])

    frame3 = make_step_frame(eccang_container, "🍉 Step 5: Copy Downloads Files", "#fadee3")
    frame3.grid(row=2, column=0, sticky="ew", pady=5)
    add_task_buttons(frame3, [
        ("Copy Downloaded Files", step5_copy),
    ])

    return eccang_container
