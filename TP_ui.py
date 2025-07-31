import tkinter as tk
import TP_tasks as TP_tasks
from styles import btn_params, header_font

def make_step_frame(parent, text, bg_color):
    frame = tk.Frame(
        parent,
        bg=bg_color,
        bd=2,
        relief="ridge",
        padx=6,
        pady=6
    )
    label = tk.Label(
        frame,
        text=text,
        font=header_font,
        fg="#3b3b3b",
        bg=bg_color
    )
    label.pack(anchor="w", pady=(0, 4))
    return frame

def add_task_buttons(frame, tasks):
    for label, func in tasks:
        tk.Button(
            frame,
            text=label,
            command=func,
            **btn_params
        ).pack(padx=35, pady=2)

def create_inventory_section(parent):
    inv_container = tk.LabelFrame(
        parent,
        text="🍋 TP",
        font=header_font,
        fg="#072020",
        bg="#fadee3",
        padx=10,
        pady=10,
        bd=3,
        relief="groove",
        labelanchor="n"
    )
    inv_container.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

    # 让容器内部自动扩展
    inv_container.columnconfigure(0, weight=1)

    frame4 = make_step_frame(inv_container, "🍋 SKU Mapping", "#dbfdfd")
    frame4.grid(row=0, column=0, sticky="ew", pady=5)
    add_task_buttons(frame4, [
        ("Open 1.1", TP_tasks.step_1_1),
        ("Generate & Copy SKU Mapping", TP_tasks.step_1_2)
    ])

    frame5 = make_step_frame(inv_container, "🍋 TP Upload", "#dbfdfd")
    frame5.grid(row=1, column=0, sticky="ew", pady=5)
    add_task_buttons(frame5, [
        ("Open 2.1", TP_tasks.step_2_1),
        ("Generate & Upload & Copy TP.csv", TP_tasks.step_2_2),
        ("Copy SKUINV", TP_tasks.step_2_4),
    ])

    frame6 = make_step_frame(inv_container, "🍋 DXM", "#dbfdfd")
    frame6.grid(row=2, column=0, sticky="ew", pady=5)
    add_task_buttons(frame6, [
        ("Rename & Open", TP_tasks.step_3_1),
        ("Generate & Copy Inventory Update", TP_tasks.step_3_3),
    ])

    return inv_container

