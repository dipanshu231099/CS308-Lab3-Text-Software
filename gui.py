# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:22:52 2020

@author: Ujjwal Soni
"""

# ---------------imports and initializers---------------
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure



#-------------window and tabs-----------------------
window = tk.Tk()
window.title("Text Analysis App")
#window.attributes("-zoomed",True)   #ubuntu
#window.attributes("-fullscreen",True)   #windows

tabControl = ttk.Notebook(window)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')



#---------------variables to store info------------
count_sentence = tk.StringVar()
count_words = tk.StringVar()
word_most = tk.StringVar()
word_least = tk.StringVar()
lines_with_keywords = tk.StringVar()



# ----------functions--------------------------------
# function to open and access file
def open_file():
    file = filedialog.askopenfilename(initialdir="/home/harish/IIT")
    file = open(file,"r")   # opened in r mode
    data = file.read()      # file info stored in data var
    
    print(data)             # use file
    
    file.close()            # close file


# refresh file to update info
def refresh_file():
    
    print("function to refresh file")

    
# set stats variable inside this function
def calc():
    word_most.set("lincoln") # eg- set most freq word= lincoln
    word_least.set("trump")
    count_sentence.set("10")
    count_words.set("50")


# function to plot graph
def freq_graph():
    word_list=["jimmy","arnold","xyz","json","m","a","b","json","c","d","e","f","g","h","i","j","k"]    # x
    word_count_list=[30,80,67,99,1,80,67,99,1,80,67,99,1,80,67,99,1]                                    # y
    
    # figure to show graph
    fig = Figure(figsize=(12,4), dpi=100)
    fig.add_subplot(111).bar(word_list, word_count_list)
    
    canvas = FigureCanvasTkAgg(fig, master=tab1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=14,column=3)
    
    toolbarFrame = tk.Frame(master=tab1)
    toolbarFrame.grid(row=15,column=4)
    toolbar= NavigationToolbar2Tk(canvas,toolbarFrame)
    toolbar.update()
    canvas.get_tk_widget().grid(row=14,column=4)
    

# find lines with keywords
def extract_data():
    text_box.delete('1.0',tk.END)
    # set extracted in var lines_with_keywords
    lines_with_keywords="qwertyuiopasdfghjklzxcvbnmaaaaaaaaaaaaaaaassssssssssssdsfafdfffffffffffffff\nhi this is LAP\n"
    text_box.insert(tk.END, lines_with_keywords)



#----------------GUI objects----------------------------------
custom_font = font.Font(family='Helvetica', size=15)    # font
# tab-1
label = tk.Label(tab1, text = "")
label.grid(row=1, column=4)
label.config(width=30)
label.config(font=("Courier",44))
ss="Text Analytics Software  "
count=0
text=''
SliderLabel= tk.Label(tab1,text=text,font=('chiller',20),relief=RIDGE,borderwidth=5,width=35,bg='white')
SliderLabel.place(x=400,y=5)
introlabeltick()
# main file
label_main = tk.Label(tab1, text = "Main File",)
label_main.grid(row=3, column=2,padx=20,pady=(50,5))
label_main.config(font=("chiller",20,'bold'))

open_button_main = tk.Button(tab1, text="Select file",font=('chiller',10,'bold'),width=20,bd=6,relief=RIDGE,activebackground='white', command=open_file) # open file fn used here
open_button_main.grid(row=5, column=2)

refresh_button_main = tk.Button(tab1, text="Refresh file",font=('chiller',10,'bold'),width=20,bd=6,relief=RIDGE,activebackground='white', command=refresh_file)  # refresh file fn used here
refresh_button_main.grid(row=5, column=3)

label_main = tk.Label(tab1, text = "Word Statistics",)
label_main.grid(row=6, column=2,padx=20,pady=(50,5))
label_main.config(font=("chiller",20,'bold'))
# stats
stats_button = tk.Button(tab1, text="Calculate stats", command= calc,font=('chiller',10,'bold'),width=20,bd=6,relief=RIDGE,activebackground='white') # calc fn used here
stats_button.grid(row=7, column=2, pady=(20,5))

tk.Label(tab1, text="Most frequent word").grid(row=8, column=2)
entry_most = tk.Entry(tab1, textvariable=word_most)
entry_most.grid(row=8, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="Least frequent word").grid(row=9, column=2)
entry_least = tk.Entry(tab1, textvariable=word_least)
entry_least.grid(row=9, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="No. of sentence").grid(row=10, column=2)
entry_ct_sentence = tk.Entry(tab1, textvariable=count_sentence)
entry_ct_sentence.grid(row=10, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="No. of words").grid(row=11, column=2)
entry_ct_words = tk.Entry(tab1, textvariable=count_words)
entry_ct_words.grid(row=11, column=3, pady=(0,5), padx=(20,0))

#tk.Label(window, text="field").grid(row=11, column=3)
#x = tk.Entry(window, textvariable=variable_to_set)
#x.grid(row=11, column=4)


# histogram
label_main = tk.Label(tab1, text = "Histogram",)
label_main.grid(row=12, column=2,padx=20,pady=(25,5))
label_main.config(font=("chiller",20,'bold'))

graph_button = tk.Button(tab1, text="Frequency Graph", command=freq_graph,font=('chiller',10,'bold'),width=20,bd=6,relief=RIDGE,activebackground='white')
graph_button.grid(row=13, column=2, pady=(10,0))


#tab-2
# keyword file
label_key = tk.Label(tab2, text = "Keywords")
label_key.grid(row=15, column=2, pady=(80,5), padx=(10,0))
label_key.config(font=("Courier",20))
label_key2 = tk.Label(tab2, text = "-   File")
label_key2.grid(row=15, column=3,pady=(80,5))
label_key2.config(font=("Courier",20))

open_button_key = tk.Button(tab2, text="select file", command=open_file)  # open file fn used here
open_button_key.grid(row=16, column=2)

refresh_button_key = tk.Button(tab2, text="Refresh file", command=refresh_file)   # refresh file fn used here
refresh_button_key.grid(row=16, column=3)


#show sentences with keywords
extract_button = tk.Button(tab2, text="Get lines", command= extract_data, font=custom_font)
extract_button.grid(row=18,column=3, pady=(40,5))
label_show = tk.Label(tab2, text="Sentences with keywords:- ")
label_show.grid(row=19, column=3)
text_box = tk.Text(tab2, height=50, width=150)
text_box.grid(row=20,column=4)



#-------------show------------
window.mainloop()
