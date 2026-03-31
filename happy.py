import tkinter as tk
import random

messages = [
    ">>> Accessing system...",
    ">>> Injecting script...",
    ">>> Camera hacked!",
    ">>> Uploading data...",
    ">>> Password found!",
    ">>> System override..."
]

def create_window():
    win = tk.Toplevel()
    win.configure(bg="black")

    # مكان عشوائي
    x = random.randint(0, 800)
    y = random.randint(0, 500)
    win.geometry(f"300x150+{x}+{y}")

    text = tk.Text(win, bg="black", fg="lime", font=("Consolas", 10))
    text.pack(expand=True, fill="both")

    def write_text():
        msg = random.choice(messages)
        text.insert(tk.END, msg + "\n")
        text.see(tk.END)
        win.after(1000, write_text)

    write_text()

    # يخليها فوق كل حاجة
    win.attributes("-topmost", True)

def spawn_windows():
    create_window()
    root.after(3000, spawn_windows)  # كل 3 ثواني نافذة جديدة

root = tk.Tk()
root.withdraw()  # يخفي النافذة الأساسية

spawn_windows()

root.mainloop()
