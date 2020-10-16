import tkinter as tk

#------designing main tinker window-------
GUI=tk.Tk()
'''
widget section starts
'''

GUI.title("Text-Statistics")
button = tk.Button(GUI, text="Close", width=100, command=GUI.destroy) 
button.grid()

'''
widget section ends
'''
#------running tinker main window --------
GUI.mainloop()