import ctypes

ctypes.windll.kernel32.SetConsoleTitleW('XRthon code editor')

import os
import liner
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import shutil
import custom
import config
from v import v
from folders import folder
from XRthon_main import _XRthon_main_


class Notebook:
    def __init__(self, parent):
        self.parent = parent
        self.parent.bind("<{}-n>".format(config.Settings().bigkey), lambda event: self.add_page())
        # self.parent.bind("<{}-w>".format(config.Settings().bigkey), lambda event: self.close_page())
        self.book = custom.CustomNotebook(parent)
        self.book.pack(side="top", fill="both", expand=True)
        self.frames = []
        self.frame_id = -1
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".XRn", filetypes=[("XRthon Files", "*.XRn"), ("Text Documents", "*.XRn")])
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as f:
                content = f.read()
            try:
                content = self.frames[self.frame_id][1].load_content(content)
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
            _XRthon_main_.var['breakpoints'] = []
    
    def save_file(self):
        file_path = os.path.join(filedialog.asksaveasfilename(initialfile="XRthon File.XRn", defaultextension=".XRn", filetypes=[("XRthon_Files", "*.XRn"), ("Text Documents", "*.XRn")]))
        if file_path:
            try:
                content = self.frames[self.frame_id][1].get_text()
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(content)

    def run_file(self):
        if self.frame_id != -1:
            try:
                content = self.frames[self.frame_id][1].get_text()
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
            temp_file_path = f"temp.XRn"
            with open(os.path.join(folder, './temp/', temp_file_path), 'w', encoding='UTF-8') as f:
                f.write(content)
            
            with open(os.path.join(folder, './temp/', temp_file_path), 'r', encoding='UTF-8') as f:
                _XRthon_main_.XRthon_file(f, os.path.join(folder, '/temp/', temp_file_path))
    
    def toggle_breakpoint(self):
        try:
            line_number = self.frames[self.frame_id][1].get_lineno_at_cursor()
            _XRthon_main_.var['breakpoints'].append(line_number + 1)
            if line_number in self.frames[self.frame_id][1].breakpoints:
                self.frames[self.frame_id][1].remove_breakpoint(line_number)
            else:
                self.frames[self.frame_id][1].set_breakpoint(line_number)
        except:
            self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")

    def add_updater(self, frame, line):
        self.frame_id = self.frames.index([frame, line])

    def add_page(self):
        frame = tk.Frame(self.parent)
        line = liner.Liner(frame)
        line.pack(fill="both", expand=True)
        self.frames.append([frame, line])
        # frame.bind('<Visibility>', lambda event: self.add_updater(frame, line))
        frame.bind('<Configure>', lambda event: self.add_updater(frame, line))
        self.book.add(frame, text="XRthon File")
        self.frame_id = len(self.frames) - 1
        menubar = tk.Menu(self.parent)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="F_Open ", command=self.open_file)
        file_menu.add_command(label="F_Save", command=self.save_file)
        file_menu.add_command(label="R_Run", command=self.run_file)
        file_menu.add_command(label="Set Breakpoint (Where the cursor is)", command=self.toggle_breakpoint)
        menubar.add_cascade(label="All", menu=file_menu)
        self.parent.config(menu=menubar)

        self.book.select(self.frame_id)

    def add_info_page(self, text="Information", title="Information"):
        frame = tk.Frame(self.parent)
        
        info_label = tk.Label(frame, text=text, wraplength=400, justify=tk.LEFT)
        info_label.pack(fill="both", expand=True)

        self.frames.append([frame, info_label])
        self.book.add(frame, text=title)
        self.frame_id = len(self.frames) - 1

        self.book.select(self.frame_id)
    
    def show_popup(self, message, title):
        messagebox.showinfo(title, message)

    def update(self):
        if self.parent.wm_state() == "iconic":
            pass
        if self.frame_id == -1:
            return
        if isinstance(self.frames[self.frame_id][1], liner.Liner) and not isinstance(self.frames[self.frame_id][1], tk.Label): 
            self.frames[self.frame_id][1].redraw()

class TEST_():
    def __init__(self):
        pass
    
    def __INIT__(self):
        try:
            root = tk.Tk()
            book = Notebook(root)
            book.add_page()
            book.add_info_page (f'''This is a text (XRthon code) editor that I wrote with my friend LoveProgramming
If you click on the XRthon File page, the content of the XRthon File page will be used when you click back
Version: {v(0.1, '__0.0.3__ V')}''', 'Start Screen')
            book.show_popup ('Welcome to XRthon Editor !!', 'Welcome !!')
            book.show_popup('Run code in command line', 'Hint')
            while True:
                root.update()
                book.update()
                try:
                    os.remove(os.path.join(folder, './temp/', 'temp.XRn'))
                    self.dels()
                except PermissionError:
                    pass
                except FileNotFoundError:
                    pass
        except tk.TclError:
            quit()

    def dels(self):
        pycache_1 = os.path.join(folder, './__pycache__')
        pycache_2 = os.path.join(folder, './custom/__pycache__')
        if os.path.exists(pycache_1) and os.path.exists(pycache_2):
            shutil.rmtree(pycache_1)
            shutil.rmtree(pycache_2)

TEST = TEST_()
TEST.dels()
