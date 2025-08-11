from ui import create_main_window
from tkinter import messagebox
from verify import verify_license
import sys


if __name__ == "__main__":
    ok, msg = verify_license()
    if not ok:
        messagebox.showerror("License fail", msg)
        sys.exit()

    create_main_window().mainloop()
