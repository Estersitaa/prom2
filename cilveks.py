
from test import Cilveks
import tkinter as tk
from tkinter import ttk, END
from tkinter.messagebox import *

# cilveku saraksts

visi_cilveki = []

# root window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('300x300')



# frame
frame = ttk.Frame(root)


# field options
options = {'padx': 5, 'pady': 5}

# temperature label
temperature_label = ttk.Label(frame, text='teksts')
temperature_label.grid(column=0, row=0, sticky='E', **options)

# dzimums label

dzimums_label = ttk.Label(frame, text='teksts')
dzimums_label.grid(column=0, row=0, sticky='E', **options)

# vards entry
vards = tk.StringVar()
vards_entry = ttk.Entry(frame, textvariable=vards)
vards_entry.grid(column=1, row=0, **options)
vards_entry.focus()

dzimums = tk.StringVar()
dzimums_entry = ttk.Entry(frame, textvariable=dzimums)
dzimums_entry.grid(column=1, row=1, **options)

vecums = tk.IntVar()
vecums_entry = ttk.Entry(frame, textvariable=vecums)
vecums_entry.grid(column=1, row=2, **options)
# convert button

#listbox saraksta atjaunosana
def nomainit_sarakstu():
   listbox.delete(0,END)
   for cilveks in visi_cilveki:
      listbox.insert("end","{},{},{}".format(cilveks.name,cilveks.sex,cilveks.age))

def razot_button_clicked():
    rezultats = vards.get()
    cilveka_vards = vards.get()
    cilveka_dzimums = dzimums.get()
    cilveka_vecums = vecums.get()
    visi_cilveki.append(Cilveks(cilveka_vards,cilveka_dzimums,cilveka_vecums))
    result_label.config(text=visi_cilveki[-1].pastastit_par_sevi())
    nomainit_sarakstu()

   

razot_button = ttk.Button(frame, text='ražot')
razot_button.grid(column=2, row=0, **options)
razot_button.configure(command=razot_button_clicked)

def dzimsanas_diena():
   izveletais = listbox.curselection()[0]
   visi_cilveki[izveletais].dz_diena()
   result_label.config(text=visi_cilveki[izveletais].pastastit_par_sevi())
   nomainit_sarakstu()

dzimene_button = ttk.Button(frame, text='dzimene')
dzimene_button.grid(column=5, row=3, **options)
dzimene_button.configure(command=dzimsanas_diena)

dzimenes_poga = ttk

saturs = tk.Variable(value=tuple(visi_cilveki))

listbox = tk.Listbox(
    root,
    listvariable=saturs,
    height=6,
    selectmode=tk.EXTENDED
)
listbox.grid(column=0, row=5, **options)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)


# start the app
root.mainloop()

print("Sveiki, mani sauc {}. Man ir {} gadu. Es esmu {}".format(self.name, self.age, dzimums))