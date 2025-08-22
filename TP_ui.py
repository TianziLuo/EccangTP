import tkinter as tk
import TP_tasks as TP_tasks
from styles import header_font
from ui_utils import make_step_frame, add_task_buttons


def create_tp_section(parent):
    tp_container = tk.LabelFrame(
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
    tp_container.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
    tp_container.columnconfigure(0, weight=1)

    # SKU Mapping
    frame1 = make_step_frame(tp_container, "🍋 SKU Mapping", "#dbfdfd")
    frame1.grid(row=0, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame1, [
        ("Open 1.1", TP_tasks.step_1_1),
        ("Open 1.6", TP_tasks.step_1_2),
        ("Generate & Copy SKU Mapping", TP_tasks.step_1_3)
    ])

    # TP Upload
    frame2 = make_step_frame(tp_container, "🍋 TP Upload", "#dbfdfd")
    frame2.grid(row=1, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame2, [
        ("Open 2.1", TP_tasks.step_2_1),
        ("Generate & Upload & Copy TP.csv", TP_tasks.step_2_2),
        ("Copy SKUINV", TP_tasks.step_2_4)
    ])

    # DXM
    frame3 = make_step_frame(tp_container, "🍋 DXM", "#dbfdfd")
    frame3.grid(row=2, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame3, [
        ("Rename & Open", TP_tasks.step_3_1),
        ("Generate & Copy Inventory Update", TP_tasks.step_3_3)
    ])

    for i in range(3):
        tp_container.rowconfigure(i, weight=1)

    return tp_container