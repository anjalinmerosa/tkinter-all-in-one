"""
Tkinter All-in-One Project
===========================
A single-file demo application that showcases almost every commonly-used
Tkinter and ttk feature, organized into tabs so it's easy to study and
easy to grade / demo.

Covers:
  - Root window setup, geometry, icon, resizing, title
  - Menu bar (File, Edit, Help) with submenus, accelerators, checkbuttons
  - Layout managers: pack, grid, place  (each in its own tab)
  - Core widgets: Label, Button, Entry, Text, Checkbutton, Radiobutton,
    Listbox, Scale, Spinbox, Scrollbar
  - ttk widgets: Notebook (tabs), Combobox, Treeview, Progressbar,
    Separator, Sizegrip
  - Canvas drawing (shapes, text, and simple mouse-driven drawing)
  - Dialog boxes: messagebox, filedialog, simpledialog, colorchooser
  - Toplevel (secondary window / modal-style popup)
  - Event binding (keyboard + mouse), and the after() timer loop
  - Simple MVC-ish structure: one App class owns all state

Run:
    python tkinter_all_in_one.py
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog, simpledialog, colorchooser


class App(tk.Tk):
    """Root application window."""

    def __init__(self):
        super().__init__()
        self.title("Tkinter All-in-One Project")
        self.geometry("900x650")
        self.minsize(760, 560)

        # Shared state used across tabs
        self.status_var = tk.StringVar(value="Ready")
        self.word_wrap_var = tk.BooleanVar(value=True)

        self._build_menu()
        self._build_notebook()
        self._build_status_bar()

        # Global key binding: Escape closes the app, Ctrl+Q too
        self.bind("<Escape>", lambda e: self.on_quit())
        self.bind("<Control-q>", lambda e: self.on_quit())

    # ------------------------------------------------------------------
    # Menu bar
    # ------------------------------------------------------------------
    def _build_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File...", accelerator="Ctrl+O",
                               command=self.open_file)
        file_menu.add_command(label="Save As...", accelerator="Ctrl+S",
                               command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", accelerator="Ctrl+Q",
                               command=self.on_quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.bind_all("<Control-o>", lambda e: self.open_file())
        self.bind_all("<Control-s>", lambda e: self.save_file())

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_checkbutton(label="Word Wrap (Text tab)",
                                   variable=self.word_wrap_var,
                                   command=self.toggle_wrap)
        edit_menu.add_command(label="Ask my name (simpledialog)",
                               command=self.ask_name)
        edit_menu.add_command(label="Pick a color...",
                               command=self.pick_color)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.config(menu=menubar)

    # ------------------------------------------------------------------
    # Notebook (tabs) — each tab demonstrates a topic
    # ------------------------------------------------------------------
    def _build_notebook(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=(8, 0))

        self.notebook.add(self._tab_widgets(), text="Basic Widgets")
        self.notebook.add(self._tab_pack(), text="Pack Layout")
        self.notebook.add(self._tab_grid(), text="Grid Layout")
        self.notebook.add(self._tab_place(), text="Place Layout")
        self.notebook.add(self._tab_text(), text="Text + Scrollbar")
        self.notebook.add(self._tab_treeview(), text="Treeview")
        self.notebook.add(self._tab_canvas(), text="Canvas Drawing")
        self.notebook.add(self._tab_dialogs(), text="Dialogs")

    # ---- Tab 1: Basic widgets --------------------------------------
    def _tab_widgets(self):
        frame = ttk.Frame(self.notebook)

        ttk.Label(frame, text="Label / Entry / Button", font=("Segoe UI", 12, "bold")
                  ).grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 4))

        ttk.Label(frame, text="Enter your name:").grid(row=1, column=0, sticky="e", padx=10, pady=4)
        self.name_entry = ttk.Entry(frame, width=25)
        self.name_entry.grid(row=1, column=1, sticky="w", padx=10, pady=4)

        ttk.Button(frame, text="Greet Me", command=self.greet
                   ).grid(row=1, column=2, padx=10, pady=4)

        # Checkbutton
        self.subscribe_var = tk.BooleanVar()
        ttk.Checkbutton(frame, text="Subscribe to newsletter",
                         variable=self.subscribe_var).grid(row=2, column=0, columnspan=2,
                                                             sticky="w", padx=10, pady=4)

        # Radiobuttons
        ttk.Label(frame, text="Choose a plan:").grid(row=3, column=0, sticky="e", padx=10, pady=4)
        self.plan_var = tk.StringVar(value="basic")
        plan_frame = ttk.Frame(frame)
        plan_frame.grid(row=3, column=1, sticky="w")
        for text, val in [("Basic", "basic"), ("Pro", "pro"), ("Enterprise", "enterprise")]:
            ttk.Radiobutton(plan_frame, text=text, value=val, variable=self.plan_var
                             ).pack(side="left", padx=4)

        # Listbox
        ttk.Label(frame, text="Pick fruits:").grid(row=4, column=0, sticky="ne", padx=10, pady=4)
        self.fruit_list = tk.Listbox(frame, selectmode="multiple", height=5, exportselection=False)
        for fruit in ["Apple", "Banana", "Cherry", "Date", "Elderberry"]:
            self.fruit_list.insert("end", fruit)
        self.fruit_list.grid(row=4, column=1, sticky="w", padx=10, pady=4)

        # Scale + Spinbox
        ttk.Label(frame, text="Volume:").grid(row=5, column=0, sticky="e", padx=10, pady=4)
        self.volume_var = tk.IntVar(value=50)
        ttk.Scale(frame, from_=0, to=100, variable=self.volume_var,
                  orient="horizontal").grid(row=5, column=1, sticky="we", padx=10, pady=4)

        ttk.Label(frame, text="Quantity:").grid(row=6, column=0, sticky="e", padx=10, pady=4)
        self.qty_spin = ttk.Spinbox(frame, from_=1, to=20, width=5)
        self.qty_spin.set(1)
        self.qty_spin.grid(row=6, column=1, sticky="w", padx=10, pady=4)

        # Combobox
        ttk.Label(frame, text="Country:").grid(row=7, column=0, sticky="e", padx=10, pady=4)
        self.country_combo = ttk.Combobox(frame, values=["India", "USA", "UK", "Germany", "Japan"],
                                           state="readonly", width=22)
        self.country_combo.current(0)
        self.country_combo.grid(row=7, column=1, sticky="w", padx=10, pady=4)

        # Progressbar
        ttk.Label(frame, text="Progress:").grid(row=8, column=0, sticky="e", padx=10, pady=4)
        self.progress = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(row=8, column=1, sticky="w", padx=10, pady=4)
        ttk.Button(frame, text="Run", command=self.run_progress).grid(row=8, column=2, padx=10)

        ttk.Separator(frame, orient="horizontal").grid(row=9, column=0, columnspan=3, sticky="we", pady=8)

        frame.columnconfigure(1, weight=1)
        return frame

    def greet(self):
        name = self.name_entry.get().strip() or "stranger"
        picks = [self.fruit_list.get(i) for i in self.fruit_list.curselection()]
        picks_txt = ", ".join(picks) if picks else "no fruits"
        self.set_status(f"Hello, {name}! Plan={self.plan_var.get()}, Fruits={picks_txt}")

    def run_progress(self):
        self.progress["value"] = 0
        self._animate_progress()

    def _animate_progress(self):
        if self.progress["value"] < 100:
            self.progress["value"] += 5
            self.after(40, self._animate_progress)  # after() timer loop
        else:
            self.set_status("Progress complete!")

    # ---- Tab 2: pack() ----------------------------------------------
    def _tab_pack(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="pack() stacks widgets top/bottom or left/right",
                  font=("Segoe UI", 11, "bold")).pack(pady=10)

        top = ttk.Frame(frame)
        top.pack(fill="x", padx=20)
        for i, color in enumerate(["#e74c3c", "#3498db", "#2ecc71"]):
            tk.Label(top, text=f"pack side=left  #{i+1}", bg=color, fg="white",
                     width=18, height=2).pack(side="left", padx=4, pady=4)

        bottom = ttk.Frame(frame)
        bottom.pack(fill="x", padx=20, pady=10)
        for i, color in enumerate(["#9b59b6", "#f39c12"]):
            tk.Label(bottom, text=f"pack side=top  #{i+1}", bg=color, fg="white",
                     width=25, height=2).pack(side="top", padx=4, pady=4)
        return frame

    # ---- Tab 3: grid() -----------------------------------------------
    def _tab_grid(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="grid() places widgets in a row/column matrix",
                  font=("Segoe UI", 11, "bold")).grid(row=0, column=0, columnspan=4, pady=10)

        colors = ["#1abc9c", "#e67e22", "#34495e", "#e84393"]
        idx = 0
        for r in range(1, 4):
            for c in range(4):
                tk.Label(frame, text=f"({r},{c})", bg=colors[idx % 4], fg="white",
                         width=10, height=3).grid(row=r, column=c, padx=4, pady=4)
                idx += 1
        return frame

    # ---- Tab 4: place() -----------------------------------------------
    def _tab_place(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="place() uses absolute or relative x/y coordinates",
                  font=("Segoe UI", 11, "bold")).place(x=10, y=10)

        tk.Label(frame, text="Top-left (10,50)", bg="#c0392b", fg="white"
                  ).place(x=10, y=50)
        tk.Label(frame, text="Centered (relx=0.5, rely=0.5, anchor=center)",
                  bg="#2980b9", fg="white").place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(frame, text="Bottom-right (relx=1, rely=1, anchor=se)",
                  bg="#27ae60", fg="white").place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
        return frame

    # ---- Tab 5: Text widget + Scrollbar -------------------------------
    def _tab_text(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="Multi-line Text widget with a Scrollbar",
                  font=("Segoe UI", 11, "bold")).pack(pady=(10, 4))

        text_frame = ttk.Frame(frame)
        text_frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(text_frame, orient="vertical")
        self.text_widget = tk.Text(text_frame, wrap="word", yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_widget.yview)

        self.text_widget.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.text_widget.insert("1.0", "Type here...\n\nTry Ctrl+O to open a file, "
                                        "Ctrl+S to save its contents, and toggle "
                                        "'Word Wrap' from the Edit menu.")

        # Key event binding example: show live char count in status bar
        self.text_widget.bind("<KeyRelease>", self._on_text_change)
        return frame

    def _on_text_change(self, event):
        content = self.text_widget.get("1.0", "end-1c")
        self.set_status(f"Characters: {len(content)}")

    def toggle_wrap(self):
        self.text_widget.config(wrap="word" if self.word_wrap_var.get() else "none")

    # ---- Tab 6: Treeview (table) --------------------------------------
    def _tab_treeview(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="ttk.Treeview used as a simple table",
                  font=("Segoe UI", 11, "bold")).pack(pady=(10, 4))

        columns = ("name", "age", "city")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=8)
        for col, label, width in [("name", "Name", 150), ("age", "Age", 80), ("city", "City", 150)]:
            tree.heading(col, text=label)
            tree.column(col, width=width, anchor="center")

        sample_rows = [
            ("Asha", 28, "Chennai"),
            ("Ravi", 34, "Mumbai"),
            ("Meera", 22, "Bengaluru"),
            ("Karan", 40, "Delhi"),
            ("Divya", 31, "Hyderabad"),
        ]
        for row in sample_rows:
            tree.insert("", "end", values=row)

        tree.pack(fill="both", expand=True, padx=10, pady=10)
        tree.bind("<<TreeviewSelect>>", lambda e: self._on_tree_select(tree))
        return frame

    def _on_tree_select(self, tree):
        selected = tree.focus()
        if selected:
            values = tree.item(selected, "values")
            self.set_status(f"Selected row: {values}")

    # ---- Tab 7: Canvas -------------------------------------------------
    def _tab_canvas(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="Canvas: shapes + click-and-drag drawing",
                  font=("Segoe UI", 11, "bold")).pack(pady=(10, 4))

        self.canvas = tk.Canvas(frame, bg="white", height=350)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)

        # Pre-drawn shapes
        self.canvas.create_rectangle(20, 20, 120, 100, fill="#3498db", outline="")
        self.canvas.create_oval(140, 20, 240, 100, fill="#e74c3c", outline="")
        self.canvas.create_line(260, 20, 360, 100, width=3, fill="#2c3e50")
        self.canvas.create_polygon(380, 100, 430, 20, 480, 100, fill="#f1c40f")
        self.canvas.create_text(250, 130, text="Click and drag below to draw freehand",
                                 font=("Segoe UI", 10, "italic"))

        # Mouse event bindings for freehand drawing
        self.canvas.bind("<B1-Motion>", self._draw_on_canvas)
        self.canvas.bind("<ButtonPress-3>", lambda e: self.canvas.delete("freehand"))

        ttk.Label(frame, text="Left-drag to draw, right-click to clear your drawing"
                  ).pack(pady=(0, 8))
        return frame

    def _draw_on_canvas(self, event):
        r = 3
        self.canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                                 fill="#8e44ad", outline="", tags="freehand")

    # ---- Tab 8: Dialogs --------------------------------------------------
    def _tab_dialogs(self):
        frame = ttk.Frame(self.notebook)
        ttk.Label(frame, text="Common dialog boxes", font=("Segoe UI", 11, "bold")
                  ).pack(pady=(10, 10))

        btns = [
            ("Info message", lambda: messagebox.showinfo("Info", "This is an info dialog.")),
            ("Warning message", lambda: messagebox.showwarning("Warning", "This is a warning.")),
            ("Error message", lambda: messagebox.showerror("Error", "This is an error dialog.")),
            ("Ask Yes/No", self.ask_yes_no),
            ("Open file dialog", self.open_file),
            ("Save file dialog", self.save_file),
            ("Ask for text (simpledialog)", self.ask_name),
            ("Pick a color", self.pick_color),
            ("Open a Toplevel popup", self.open_popup),
        ]
        for text, cmd in btns:
            ttk.Button(frame, text=text, command=cmd, width=32).pack(pady=4)

        return frame

    def ask_yes_no(self):
        result = messagebox.askyesno("Confirm", "Do you like Tkinter?")
        self.set_status(f"You answered: {'Yes' if result else 'No'}")

    def open_file(self):
        path = filedialog.askopenfilename(title="Open a file")
        if path:
            try:
                with open(path, "r", errors="ignore") as f:
                    content = f.read()
                self.text_widget.delete("1.0", "end")
                self.text_widget.insert("1.0", content)
                self.notebook.select(4)  # jump to Text tab
                self.set_status(f"Opened: {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")

    def save_file(self):
        path = filedialog.asksaveasfilename(title="Save file as", defaultextension=".txt")
        if path:
            try:
                content = self.text_widget.get("1.0", "end-1c")
                with open(path, "w") as f:
                    f.write(content)
                self.set_status(f"Saved: {path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")

    def ask_name(self):
        name = simpledialog.askstring("Your name", "What should I call you?")
        if name:
            self.set_status(f"Nice to meet you, {name}!")

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose a color")
        if color and color[1]:
            self.set_status(f"Picked color: {color[1]}")
            self.config(bg=color[1])

    def open_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Toplevel Popup")
        popup.geometry("300x150")
        popup.transient(self)   # stays on top of main window
        popup.grab_set()        # modal-ish: blocks interaction with main window

        ttk.Label(popup, text="I'm a secondary (Toplevel) window!",
                  font=("Segoe UI", 10, "bold")).pack(pady=20)
        ttk.Button(popup, text="Close", command=popup.destroy).pack()

    def show_about(self):
        messagebox.showinfo("About", "Tkinter All-in-One Project\nBuilt with Python's tkinter + ttk.")

    # ------------------------------------------------------------------
    # Status bar + misc
    # ------------------------------------------------------------------
    def _build_status_bar(self):
        bar = ttk.Frame(self)
        bar.pack(fill="x", side="bottom")
        ttk.Separator(bar, orient="horizontal").pack(fill="x")
        ttk.Label(bar, textvariable=self.status_var, anchor="w").pack(side="left", padx=8, pady=4)
        ttk.Sizegrip(bar).pack(side="right")

    def set_status(self, message):
        self.status_var.set(message)

    def on_quit(self):
        if messagebox.askokcancel("Quit", "Close the application?"):
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_quit)
    app.mainloop()
