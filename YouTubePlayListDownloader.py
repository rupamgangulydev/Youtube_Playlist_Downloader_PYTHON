from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import youtube_dl
import sys
import webbrowser
import os
import threading
import subprocess
url = "https://github.com/rupamgangulydev"
new = 1
font=('Verdana', 15, 'bold')
folderName=""
fileSize=0
maxFileSize=0
def openweb():
    webbrowser.open(url,new=new)
def on_enter(e):
    Btn['foreground'] = 'green'

def on_leave(e):
    Btn['foreground'] = 'black'

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
# the_menu.add_command(label="Select")
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    # the_menu.entryconfigure("Select",command=lambda:
    w.event_generate("<<Select>>")
    the_menu.entryconfigure("Cut",command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",command=lambda:
    w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

        
def my_hook(d):
    if d['status']=='finshed':
        fileTuple=os.path.split(os.path.abspath(d['filename']))
        resultOutput.config(text="Done Downloading{}".format(fileTuple[1]))
    if d['status']=='downloading':
        file_name=os.path.split(os.path.abspath(d['filename']))
        namevar=file_name[1],
        resultOutput.config(text=namevar)
        resultOutputPercent.config(text="Percenrage- "+d['_percent_str'])
        resultOutputEstimateTime.config(text="Estimation Time- "+d['_eta_str']+"    Speed- "+d['_speed_str'])
def openDirectory():
    global folderName
    folderName=filedialog.askdirectory()
    if(len(folderName)>1):
        errorMsz2.configure(text=folderName)
    else:
        errorMsz2.configure(text="Please Select Folder Path")

def downloaderFiles():
    ProgressMsz.config(text=" ...Process Started... ",font=('Verdana', 15, 'bold'),bg="white")
    str=folderName+'/%(title)s-%(id)s.%(ext)s'
    urlEnt=urlEnrty.get()
    if(len(urlEnt)>1):
        subprocess.run(['explorer', os.path.realpath(folderName)])
        ydl_opts = {
            'outtmpl': str,
            'progress_hooks': [my_hook],
        }
        print(ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlEnt])     
        ProgressMsz.config(text="COMPLETED",font=('Verdana', 15, 'bold'),bg="white")

def threadCallingDownloadFiles():
    th=threading.Thread(target=downloaderFiles)
    th.start()

root= Tk()
root.geometry("640x540") #Width x Height
root.configure(bg='white')
root.title("Youtube PlayList Downloader")
root.option_add("*TCombobox*Listbox*Font",font )
root.grid_columnconfigure(0, weight=1)
root.resizable(False, False)
make_menu(root)
labe1=Label(root,text=" Paste Playlist's or Single video's URL here",font=('Verdana', 15) ,bg="white")
labe1.grid(padx=10, pady=5)

urlVar=StringVar()
urlEnrty=Entry(root, textvariable=urlVar,font=('Verdana', 12),width=100,fg="black",bd=1,borderwidth=2)
urlEnrty.grid(padx=40, pady=5)
urlEnrty.bind_class("Entry", "<ButtonRelease-3>", show_menu)

label2=Label(root, text="Choose where to Download the Videoes: ",font=('Verdana', 10), bg="white")
label2.grid(padx=10, pady=5)

button1=Button(root, bg='#2bedb0',fg="black", text="BROWSE",font=('Verdana', 15, 'bold'),command=openDirectory)
button1.grid(padx=10, pady=5,)

errorMsz2=Label(root, text="",bg="white")
errorMsz2.grid(padx=10, pady=5)


button2=Button(root,bg='#2bedb0',fg="black", text="Download",height = 0,width = 0,font=('Verdana', 25, 'bold'),command=threadCallingDownloadFiles)
button2.grid(padx=10, pady=5)

ProgressMsz1=Label(text="If Somehow Download Process Interupted then again Click Download Button to Resume",font=('Verdana', 10),bg="white")
ProgressMsz1.grid(padx=10)


resultOutput=Label(root,text="",font=('Verdana', 10, 'bold'),bg="white", wraplength=500)
resultOutput.grid(padx=10,pady=5)

resultOutputPercent=Label(root,text="",font=('Verdana', 10, 'bold'),bg="white")
resultOutputPercent.grid(padx=10,pady=5)

resultOutputEstimateTime=Label(root,text="",font=('Verdana', 10, 'bold'),bg="white")
resultOutputEstimateTime.grid(padx=10,pady=5)

ProgressMsz=Label(text="...............",font=('Verdana', 10, 'bold'),bg="white")
ProgressMsz.grid(padx=10)
devby=Label(root,text=" Developed by Rupam Ganguly ",bg="black",fg="white",font=('Verdana', 10, 'bold'))
devby.grid()
Btn = Button(root, text = "https://github.com/rupamgangulydev",command=openweb,borderwidth=0, bg="white")
Btn.grid(pady=5)
Btn.bind("<Enter>", on_enter)
Btn.bind("<Leave>", on_leave)

root.mainloop()
sys.exit()