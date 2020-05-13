# NetmusicDownload
通过Python下载网易云音乐歌手页面的歌曲

根据```Tkinter```生成的GUI图形化操作

---

# 使用方法

1. >pip install -r [requirements.txt](https://github.com/yanlc39/NetmusicDownload/blob/master/requirements.txt)

   安装所需依赖文件

2. >python main.py

   启动

3. 打开网易云音乐，将歌手页面的URL粘入文本框中，点击获取列表可得到曲目列表，选中所   	     需下载音乐点开始下载即下载到```music```文件夹中









# 已知缺陷

1. 付费音乐接口不正确，无法正常播放
2. 无删除缓存功能，需要再次启动才可下载另一位歌手的音乐
3. 下载的音乐比特率仅为```128kbps```
4. 没有进度条以及友好的用户提示