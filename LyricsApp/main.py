import tkinter as tk
import getSpotifyCurrentTrack
import getLyrics
import rumps
import urllib.request


songInfo = None
songName = None
artistName = None
lyrics = None
lyricsList = None
listbox = None

def check_internet():
    try:
        urllib.request.urlopen('http://google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        return False


def reloadList():
    global songInfo, songName, artistName, lyrics, lyricsList, listbox
    if getSpotifyCurrentTrack.confirmRunning():
        if songInfo != getSpotifyCurrentTrack.getInfo():
            songInfo = getSpotifyCurrentTrack.getInfo()
            songName = songInfo[0]
            artistName = songInfo[1]
            if check_internet():
                lyrics = getLyrics.getLyrics(artistName=artistName, songName=songName)
                if lyrics == None:
                    lyricsList = ("すいません。歌詞が登録されていません。")
                else:
                    lyricsList = lyrics.split("\n")
            else:
                lyricsList = ("インターネットに接続されていません。接続を確認してください。")
            listbox = tk.Listbox(
                root,
                width=70,
                height=30,
                font=("Helvetica", 14),
                listvariable=tk.StringVar(value=lyricsList)
            )
            listbox.grid(row=0, column=0)

    else:
        lyricsList = ("Spotifyアプリが起動していません。")
        songInfo = None
        listbox = tk.Listbox(
            root,
            width=70,
            height=30,
            font=("Helvetica", 14),
            listvariable=tk.StringVar(value=lyricsList)
        )
        listbox.grid(row=0, column=0)


class rumpsApp(rumps.App):
    @rumps.clicked("ウィンドウを常に前面にする")
    def toggleTopBool(self, sender):
        # メニューにチェックマークをつける
        sender.state = not sender.state
        root.wm_attributes("-topmost", sender.state)
        root.mainloop()

    @rumps.clicked("リロード")
    def reload(self, sender):
        reloadList()
if getSpotifyCurrentTrack.confirmRunning():
    songInfo = getSpotifyCurrentTrack.getInfo()
    songName = songInfo[0]
    artistName = songInfo[1]
    # エラー処理
    if check_internet():
        lyrics = getLyrics.getLyrics(artistName=artistName, songName=songName)
        if lyrics is None:
            lyricsList = ("すいません。歌詞が登録されていません。")
        else:
            lyricsList = lyrics.split("\n")
    else:
        lyricsList = ("インターネットに接続されていません。接続を確認してください。")
else:
    lyricsList = ("Spotifyアプリが起動されていません。")

root = tk.Tk()
# Hide the root window drag bar and close button
root.overrideredirect(True)

root.wm_attributes("-topmost", True)
# Turn off the window shadow
root.wm_attributes("-transparent", True)
# Set the root window background color to a transparent color
root.config(bg='systemTransparent')

root.geometry("564x570")

# ListBoxの定義
listbox = tk.Listbox(
    root,
    width=70,
    height=30,
    font=("Helvetica", 14),
    listvariable=tk.StringVar(value=lyricsList)
)

listbox.grid(row=0, column=0)

ybar = tk.Scrollbar(
    root,  # 親ウィジェット
    orient=tk.VERTICAL,  # バーの方向
)

rumpsApp("Lyricspot").run()
root.mainloop()
