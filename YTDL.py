#Packages
import tkinter as tk
from pytube import YouTube

def start_gui():
    #Creating a Window
    top = tk.Tk()

    # For changing the title of the title bar
    top.title("Youtube Downloader")

    #Placing a Text
    label = tk.Label(text= "Hello, User")
    label.pack()

    #Entry Label
    label2 = tk.Label(text= "Enter Youtube Link Here")
    label2.pack()

    entry = tk.Entry(fg="yellow", bg="black", width=50)
    entry.pack()

    #Location Label
    label3 = tk.Label(text= "Enter Video Destination Here")
    label3.pack()

    location = tk.Entry(fg="yellow", bg="black", width=50)
    location.pack()

    #Note
    label4 = tk.Label(fg="red", text = "Note: Preferred Location is a place like the *Documents Folder*.")
    label4.pack()
    label5 = tk.Label(fg="red", text = "Windows might block it otherwise becaue of OS Permissions.")
    label5.pack()


    # command
    def get_video_url():
        Link = entry.get()
        Directory = location.get()
        yt = YouTube(Link)
        #Title of video
        x = ("Title: ",yt.title)
        label6 = tk.Label(text = x)
        label6.pack()
        #Number of views of video
        y = ("Number of views: ",yt.views)
        label7 = tk.Label(text = y)
        label7.pack()
        #Length of the Video
        z = ("Length of the Video: ", yt.length, "seconds")
        label8 = tk.Label(text = z)
        label8.pack()

        def high():
            ys = yt.streams.get_highest_resolution()
            ys.download(Directory)
            labelA = tk.Label(fg="green", text = "Download Complete!")
            labelA.pack()

        #Placing a button to Download the Highest Quality
        HQ = tk.Button(text = "High Quality", command = high)
        HQ.pack()

        def low():
            ys = yt.streams.get_lowest_resolution()
            ys.download(Directory)
            labelB = tk.Label(fg="green", text = "Download Complete!")
            labelB.pack()

        #Placing a button to Download the Lowest Quality
        LQ = tk.Button(text = "Low Quality", command = low)
        LQ.pack()

    #Placing the Download Button
    button = tk.Button(text = "Download", command = get_video_url)
    button.pack()

    def restart_gui():
        top.destroy()
        start_gui()

    #Placing a Restart Button
    restart = tk.Button(text = "Restart", command = restart_gui)
    restart.pack()
    label9 = tk.Label(fg="blue", text = "(Click restart after every download to download another video)")
    label9.pack()

    #Set window size
    top.geometry("550x450")
    top.mainloop()

start_gui()
