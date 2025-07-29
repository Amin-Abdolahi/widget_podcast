# Simple VLC Audio Streamer 🎵

This is a simple Python program using the [python-vlc](https://pypi.org/project/python-vlc/) module that allows you to:

- Stream a radio URL or local audio file.
- Control playback (Play / Stop).
- Adjust volume.
- Set a sleep timer.

## Features

- ✅ Play a remote audio URL or local file
- ✅ Volume control (1–100)
- ✅ Simple command-line interface
- ✅ Optional sleep timer to auto-stop playback

## Requirements

- Python 3.x
- [python-vlc](https://pypi.org/project/python-vlc/)  
You can install it using:

```bash
pip install python-vlc
```
Note: You also need to have VLC installed on your system.
## How to Run
```
podcast_player.py
```
Just press Enter to use the default test radio stream.

## Example
```
Enter file address or URL:
# (Press Enter for default stream)

1- Stop
2- Refresh
3- Volume
4- Sleep timer
Your choice: 3
Enter a number between 1 - 100 for volume: 90
```
## To Do (Future Improvements)
- Add GUI (e.g. using tkinter or PyGObject)

- Save recent URLs to a history file

- Show current stream title or metadata

- Handle invalid URLs or errors more gracefully

## License
MIT License