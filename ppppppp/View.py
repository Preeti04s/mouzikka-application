import random
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox,filedialog
import MyExceptions
from pygame import mixer
import threading
import musicplayer_support
from Player import Player
import tkinter.messagebox
import time
from cx_Oracle import DatabaseError

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top=View(root)
    musicplayer_support.init(root,top)
    root.resizable(False, False)
    root.mainloop()

class View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Avenir Next Cyr Medium} -size 23 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
        font12 = "-family {Avenir Next Cyr} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Mistral} -size 34 -weight " \
                 "bold -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("687x526+558+155")
        top.configure(background="#fff")
        self.top=top
        self.songName = tk.Label(top)
        self.songName.place(relx=0.437, rely=0.038, height=44, width=281)
        self.songName.configure(background="#fff")
        self.songName.configure(disabledforeground="#a3a3a3")
        self.songName.configure(font=font13)
        self.songName.configure(foreground="#000000")
        self.songName.configure(text='''MOUZIKKA''')
        self.var=tk.DoubleVar()
        self.songProgress = ttk.Scale(top,orient="horizontal")

        self.songProgress.place(relx=0.393, rely=0.209, relwidth=0.495
                , relheight=0.0, height=7)


        self.songTotalDuration = ttk.Label(top)
        self.songTotalDuration.place(relx=0.844, rely=0.171, height=19, width=29)

        self.songTotalDuration.configure(background="#fff")
        self.songTotalDuration.configure(foreground="#3399ff")
        self.songTotalDuration.configure(font=font12)
        self.songTotalDuration.configure(relief='flat')


        self.songTimePassed = ttk.Label(top)
        self.songTimePassed.place(relx=0.393, rely=0.171, height=19, width=29)
        self.songTimePassed.configure(background="#ffffff")
        self.songTimePassed.configure(foreground="#000000")
        self.songTimePassed.configure(font=font12)
        self.songTimePassed.configure(relief='flat')


        self.pauseButton = tk.Button(top)
        self.pauseButton.place(relx=0.568, rely=0.266, height=34, width=34)
        self.pauseButton.configure(activebackground="#ececec")
        self.pauseButton.configure(activeforeground="#000000")
        self.pauseButton.configure(background="#fff")
        self.pauseButton.configure(borderwidth="0")
        self.pauseButton.configure(disabledforeground="#a3a3a3")
        self.pauseButton.configure(foreground="#000000")
        self.pauseButton.configure(highlightbackground="#d9d9d9")
        self.pauseButton.configure(highlightcolor="black")
        self._img1 = tk.PhotoImage(file="./icons/pause.png")
        self.pauseButton.configure(image=self._img1)
        self.pauseButton.configure(pady="0")
        self.pauseButton.configure(text='''Button''')

        self.playButton = tk.Button(top)
        self.playButton.place(relx=0.64, rely=0.266, height=34, width=34)
        self.playButton.configure(activebackground="#ececec")
        self.playButton.configure(activeforeground="#000000")
        self.playButton.configure(background="#fff")
        self.playButton.configure(borderwidth="0")
        self.playButton.configure(disabledforeground="#a3a3a3")
        self.playButton.configure(foreground="#000000")
        self.playButton.configure(highlightbackground="#d9d9d9")
        self.playButton.configure(highlightcolor="black")
        self._img2 = tk.PhotoImage(file="./icons/play.png")
        self.playButton.configure(image=self._img2)
        self.playButton.configure(pady="0")
        self.playButton.configure(text='''Button''')

        self.stopButton = tk.Button(top)
        self.stopButton.place(relx=0.713, rely=0.266, height=34, width=34)
        self.stopButton.configure(activebackground="#ececec")
        self.stopButton.configure(activeforeground="#000000")
        self.stopButton.configure(background="#fff")
        self.stopButton.configure(borderwidth="0")
        self.stopButton.configure(disabledforeground="#a3a3a3")
        self.stopButton.configure(foreground="#000000")
        self.stopButton.configure(highlightbackground="#d9d9d9")
        self.stopButton.configure(highlightcolor="black")
        self._img3 = tk.PhotoImage(file="./icons/stop.png")
        self.stopButton.configure(image=self._img3)
        self.stopButton.configure(pady="0")
        self.stopButton.configure(text='''Button''')

        self.vinylRecordImage = tk.Label(top)
        self.vinylRecordImage.place(relx=0.0, rely=0.0, height=204, width=204)
        self.vinylRecordImage.configure(background="#d9d9d9")
        self.vinylRecordImage.configure(disabledforeground="#a3a3a3")
        self.vinylRecordImage.configure(foreground="#000000")
        self._img4 = tk.PhotoImage(file="./icons/vinylRecord.PNG")
        self.vinylRecordImage.configure(image=self._img4)
        self.vinylRecordImage.configure(text='''Label''')

        self.playList = ScrolledListBox(top)
        self.playList.place(relx=0.0, rely=0.38, relheight=0.532, relwidth=0.999)

        self.playList.configure(background="white")
        self.playList.configure(disabledforeground="#a3a3a3")
        self.playList.configure(font="TkFixedFont")
        self.playList.configure(foreground="black")
        self.playList.configure(highlightbackground="#d9d9d9")
        self.playList.configure(highlightcolor="#d9d9d9")
        self.playList.configure(selectbackground="#c4c4c4")
        self.playList.configure(selectforeground="black")
        self.playList.configure(width=10)

        self.previousButton = tk.Button(top)
        self.previousButton.place(relx=0.509, rely=0.285, height=16, width=16)
        self.previousButton.configure(background="#fff")
        self.previousButton.configure(borderwidth="0")
        self.previousButton.configure(disabledforeground="#a3a3a3")
        self.previousButton.configure(foreground="#000000")
        self._img5 = tk.PhotoImage(file="./icons/previous.png")
        self.previousButton.configure(image=self._img5)
        self.previousButton.configure(text='''Label''')

        self.bottomBar = ttk.Label(top)
        self.bottomBar.place(relx=0.0, rely=0.913, height=49, width=686)
        self.bottomBar.configure(background="#d9d9d9")
        self.bottomBar.configure(foreground="#000000")
        self.bottomBar.configure(font="TkDefaultFont")
        self.bottomBar.configure(relief='flat')
        self.bottomBar.configure(width=686)
        self.bottomBar.configure(state='disabled')

        self.vol_scale = ttk.Scale(top)
        self.vol_scale.place(relx=0.015, rely=0.932, relwidth=0.146, relheight=0.0
                , height=26, bordermode='ignore')
        self.vol_scale.configure(takefocus="")

        self.addSongsToPlayListButton = tk.Button(top)
        self.addSongsToPlayListButton.place(relx=0.961, rely=0.323, height=17
                , width=17)
        self.addSongsToPlayListButton.configure(activebackground="#ececec")
        self.addSongsToPlayListButton.configure(activeforeground="#d9d9d9")
        self.addSongsToPlayListButton.configure(background="#fff")
        self.addSongsToPlayListButton.configure(borderwidth="0")
        self.addSongsToPlayListButton.configure(disabledforeground="#a3a3a3")
        self.addSongsToPlayListButton.configure(foreground="#000000")
        self.addSongsToPlayListButton.configure(highlightbackground="#d9d9d9")
        self.addSongsToPlayListButton.configure(highlightcolor="black")
        self._img6 = tk.PhotoImage(file="./icons/add.png")
        self.addSongsToPlayListButton.configure(image=self._img6)
        self.addSongsToPlayListButton.configure(pady="0")
        self.addSongsToPlayListButton.configure(text='''Button''')

        self.deleteSongsFromPlaylistButton = tk.Button(top)
        self.deleteSongsFromPlaylistButton.place(relx=0.917, rely=0.323
                , height=18, width=18)
        self.deleteSongsFromPlaylistButton.configure(activebackground="#ececec")
        self.deleteSongsFromPlaylistButton.configure(activeforeground="#000000")
        self.deleteSongsFromPlaylistButton.configure(background="#fff")
        self.deleteSongsFromPlaylistButton.configure(borderwidth="0")
        self.deleteSongsFromPlaylistButton.configure(disabledforeground="#a3a3a3")
        self.deleteSongsFromPlaylistButton.configure(foreground="#000000")
        self.deleteSongsFromPlaylistButton.configure(highlightbackground="#d9d9d9")
        self.deleteSongsFromPlaylistButton.configure(highlightcolor="black")
        self._img7 = tk.PhotoImage(file="./icons/delete.png")
        self.deleteSongsFromPlaylistButton.configure(image=self._img7)
        self.deleteSongsFromPlaylistButton.configure(pady="0")
        self.deleteSongsFromPlaylistButton.configure(text='''Button''')

        self.addFavourite = tk.Button(top)
        self.addFavourite.place(relx=0.932, rely=0.913, height=42, width=42)
        self.addFavourite.configure(activebackground="#ececec")
        self.addFavourite.configure(activeforeground="#000000")
        self.addFavourite.configure(background="#d9d9d9")
        self.addFavourite.configure(borderwidth="0")
        self.addFavourite.configure(disabledforeground="#a3a3a3")
        self.addFavourite.configure(foreground="#000000")
        self.addFavourite.configure(highlightbackground="#d9d9d9")
        self.addFavourite.configure(highlightcolor="black")
        self._img8 = tk.PhotoImage(file="./icons/like.png")
        self.addFavourite.configure(image=self._img8)
        self.addFavourite.configure(pady="0")
        self.addFavourite.configure(text='''Button''')
        self.addFavourite.configure(width=42)

        self.removeFavourite = tk.Button(top)
        self.removeFavourite.place(relx=0.873, rely=0.913, height=42, width=42)
        self.removeFavourite.configure(activebackground="#ececec")
        self.removeFavourite.configure(activeforeground="#000000")
        self.removeFavourite.configure(background="#d9d9d9")
        self.removeFavourite.configure(borderwidth="0")
        self.removeFavourite.configure(disabledforeground="#a3a3a3")
        self.removeFavourite.configure(foreground="#000000")
        self.removeFavourite.configure(highlightbackground="#d9d9d9")
        self.removeFavourite.configure(highlightcolor="black")
        self._img9 = tk.PhotoImage(file="./icons/not_favorite.png")
        self.removeFavourite.configure(image=self._img9)
        self.removeFavourite.configure(pady="0")
        self.removeFavourite.configure(text='''Button''')
        self.removeFavourite.configure(width=48)

        self.loadFavourite = tk.Button(top)
        self.loadFavourite.place(relx=0.83, rely=0.932, height=26, width=26)
        self.loadFavourite.configure(activebackground="#ececec")
        self.loadFavourite.configure(activeforeground="#000000")
        self.loadFavourite.configure(background="#d9d9d9")
        self.loadFavourite.configure(borderwidth="0")
        self.loadFavourite.configure(disabledforeground="#a3a3a3")
        self.loadFavourite.configure(foreground="#000000")
        self.loadFavourite.configure(highlightbackground="#d9d9d9")
        self.loadFavourite.configure(highlightcolor="black")
        self._img10 = tk.PhotoImage(file="./icons/refresh.png")
        self.loadFavourite.configure(image=self._img10)
        self.loadFavourite.configure(pady="0")
        self.loadFavourite.configure(text='''Button''')
        icon=tk.PhotoImage(file="./icons/vinylrecord.png")
        root.iconphoto(root,icon)
        root.title("MOUZIKKA-DANCE TO THE RHYTHM OF YOUR HEART")
        self.player=Player()

        try:

            if self.player.get_db_status()==True:
                messagebox.showinfo("Success!!","Successfully connected to the database!!")
            else:
                raise Exception("Sorry!You can't save or load favourites!!")
        except Exception as ex:
            messagebox.showinfo("DB Error!",ex)
            self.loadFavourite.config(status="disabled")
            self.addFavourite.config(status="disabled")
            self.removeFavourite.config(status="disabled")
        self.vol_scale.config(from_=0, to=100, command=self.change_vol)
        self.vol_scale.set(50)
        self.loadFavourite.config(command=self.load_favourites)
        self.removeFavourite.config(command=self.remove_favourites)
        self.addFavourite.config(command=self.add_favourites)
        self.playList.config(font="Vivaldi 12")
        self.playList.bind("<Double-1>", self.list_double_click)
        self.addSongsToPlayListButton.config(command=self.add_songs)
        self.deleteSongsFromPlaylistButton.config(command=self.delete_song)
        self.previousButton.config(command=self.play_previous)

        self.playButton.config(command=self.play_song)
        self.pauseButton.config(command=self.pause_song)
        self.stopButton.config(command=self.stop_song)
        self.isPlaying = False
        self.isPaused = False
        root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.my_thread = None
        self.isThreadRunning = False
        self.stopThread = False



    def change_vol(self,vol):
        vol_level=float(vol)/100
        self.player.set_volume(vol_level)



    def load_favourites(self):
        try:
            load_result = self.player.load_song_from_favourites()
            result = load_result[0]
            if result.find("No songs present") != -1:
                messagebox.showinfo("Favourites Empty!!!", "No songs in your favourites")
                return
            song_dict = load_result[1]
            self.playList.delete(0, tk.END)
            for song_name in song_dict:
                self.playList.insert(tk.END, song_name)
                print("from db:", song_name)
            rcolor = lambda: random.randint(0, 255)
            red = hex(rcolor())
            green = hex(rcolor())
            blue = hex(rcolor())
            mycolor = "#" + red[2:3] + green[2:3] + blue[2:3]
            self.playList.configure(fg=mycolor)
            messagebox.showinfo("Success!!!", "List populated from your favourites!!!")

        except(DatabaseError)as ex1:
            messagebox.showerror("DB Error!", "Sorry! songs cannot be loaded from favourites!!!")

    def remove_favourites(self):
        song_name_tuple=self.playList.curselection()
        try:
            if len(song_name_tuple)==0:
                raise MyExceptions.NoSongSelectedError
            song_name=self.playList.get(song_name_tuple[0])
            str_removed=self.player.remove_song_from_favourites(song_name)
            if str_removed.startswith("Songs"):
                messagebox.showerror("Can't load favourites!",str_removed)
            else:
                messagebox.showinfo("Loaded!!",str_removed)
        except MyExceptions.NoSongSelectedError as ex1:
            messagebox.showerror("Error!!","Select a song first")
        except DatabaseError as ex2:
            messagebox.showerror("Error!!","Song cannot be removed!!")



    def add_favourites(self):
        try:
            fav_song_sel_tuple=self.playList.curselection()
            if len(fav_song_sel_tuple)==0:
                raise MyExceptions.NoSongSelectedError
            song_name=self.playList.get(fav_song_sel_tuple[0])
            result=self.player.add_song_to_favourites(song_name)
            messagebox.showinfo("Success!!",result)
        except MyExceptions.NoSongSelectedError as ex1:
            messagebox.showerror("Error!!","Select a song first")
        except DatabaseError as ex2:
            messagebox.showerror("Error!!","Song cannot be added!!")

    def list_double_click(self,e):
        self.play_song()

    def add_songs(self):
        song_list=self.player.add_songs()
        if song_list is None: return
        for song_name in song_list:
            self.playList.insert(tk.END,song_name)
        rcolor = lambda: random.randint(0, 255)
        red = hex(rcolor())
        green = hex(rcolor())
        blue = hex(rcolor())
        red = red[2:]
        green = green[2:]
        blue = blue[2:]
        if len(red) == 1:
            red = "0" + red
        if len(green) == 1:
            green = "0" + green
        if len(blue) == 1:
            blue = "0" + blue
        mycolor = "#" + red + green + blue
        self.playList.configure(fg=mycolor)

    def delete_song(self):
        self.sel_song_index_tuple = self.playList.curselection()
        try:
            if len(self.sel_song_index_tuple) == 0:
                raise MyExceptions.NoSongSelectedError("Please select a song to be removed!!")
            song_name=self.playList.get(self.sel_song_index_tuple[0])
            self.player.remove_song(song_name)
            self.playList.delete(self.sel_song_index_tuple[0])
        except MyExceptions.NoSongSelectedError as ex1:
            messagebox.showerror("Song not selected",ex1)


    def play_previous(self):
        try:
            if hasattr(self,"sel_song_index_tuple")==False:
                raise MyExceptions.NoSongSelectedError("Please select a song!")
            self.prev_song_index=self.sel_song_index_tuple[0]-1
            if self.prev_song_index==-1:
                self.prev_song_index=self.player.get_song_count()-1
            self.playList.select_clear(0,tk.END)
            self.playList.selection_set(self.prev_song_index)
            #self.isThreadRunning=False
            self.play_song()
        except MyExceptions.NoSongSelectedError as ex1:
            messagebox.showerror("Error!",ex1)

    def play_song(self):
        self.sel_song_index_tuple=self.playList.curselection()
        try:
            if len(self.sel_song_index_tuple)==0:
                raise MyExceptions.NoSongSelectedError("Please select a song to play!!")
            self.stop_song()
            self.song_name = self.playList.get(self.sel_song_index_tuple [0])
            self.show_song_details()
            self.change_vol(self.vol_scale.get())
            self.stopThread
            self.player.play_song()
            s=self.song_length
            self.songProgress.set(0)

            self.setup_thread()
        except MyExceptions.NoSongSelectedError as ex1:
            messagebox.showinfo("Song Not selected",ex1)

    def pause_song(self):
        if self.isPlaying==True:
            if self.isPaused == False:
                self.player.pause_song()
                self.isPaused = True
            else:
                self.player.unpause_song()
                self.isPaused = False

    def stop_song(self):

            self.player.stop_song()
            self.stopThread=True

            self.isPlaying = False



    def ask_quit(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit now?"):
            self.player.close_player()
            messagebox.showinfo("Have a great day!","Thank you for using this app...")
            root.destroy()

    def show_song_details(self):
        self.song_length=self.player.get_song_length(self.song_name)

        min,sec=divmod(self.song_length,60)
        min=round(min)
        sec=round(sec)
        self.songTotalDuration.config(text=str(min)+":"+str(sec))
        self.songTimePassed.config(text="0:0")
        dot_index=self.song_name.rfind(".")
        print(type(dot_index))
        song_name_str=self.song_name[0:dot_index]
        if len(song_name_str)>14: song_name_str=song_name_str[0:14]+"..."
        self.songName.config(text=song_name_str)

    def show_timer(self, total_sec):
        self.curr_sec = 0
        self.stopThread = False
        while self.curr_sec <= total_sec:
            self.songProgress.config(from_=0,to=total_sec,command=self.slide_slide)
            self.songProgress.set(self.curr_sec)
            min, sec = divmod(self.curr_sec, 60)
            self.songTimePassed.configure(text=str(min) + ":" + str(sec))
            time.sleep(1)
            self.curr_sec += 1
            while self.isPaused == True:
                time.sleep(1)
            if self.stopThread == True:
                return

    def setup_thread(self):
        self.my_thread = threading.Thread(target=self.show_timer, args=(self.song_length,))
        self.isPlaying = True
        self.isThreadRunning = True
        self.my_thread.start()

    def slide_slide(self, e):
        value = self.songProgress.get()
        self.curr_sec = int(value)
        mixer.music.load(self.player.mymodel.get_song_path(self.song_name))
        mixer.music.play(loops=0, start=self.curr_sec)


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()






