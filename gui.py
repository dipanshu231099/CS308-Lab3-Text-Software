# ---------------imports and initializers---------------
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
#from matplotlib.figure import Figure
import API

# ----------- Custom Classes ----------------------
class CustomText(tk.Text):
    '''A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246
    '''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                        regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")


#-------------window and tabs-----------------------
window = tk.Tk()
window.title("Text Analysis App")
window.attributes("-zoomed",True)   #ubuntu
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
path_of_file= tk.StringVar()
path_of_file2= tk.StringVar()
lines_with_keywords = tk.StringVar()
main_file = tk.StringVar()
keyword_file = tk.StringVar()
fig = plt.Figure(figsize=(8,4), dpi=100)


# ----------functions--------------------------------
# function to open and access file
def open_file(is_keyword_file = False):
    file = filedialog.askopenfilename(initialdir="~")
    if (not is_keyword_file): 
        main_file.set(file)
        path_of_file.set(file)
    else:
        keyword_file.set(file)
        path_of_file2.set(file)


# refresh file to update info
def refresh_file():
    calc()
    #canvas.delete("all")
    
    freq_graph()
    print("function to refresh file")

    
# set stats variable inside this function
def calc():
    
    file_path = main_file.get()   ## file path of selected file
    print("File path is-",file_path)
    
    ## calculating most frequent word
    most_freq = (API.mostOccuringWords(file_path))[0][0]
    print("Most frquent word is" , most_freq)
    word_most.set(most_freq)

    ## calculating least frequent word
    least_freq = (API.leastOccuringWord(file_path))[0][0]
    print("Least frquent word is" , least_freq)
    word_least.set(least_freq)

    ## Number of sentences/lines
    sentence_count = API.lineCounter(file_path)
    count_sentence.set(sentence_count)

    ## Calculating words count
    word_count = (API.WordCounter(file_path)) 
    print("The word count is" , word_count)
    count_words.set(word_count)


# function to plot graph
def freq_graph():
    fig.clf()
    file_path = main_file.get()
    mapping = API.wordMapper(file_path)
    word_list = list(mapping.keys())
    word_count_list = list(mapping.values())


    # figure to show graph
    #fig = Figure(figsize=(12,4), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(word_list, word_count_list)
    ax.set_xticklabels(word_list, rotation=90)
    
    canvas = FigureCanvasTkAgg(fig, master=tab1)
    canvas.draw()
    canvas.get_tk_widget().grid(row=14,column=3)
    
    toolbarFrame = tk.Frame(master=tab1)
    toolbarFrame.grid(row=15,column=4)
    toolbar= NavigationToolbar2Tk(canvas,toolbarFrame)
    toolbar.update()
    canvas.get_tk_widget().grid(row=14,column=4)


#----------------GUI objects----------------------------------
custom_font = font.Font(family='Helvetica', size=15)    # font
# tab-1    
label = tk.Label(tab1, text = "Text Analytics")
label.grid(row=1, column=4, pady=(40,0))
label.config(width=30)
label.config(font=("Courier",44,'underline'))

# main file
label_main = tk.Label(tab1, text = "Main File")
label_main.grid(row=3, column=2,pady=(50,5))
label_main.config(font=("Courier",15))

label_main = tk.Label(tab1, text = "File Selected : ")
label_main.grid(row=5, column=2,padx=5,pady=(10,0))
label_main.config(font=("Courier",10))
pathoffile=" "
ent = tk.Entry(tab1, textvariable=path_of_file,width=70)
ent.grid(row=5, column=3, pady=(10,0), padx=(5,0))

open_button_main = tk.Button(tab1, text="select file", command=open_file) # open file fn used here
open_button_main.grid(row=4, column=2)

refresh_button_main = tk.Button(tab1, text="Refresh file", command=refresh_file)  # refresh file fn used here
refresh_button_main.grid(row=4, column=3)


# stats
stats_button = tk.Button(tab1, text="Calculate stats", command= calc, font=custom_font) # calc fn used here
stats_button.grid(row=6, column=2, pady=(50,5), padx=(20,0))

tk.Label(tab1, text="Most frequent word : ").grid(row=7, column=2)
entry_most = tk.Entry(tab1, textvariable=word_most)
entry_most.grid(row=7, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="Least frequent word : ").grid(row=8, column=2)
entry_least = tk.Entry(tab1, textvariable=word_least)
entry_least.grid(row=8, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="No. of sentence : ").grid(row=9, column=2)
entry_ct_sentence = tk.Entry(tab1, textvariable=count_sentence)
entry_ct_sentence.grid(row=9, column=3, pady=(0,5), padx=(20,0))

tk.Label(tab1, text="No. of words : ").grid(row=10, column=2)
entry_ct_words = tk.Entry(tab1, textvariable=count_words)
entry_ct_words.grid(row=10, column=3, pady=(0,5), padx=(20,0))

#tk.Label(window, text="field").grid(row=11, column=3)

def extract_data(debug=False):

    main_file_path = main_file.get()   # file path of selected file
    if debug: print("File path is-",main_file_path)

    keyword_file_path = keyword_file.get()
    if debug: print("Keyword file path -", keyword_file_path)

    keywords = API.extractKeywords(keyword_file_path)
    if debug: print("Keywords: ", keywords)

    sentences = API.extractSentences(main_file_path)
    if debug: print("sentences: ", sentences)

    kwrd_sent_map = API.keywordMapper(sentences, keywords)
    if debug: print("Keywords-Sentences-Map: ", kwrd_sent_map)


    text_box.delete('1.0',tk.END)

    for kwrds, sentences in kwrd_sent_map.items():
        for sentence in sentences:
            text_box.insert(tk.END, sentence+"\n")
        text_box.insert(tk.END, "\n")
        text_box.highlight_pattern(kwrds, "highlight")
        indow, textvariable=variable_to_set
#x.grid(row=11, column=4)
def refresh_file_tab2():
    extract_data()
    print("Tab2 refresh")

# histogram
graph_button = tk.Button(tab1, text="Frequency Graph", command=freq_graph, font=custom_font)
graph_button.grid(row=13, column=2, pady=(50,0), padx=(20,0))


#tab-2
# keyword file
label_key = tk.Label(tab2, text = "Keywords")
label_key.grid(row=15, column=2, pady=(80,5), padx=(10,0))
label_key.config(font=("Courier",20))
label_key2 = tk.Label(tab2, text = "-   File")
label_key2.grid(row=15, column=3,pady=(80,5))
label_key2.config(font=("Courier",20))

open_button_key = tk.Button(tab2, text="select file", command=lambda: open_file(is_keyword_file=True))  # open file fn used here
open_button_key.grid(row=16, column=2)

label_main = tk.Label(tab2, text = "File Selected : ")
label_main.grid(row=17, column=2,padx=5,pady=(10,0))
label_main.config(font=("Courier",10))
pathoffile=" "
ent = tk.Entry(tab2, textvariable=path_of_file2,width=70)
ent.grid(row=17, column=3, pady=(10,0), padx=(5,0))

refresh_button_key = tk.Button(tab2, text="Refresh file", command=refresh_file_tab2)   # refresh file fn used here
refresh_button_key.grid(row=16, column=3)


#show sentences with keywords
extract_button = tk.Button(tab2, text="Get lines", command= lambda: extract_data(debug=True), font=custom_font)
extract_button.grid(row=18,column=3, pady=(40,5))
label_show = tk.Label(tab2, text="Sentences with keywords:- ")
label_show.grid(row=19, column=3)
text_box = CustomText(tab2, height=50, width=100)
text_box.grid(row=20,column=4)
text_box.tag_configure("highlight", foreground="red", background="black")



#-------------show------------
window.mainloop()
