# subs-naming-fix

Little Python script specially designed to fix subtitles and video files naming for TV shows and movie fans.

To run it, when located in the same directory as the .py file:

```
python str_fix.py
```

A disorganized folder like this:

```
- abc.s01e01.EpisodeName.TorrentSite.srt
- abc.s01e01.mkv
- abc.s01e02.EpisodeName.TorrentSite.srt
- abc.s01e02.mkv
```

Will change to this:

```
- abc.s01e01.mkv
- abc.s01e01.srt
- abc.s01e02.mkv
- abc.s01e02.srt
```

Use it carefully. It has a preview mode to avoid any problems, but renaming some directories on your computer may be dangerous.