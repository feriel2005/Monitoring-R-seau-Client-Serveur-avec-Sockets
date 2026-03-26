# ============================================================
#  dashboard.py — Interface Tkinter temps réel
# ============================================================

import tkinter as tk
from tkinter import ttk
import time

from shared_state import agents, agents_lock


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Network Monitor Dashboard")
        self.geometry("900x500")

        self.tree = ttk.Treeview(
            self,
            columns=("id", "host", "cpu", "ram", "status"),
            show="headings"
        )

        self.tree.heading("id", text="Agent ID")
        self.tree.heading("host", text="Hostname")
        self.tree.heading("cpu", text="CPU %")
        self.tree.heading("ram", text="RAM MB")
        self.tree.heading("status", text="Status")

        self.tree.pack(fill="both", expand=True)

        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        with agents_lock:
            for aid, info in agents.items():
                self.tree.insert("", "end", values=(
                    aid,
                    info["hostname"],
                    f"{info['cpu']:.1f}",
                    f"{info['ram']:.0f}",
                    info["status"]
                ))

        self.after(1000, self.refresh)


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()
