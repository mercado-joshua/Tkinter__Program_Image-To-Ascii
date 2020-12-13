#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import pywhatkit
import os

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Image to Ascii Text Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        fieldset = ttk.LabelFrame(frame, text='Choose Picture')
        fieldset.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.browse_btn = ttk.Button(fieldset, text='Browse', command=self.get_image)
        self.browse_btn.grid(row=0, column=1, padx=5, pady=5, sticky=tk.NSEW)

        self.filepath = tk.StringVar()
        self.filepath_entry = ttk.Entry(fieldset, textvariable=self.filepath, width=100, state=tk.DISABLED)
        self.filepath_entry.grid(row=0, column=2, sticky=tk.W, padx=(0, 5), ipady=5)

        self.convert_btn = ttk.Button(fieldset, text='Convert', command=self.convert_to_ascii)
        self.convert_btn.grid(row=1, column=1, columnspan=2, sticky=tk.E, padx=5, pady=(0, 5))

    # ------------------------------------------
    def convert_to_ascii(self):
        self.convert_btn.config(state=tk.DISABLED)
        filename = 'ascii.txt'
        pywhatkit.image_to_ascii_art(self.filepath.get(), filename)
        os.startfile(filename)
        self.convert_btn.config(state=tk.NORMAL)

    def get_image(self):
        """Open and loads the image file."""
        self.filepath_entry.config(state=tk.NORMAL)

        try:
            file_types = (('JPEG Files', '*.jpg'), ('PNG Files', '*.png'))
            filename = fd.askopenfilename(title='Open', initialdir='/', filetypes=file_types)
            self.filepath.set(filename)

        except Exception as e:
            return

        self.filepath_entry.config(state=tk.DISABLED)

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()