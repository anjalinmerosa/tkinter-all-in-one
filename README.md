# Tkinter All-in-One Project

A single-file Python desktop application built with **Tkinter** and **ttk** that
demonstrates the core building blocks of GUI programming: widgets, layout
managers, events, dialogs, menus, and canvas drawing — all organized into a
clean tabbed interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Menu bar** — File / Edit / Help with keyboard accelerators (Ctrl+O, Ctrl+S, Ctrl+Q)
- **Basic widgets** — Label, Entry, Button, Checkbutton, Radiobutton, Listbox,
  Scale, Spinbox, Combobox, Progressbar
- **Layout managers** — dedicated tabs for `pack()`, `grid()`, and `place()`
- **Text editor tab** — multi-line `Text` widget with a linked `Scrollbar` and
  live character-count updates on keypress
- **Treeview** — a sortable table widget populated with sample data
- **Canvas** — pre-drawn shapes (rectangle, oval, line, polygon) plus
  click-and-drag freehand drawing
- **Dialogs** — `messagebox`, `filedialog`, `simpledialog`, `colorchooser`,
  and a custom `Toplevel` popup window
- **Status bar** — live feedback for user actions across every tab

## Screenshot

*(Add a screenshot here — see instructions below)*

## Getting Started

### Prerequisites
- Python 3.8 or higher (Tkinter ships with the standard library — no extra
  installs needed on Windows/macOS; on Linux you may need
  `sudo apt-get install python3-tk`)

### Run it
```bash
git clone https://github.com/<your-username>/tkinter-all-in-one.git
cd tkinter-all-in-one
python tkinter_all_in_one.py
```

## Project Structure
```
tkinter-all-in-one/
├── tkinter_all_in_one.py   # Main application (single file)
└── README.md
```

## What I Learned

- How Tkinter's event loop (`mainloop()`) and event bindings work
- The tradeoffs between `pack`, `grid`, and `place` layout managers
- Building multi-tab interfaces with `ttk.Notebook`
- Linking widget state to Python variables via `StringVar` / `IntVar` / `BooleanVar`
- Using built-in dialogs instead of building custom popups from scratch

## License

This project is open source and available under the [MIT License](LICENSE).