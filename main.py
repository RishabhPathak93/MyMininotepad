import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.colorchooser import askcolor
import math

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        # Create text widget
        self.text = tk.Text(master, undo=True)
        self.text.pack(expand=True, fill='both')

        # Create menu bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # Create File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.text.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.text.edit_redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Create Format menu
        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.font_menu = tk.Menu(self.format_menu, tearoff=0)
        self.font_family = tk.StringVar()
        self.font_size = tk.StringVar()
        self.font_family.set("Arial")
        self.font_size.set("12")
        self.font_menu.add_radiobutton(label="Arial", variable=self.font_family, value="Arial",
                                       command=self.change_font)
        self.font_menu.add_radiobutton(label="Times New Roman", variable=self.font_family, value="Times New Roman",
                                       command=self.change_font)
        self.font_menu.add_radiobutton(label="Courier", variable=self.font_family, value="Courier",
                                       command=self.change_font)
        self.font_menu.add_separator()
        self.font_menu.add_radiobutton(label="12", variable=self.font_size, value="12", command=self.change_font)
        self.font_menu.add_radiobutton(label="16", variable=self.font_size, value="16", command=self.change_font)
        self.font_menu.add_radiobutton(label="20", variable=self.font_size, value="20", command=self.change_font)
        self.format_menu.add_cascade(label="Font", menu=self.font_menu)
        self.format_menu.add_command(label="Font Color", command=self.font_color)
        self.format_menu.add_command(label="Highlight Color", command=self.highlight_color)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)

        

        # Create Help menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="About Notepad", command=self.about_notepad)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Create key bindings
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-s>", lambda event: self.save_file())
        self.master.bind("<Control-a>", lambda event: self.select_all())
        self.master.bind("<Control-x>", lambda event: self.cut())
        self.master.bind("<Control-c>", lambda event: self.copy())
        self.master.bind("<Control-v>", lambda event: self.paste())

        # Initialize filename
        self.filename = None

    def new_file(self):
        if self.text.edit_modified():
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to current file?")
            if response:
                self.save_file()
            elif response is None:
                return
        self.text.delete("1.0", "end")
        self.filename = None
        self.master.title("Notepad")

    def open_file(self):
        if self.text.edit_modified():
            response = messagebox.askyesnocancel("Save Changes", "Do you want to save changes to current file?")
            if response:
                self.save_file()
            elif response is None:
                return
        self.filename = filedialog.askopenfilename(defaultextension=".txt",
                                                   filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.text.delete("1.0", "end")
            with open(self.filename, "r") as f:
                self.text.insert("1.0", f.read())
            self.master.title(f"Notepad - {self.filename}")

    def save_file(self):
        if not self.filename:
            self.save_file_as()
        else:
            with open(self.filename, "w") as f:
                f.write(self.text.get("1.0", "end-1c"))
            self.text.edit_modified(False)

    def save_file_as(self):
        self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if self.filename:
            self.save_file()

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end")

    def change_font(self):
        self.text.config(font=(self.font_family.get(), int(self.font_size.get())))

    def font_color(self):
        color = askcolor()
        if color:
            self.text.config(fg=color[1])

    def highlight_color(self):
        color = askcolor()
        if color:
            self.text.config(bg=color[1])

    def about_notepad(self):
        messagebox.showinfo("About Notepad",
                            "Notepad\n\nVersion 1.0\n\nA simple text editor written in Python using Tkinter.")


if __name__ == "__main__":
    root = tk.Tk()
app = Notepad(root)
root.mainloop()
