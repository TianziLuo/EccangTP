import tkinter as tk
from UI_section.Diary_task import run_output, open_files
from styles import header_font
from UI_section.ui_utils import make_step_frame, add_task_buttons

def create_diary_section(parent):
    # Main container for the Diary section
    diary_container = tk.LabelFrame(
        parent,
        text="🍉 Diary",
        font=header_font,
        fg="#072020",
        bg="#D1FAE5",
        padx=10,
        pady=10,
        bd=3,
        relief="groove",
        labelanchor="n"
    )
    diary_container.grid(row=0, column=0, sticky="nsew", pady=0)
    diary_container.columnconfigure(0, weight=1)
    diary_container.rowconfigure(0, weight=1)

    # Step frame inside container
    frame1 = make_step_frame(diary_container, "🍉 Diary In", "#fdfddb")
    frame1.grid(row=0, column=0, sticky="nsew", padx=10)
    add_task_buttons(frame1, [("Open Diary", open_files)])

    frame2 = make_step_frame(diary_container, "🍉 Diary Out", "#fdfddb")
    frame2.grid(row=0, column=1, sticky="nsew", padx=10)
    add_task_buttons(frame2, [("Diary Output", run_output)])


    return diary_container