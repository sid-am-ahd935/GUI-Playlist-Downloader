import os
import logging
from time import sleep
from tqdm import tqdm
from threading import Thread
from pytube import Playlist, YouTube, Stream
from pytube.cli import on_progress
from pytube.exceptions import VideoUnavailable, VideoPrivate, VideoRegionBlocked, RegexMatchError
import tkinter as tk

import pytube



logging.basicConfig(filename='progress.log', level=logging.WARNING)


pbar = None


def progress_callback(stream: 'Stream', data_chunk: bytes, bytes_remaining: int) -> None:
    pbar.update(len(data_chunk))




def get_file_size(video= None, _in: "['b', 'kb', 'mb', 'gb']" = None) -> tuple([int, str]):
    if not video:
        return None

    convert = {
        'B': 1,
        'KB': 1024**1,
        'MB': 1024**2,
        'GB': 1024**3,
    }
    if not _in:
        _in = 'MB'

    if _in in ['bytes', 'byte', 'b', "B"]:
        _in = 'B'

    _in = _in.upper()
    size = int(round( video.filesize / convert[_in]))
    _in = "byte(s)" if _in == 'B' else _in

    return size, _in




download_video = lambda : 1


def download_playlist(url= None, quality= ('mid' or 'high' or 'low'), playlist= None):

    dir_name = playlist.title

    if dir_name not in os.listdir():
        os.mkdir(dir_name)


    for vid_url in tqdm(playlist, desc= "Videos Downloaded"):
        try:
            download_video(url= vid_url, quality= quality, path= dir_name, download_confirmed= True)
        except Exception as e:
            import traceback as tb
            logging.critical(f'In URL: {vid_url} \n\n{tb.format_exc()} \n')
