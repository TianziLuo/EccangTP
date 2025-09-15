import tkinter as tk
import UI_section.refresh_tasks as Refresh_tasks
from styles import header_font
from UI_section.ui_utils import make_step_frame, add_task_buttons


def create_refresh_section(parent):
    refresh_container = tk.LabelFrame(
        parent,
        text="🍉 Refresh",
        font=header_font,
        fg="#072020",
        bg="#d4fade",  
        padx=10,
        pady=10,
        bd=3,
        relief="groove",
        labelanchor="n"
    )
    refresh_container.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
    refresh_container.columnconfigure(0, weight=1)

    # Step 1
    frame1 = make_step_frame(refresh_container, "🌱 Step 1", "#fdfddb")
    frame1.grid(row=0, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame1, [
        ("Open 3.1 FBA", Refresh_tasks.step_1_1),
        ("Open 4.1 FBA Inverntory", Refresh_tasks.step_1_2),
    ])

    # Step 2
    frame2 = make_step_frame(refresh_container, "🌱 Step 2", "#fdfddb")
    frame2.grid(row=1, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame2, [
        ("Open 1.6 FBA Listing", Refresh_tasks.step_2_1),
        ("SKU Mapping & Copy", Refresh_tasks.step_2_2),
    ])

    # Step 3
    frame3 = make_step_frame(refresh_container, "🌱 Step 3", "#fdfddb")
    frame3.grid(row=2, column=0, sticky="nsew", pady=5)
    add_task_buttons(frame3, [
        ("Open 1.2 Database", Refresh_tasks.step_3_1),
        ("Open 2.6 In-transit", Refresh_tasks.step_3_2),
        ("Open 2.9 Purchase", Refresh_tasks.step_3_3),
        ("Open 5.1 Plaque", Refresh_tasks.step_3_4),
        ("Open 5.2 Cushion", Refresh_tasks.step_3_5),
    ])

    for i in range(3):
        refresh_container.rowconfigure(i, weight=1)

    return refresh_container
