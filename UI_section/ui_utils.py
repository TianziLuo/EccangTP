import tkinter as tk
from styles import btn_params, header_font
import UI_section.Eccang_tasks as Eccang_tasks
import UI_section.TP_tasks as TP_tasks

def make_step_frame(parent, text, bg_color):
    frame = tk.Frame(
        parent,
        bg=bg_color,
        bd=2,
        relief="ridge",
        padx=4,
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
        ).pack(padx=32, pady=2)
