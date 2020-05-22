# name: music.py
__author__ = "xush2014@hotmail.com"

# -*-coding:utf-8-*-a

from tkinter import *
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


class NetMusicGUI(object):
    def __init__(self):
        self.header = {
            'Host': 'music.163.com',
            'Referer': 'https://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',

        }
        root = Tk()
        root.title('网易云音乐   --Made by Yanlc')
        root.geometry('800x600+520+220')
        label = Label(root, text='输入歌手页面地址：', font=('微软雅黑', 23))
        label.grid(row=0, column=0)
        self.url = ''
        self.downloading = 0
        self.music_dict = {}
        self.music_list = {}
        self.entry = Entry(root, font=('微软雅黑', 23), width=25)
        self.entry.grid(row=0, column=1)
        self.text = Listbox(root, font=('微软雅黑', 23), width=40, height=11, selectmode='extended')
        self.text.grid(row=1, columnspan=2)
        button1 = Button(root, text='获取曲目列表', font=('微软雅黑', 20), command=self.getList)
        button1.grid(row=2, column=0, sticky=W)
        button2 = Button(root, text='开始下载', font=('微软雅黑', 20), command=self.downloadMusic)
        button2.grid(row=2, column=1, sticky=W)

        root.mainloop()

    def downloadMusic(self):
        need_song = self.text.curselection()[0]
        # print(need_song)
        result = requests.get(self.url, headers=self.header)
        r = BeautifulSoup(result.text, 'html.parser')
        songID = self.music_list[need_song]
        singer = r.find('title').text.strip(' - 歌手 - 网易云音乐')
        songDownload_Url = 'http://music.163.com/song/media/outer/url?id=' + songID
        path = 'music\\' + self.music_dict[songID] + ' - ' + singer + '.mp3'
        urlretrieve(songDownload_Url, path, self.loading)
        downPercent = Tk()
        downPercent.title('下载进度---' + self.music_dict[songID]+' - '+singer+'.mp3')
        song_Str = self.music_dict[songID]+' - '+singer+'.mp3'
        downPercent.geometry('1212x520+700+400')
        downLabel = Label(downPercent, text=song_Str+':'+'已经下载:{}'.format(self.downloading), font=('微软雅黑', 23))
        downLabel.grid(row=0, column=0)

    def getList(self):
        self.text.delete(0, END)
        self.music_list = {}
        self.music_dict = {}
        self.url = self.entry.get().replace('/#', '')
        result = requests.get(self.url, headers=self.header)
        r = BeautifulSoup(result.text, 'html.parser')
        songID = r.find('ul', {'class', 'f-hide'}).find_all('a')
        singer = r.find('title').text.strip(' - 歌手 - 网易云音乐')
        self.text.insert(END, "歌手：" + singer)
        x = 1
        for music in songID:
            music_id = music.get('href').strip('/song?id=')
            music_name = music.text
            self.music_dict[music_id] = music_name
            self.music_list[x] = music_id
            x = x + 1
            self.text.insert(END, music_name)
            self.text.see(END)
            self.text.update()

    def loading(self, blocknum, blocksize, totalsize):
        percent = 100.0 * blocknum * blocksize / totalsize
        if percent > 100:
            percent = 100
        self.downloading = '%.2f%%' % percent


if __name__ == '__main__':
    netMusic = NetMusicGUI()
