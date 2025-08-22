import tkinter as tk
from Eccang_tasks import (
    run_purchase_files,
    step2_to_4_all,
    step5_copy,
)
from styles import header_font
from ui_utils import make_step_frame, add_task_buttons

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
    eccang_container.grid(row=0, column=0, sticky="nsew", pady=5)
    eccang_container.columnconfigure(0, weight=1)

    # Step frames
    frame1 = make_step_frame(eccang_container, "🍉 Step 1: Purchase Process", "#fadee3")
    frame1.grid(row=0, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame1, [("Update Purchase Folder", run_purchase_files)])

    frame2 = make_step_frame(eccang_container, "🍉 Step 2-4: Unzip ➜ Convert ➜ Rename", "#fadee3")
    frame2.grid(row=1, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame2, [("Unzip, Convert, Rename", step2_to_4_all)])

    frame3 = make_step_frame(eccang_container, "🍉 Step 5: Copy Downloads Files", "#fadee3")
    frame3.grid(row=2, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame3, [("Copy Downloaded Files", step5_copy)])

    for i in range(3):
        eccang_container.rowconfigure(i, weight=1)

    return eccang_container