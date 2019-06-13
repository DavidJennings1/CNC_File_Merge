import tkinter as tk
from tkinter import filedialog  # noqa: F401
from tkinter import ttk
import re
import os


#  To Do
#  github push test
#  Create template if none exists
#  Exception handling
#  Scan file for rotations
#  Create King icon

#  self.iconbitmap('py.ico')

class File_Merge(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('CNC File Merge')
        self.files = []  # List of selected files
        self.machine = ''

        # --------------------Top Frame

        title_frame = tk.Frame(self, bd=10)
        title_frame.pack(side=tk.TOP)

        title = tk.Label(title_frame, text='CNC File Merge')
        title.grid(column=0, row=0, sticky=tk.E+tk.W)

        # --------------------Bottom Frame

        frame2 = tk.Frame(self, bd=10)
        frame2.pack(side=tk.TOP, fill=tk.X)

        frame3 = tk.Frame(self, bd=10)
        frame3.pack(side=tk.TOP, fill=tk.X)

        frame4 = tk.Frame(self, bd=10)
        frame4.pack(side=tk.BOTTOM, fill=tk.X)

        # --------------------Combo Boxes

        label1 = tk.Label(frame2, text='Choose Machine')
        label1.grid(column=0, row=0)

        self.choose_machine_combo = ttk.Combobox(frame2, width=19)
        self.choose_machine_combo.set('MH13')
        self.choose_machine_combo['values'] = ('MH06', 'MH08', 'MH09', 'MH13')
        self.choose_machine_combo.bind("<<>ComboboxSelected>")
        self.choose_machine_combo.grid(column=1, row=0)

        label2 = tk.Label(frame2, text='Choose offset template')
        label2.grid(column=0, row=1)

        self.choose_offset_template_combo = ttk.Combobox(frame2, width=19)
        self.choose_offset_template_combo.set('Custom')
        self.choose_offset_template_combo['values'] = ('None', 'Custom')
        self.choose_offset_template_combo.bind("<<>ComboboxSelected>")
        self.choose_offset_template_combo.grid(column=1, row=1)

        label3 = tk.Label(frame3, text='Pallet Change')
        label3.grid(column=0, row=2)

        self.pallet_change_combo = ttk.Combobox(frame3, width=19)
        self.pallet_change_combo.set('None')
        self.pallet_change_combo['values'] = ('None', 'After 1st', 'After 2nd',
                                              'After 3rd', 'After 4th')
        self.pallet_change_combo.bind("<<>ComboboxSelected>")
        self.pallet_change_combo.grid(column=1, row=2)

        # --------------------Listbox

        self.file_listbox = tk.Listbox(frame3, bg='light blue', height=5,
                                       width=65, bd=1)
        self.file_listbox.grid(column=0, row=0, columnspan=4,
                               rowspan=2, sticky=tk.E+tk.W)

        # --------------------Buttons

        self.choose_file_button = tk.Button(frame3, text="Add File",
                                            relief=tk.RAISED,
                                            width=16, bd=2, padx=10, pady=6)
        self.choose_file_button.bind('<ButtonRelease-1>', self.choose_files)
        self.choose_file_button.grid(column=5, row=0)

        self.merge_file_button = tk.Button(frame3, text="Merge Files",
                                           relief=tk.RAISED,
                                           width=16, bd=2, padx=10, pady=6)
        self.merge_file_button.bind('<ButtonRelease-1>', self.merge_files)
        self.merge_file_button.grid(column=5, row=1)

        self.process_file_button = tk.Button(frame4,
                                             text="Process Merged File",
                                             relief=tk.RAISED,
                                             width=16, bd=2, padx=10, pady=6)
        self.process_file_button.bind('<ButtonRelease-1>', self.process_file)
        self.process_file_button.grid(column=0, row=3)

        # open_merged_file_button = tk.Button(frame2, text="Open Merged File",
        #                                     relief=tk.RAISED, width=16, bd=2,
        #                                     padx=10, pady=6)
        # open_merged_file_button.grid(column=1, row=5)

        # reset_button = tk.Button(frame2, text="Reset", relief=tk.RAISED,
        #                     bd=2, padx=10, pady=6)
        # reset_button.bind('<ButtonRelease-1>', reset)
        # reset_button.grid(column=4, row=7)

        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Open', command=self.open_merged_file)
        edit_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(label='MH06 Template',
                              command=self.menu_action_06)
        edit_menu.add_command(label='MH08 Template',
                              command=self.menu_action_08)
        edit_menu.add_command(label='MH09 Template',
                              command=self.menu_action_09)
        edit_menu.add_command(label='MH13 Template',
                              command=self.menu_action_13)
        # self.geometry('600x400+0+0')

    def choose_files(self, event):

        with open('fileMerge.ini', 'r') as f:
            self.idir = f.read()
        self.machine = self.choose_machine_combo.get()
        filetypes_string = ("(('{} Files', '*.{}'), ('All Files', '*.*'))"
                            .format(self.machine, self.machine))
        self.filetypes = eval(filetypes_string)
        self.filename = (tk.filedialog.askopenfilename
                         (initialdir=self.idir, title='Add File',
                          filetypes=self.filetypes))
        self.idir = os.path.split(self.filename)[0]
        with open('fileMerge.ini', 'w') as f:
            f.write(self.idir)

        self.file_listbox.insert(tk.END, self.filename)
        self.files.append(self.filename)
        while '' in self.files:
            self.files.remove('')

    def replacement_function_director(self, event):
        if self.machine == 'mh06':
            pass
        elif self.machine == 'mh08':
            pass
        elif self.machine == 'mh09':
            pass
        elif self.machine == 'mh13':
            pass

    def merge_files(self, event):
        self.choose_file_button.unbind('<ButtonRelease-1>')
        self.merge_file_button.unbind('<ButtonRelease-1>')
        self.new_file = (tk.filedialog.asksaveasfilename
                         (initialdir=self.idir, title="Add File",
                          filetypes=self.filetypes))
        with open(self.new_file, 'w') as f:
            for fname in self.files:
                with open(fname) as infile:
                    f.write(infile.read())
                    print('\n')
        self.file_listbox.insert(tk.END, self.new_file)
        # substitution()

        # open_merged_file_button.bind('<ButtonRelease-1>', open_merged_file)

    def reset(self, event):
        pass

    def menu_action(self):
        pass

    def menu_action_06(self):
        os.startfile('Offset_Templates\\MH06_Template.txt')

    def menu_action_08(self):
        os.startfile('Offset_Templates\\MH08_Template.txt')

    def menu_action_09(self):
        os.startfile('Offset_Templates\\MH09_Template.txt')

    def menu_action_13(self):
        os.startfile('Offset_Templates\\MH13_Template.txt')

    def open_merged_file(self):
        """ Open external data storage file in Notepad"""
        os.startfile(self.new_file)

    def process_file(self, event):

        #  Read in the file
        with open(self.new_file, 'r') as filein:
            filedata = filein.read()

        with open('Offset_Templates/workshift_offset_pattern.txt',
                  'r') as filepat:
            work_shift_pattern = filepat.read()

        custom_template = self.choose_offset_template_combo.get()
        if custom_template == 'Custom':
            custom_pattern = ('Offset_Templates\\{}_Template.{}').format(self.machine, 'txt')
            with open(custom_pattern, 'r') as offpat:
                self.custom_offset_pattern = offpat.read()

        # Replace the target string
        filedata = filedata.replace(work_shift_pattern,
                                    self.custom_offset_pattern, 1)
        filedata = filedata.replace(work_shift_pattern, '')

        pattern2 = re.compile(r'O\d+')
        match2 = pattern2.findall(filedata)

        index = 0
        ln = 1000
        while index < (len(match2)):
            match2[index] = ('{}{}').format('N', ln)
            filedata = filedata.replace('O1', match2[index], 1)
            index += 1
            ln += 1000
        filedata = filedata.replace('N1000', 'O1', 1)
        if self.machine == 'MH06':
            pattern_mh06 = re.compile(r'M99\n%\n%\n')
            filedata = re.sub(pattern_mh06, '', filedata)
        if self.machine == 'MH13':
            pattern_mh13 = re.compile(r'T60M6\nM98P9901\nM30\n%\n%')
            filedata = re.sub(pattern_mh13, 'M1', filedata)

        pattern3 = re.compile(r'T\d+')
        match3 = pattern3.findall(filedata)
        rep_t60 = []
        for i, j in enumerate(match3):
            if j == 'T60':
                if (i + 1) < len(match3):
                    rep_t60.append(match3[(i + 1)])
                    print(rep_t60)
    #     rep_t60 = [w.replace('M6', '') for w in rep_t60]
        index2 = 0
        while index2 < (len(rep_t60)):
            filedata = filedata.replace('T60', rep_t60[index2], 1)
            index2 += 1
        self.file_listbox.insert(tk.END, 'Operation Complete')
        # Write the file out

        with open(self.new_file, 'w') as file:
            file.write(filedata)


root = File_Merge()
root.mainloop()
