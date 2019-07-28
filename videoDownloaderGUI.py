from tkinter import *
#from tkinter.ttk import Progressbar
import videoDownloader as vd # main downloader
from urllib.request import urlopen # for image thumbnail
master = Tk()
master.title('Download')
def getLink():
    down = Tk()
    down.title('Download File')
    down.geometry('1000x720')
    text = linkEntry.get()
    download_btn = Button(down, text = 'Download Video', command = vd.downloadFile(text), fg = 'red')
    down_label = Label(down, text = 'Download quality = 720p, mp4 Video', fg = 'blue')
    lb = Label(down, text = vd.showVideoName(text), fg = 'blue')
    lb.pack()
    down_label.pack()
    exitB = Button(down, text = 'Quit', command = down.destroy, fg = 'red' , bg = 'cyan')
    exitB.pack()
    download_btn.pack(pady = 10)
    

    
master.geometry('300x300')
label1 = Label(master, text = 'Enter link of the video', fg = 'red')
linkEntry = Entry(master, bd = 4)
enterB = Button(master, text = 'Enter Link', command = getLink, fg = 'red', bg = 'cyan')
exitB = Button(master, text = 'Quit', command = master.destroy, fg = 'red' , bg = 'cyan')
label1.pack()
linkEntry.pack()
enterB.pack(pady = 10)
exitB.pack(pady = 5)
master.mainloop()
