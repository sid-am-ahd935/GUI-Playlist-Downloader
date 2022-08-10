from helper_functions import d_print
from threading import Thread
import downloader

import socket
socket.setdefaulttimeout(60)

import time
from constants import (
    MEDIUM,
    AV_BOTH,
    URL_PLACEHOLDER,
    QUALITY_PLACEHOLDER,
    AV_PLACEHOLDER,
    DEFAULT_ENTRY_PLACEHOLDER
)
from tkinter import END, Frame, EW, Label, Button, Checkbutton, NSEW, LEFT, X
from validators import validate_url


def wait(seconds, wait_for):
    i = 0
    while i < seconds and not wait_for:
        time.sleep(0.1)
        i += 0.1


def get_video_details(i, url):
    try:
        vid_obj = downloader.get_video(url)
        vid_info = vid_obj.vid_info
        streams = vid_obj.streams
        vid_details = vid_info['videoDetails']
        Cache.video_details[i] = vid_info, streams, vid_details
    except Exception:
        return



class Cache:
    prev_url = ''
    path = ''
    quality = ''
    av = ''
    include = []
    exclude = []
    inc_ranges = ''
    exc_ranges = ''
    vars = {}
    videos = []
    threads = []
    video_details = {}
    listbox = None
    statusbox = None
    max_wait_time= 10

    @staticmethod
    def update_video_list(playlist : list):
        Cache.videos = playlist

    @staticmethod
    def get_videos():
        for t in Cache.threads:
            t.join()
        return Cache.videos

    @staticmethod
    def add_status(text):
        Cache.statusbox.insert(END, text)

    @staticmethod
    def update_status(text):
        Cache.statusbox.delete(0, END)
        Cache.add_status(text)

    @staticmethod
    def add_video_details(i, url):
        try:
            vid_obj = downloader.get_video(url)
            vid_info = vid_obj.vid_info
            streams = vid_obj.streams
            vid_details = vid_info['videoDetails']
            Cache.video_details[i] = vid_info, streams, vid_details
        except Exception:
            return

    @staticmethod
    def add_videos(url, placeholder= URL_PLACEHOLDER):
        url = url.strip()
        url = url.replace(placeholder, '')

        if Cache.prev_url == url:
            return

        Cache.prev_url = url

        if not validate_url(url):
            Cache.update_status(f"Bad URL Format[{url}]....")
            return

        d_print(validate_url(url), url)
        d_print("Started extracting playlist videos...")

        # Cache.update_status(f"Entered URL[{url}]...")
        Cache.update_status("Loading Contents...")

        videos = []

        try:
            videos = downloader.get_playlist(url= url, raise_error= True)
            Cache.update_video_list(videos)
        except Exception as e:
            import traceback
            d_print("Exception occurred:", '-'*30, '\n', traceback.format_exc())
            Cache.update_status("There was some error, please restart this application and try again.")


        d_print(len(Cache.threads))
        d_print(Cache.threads)
        exclude_threads = len(Cache.threads)

        for i, v_url in enumerate(videos):
            # d_print(i, v_url)
            # video_obj = downloader.get_video(url)
            # vid_info = video_obj.vid_info['videoDetails']
            # d_print(vid_details.keys())
            thread_worker = Thread(target= get_video_details, args= (i, v_url))
            thread_worker.start()
            Cache.threads.append(thread_worker)

        d_print(len(Cache.threads))
        d_print(Cache.threads)


        for thread in Cache.threads[exclude_threads:]:
            thread.join()

        for i, v in Cache.video_details.items():
            vid_info, streams, vid_details = v
            d_print(i, vid_details['title'])



        ## Listbox Insertion






        Cache.update_status("Contents Loaded.")
        d_print("\n\nStopped extracting playlist videos...")

    @staticmethod
    def save_path(path, placeholder= DEFAULT_ENTRY_PLACEHOLDER):
        path = path.replace(placeholder, '')
        if path == Cache.path:
            return
        Cache.path = path

    @staticmethod
    def save_quality(quality, placeholder= QUALITY_PLACEHOLDER):
        quality = quality.replace(placeholder, '')
        if quality == Cache.quality:
            return
        Cache.quality = quality

    @staticmethod
    def save_av(av, placeholder= AV_PLACEHOLDER):
        av = av.replace(placeholder, '')
        if av == Cache.av:
            return
        Cache.av = av

    @staticmethod
    def range2list(ranges):
        res = []

        if ranges.startswith('...'):
            ranges = ranges.replace('...', '1', 1)

        if ranges.endswith('...'):
            ranges = ranges.replace('...', str(len(Cache.videos)))

        for r in ranges.split(','):
            s, *e = r.split('-')
            s = int(s)
            e = int(e[-1]) if e else s
            res.extend(range(s, e+1))

        return res

    @staticmethod
    def save_include(ranges, placeholder= DEFAULT_ENTRY_PLACEHOLDER):
        ranges = ranges.replace(placeholder, '')
        if ranges == Cache.inc_ranges:
            return
        Cache.inc_ranges = ranges
        Cache.include = Cache.range2list(ranges)

        d_print(Cache.include, Cache.inc_ranges)

    @staticmethod
    def save_exclude(ranges, placeholder= DEFAULT_ENTRY_PLACEHOLDER):
        ranges = ranges.replace(placeholder, '')
        if ranges == Cache.exc_ranges:
            return
        Cache.exc_ranges = ranges
        Cache.exclude = Cache.range2list(ranges)

        d_print(Cache.exclude, Cache.exc_ranges)

    @staticmethod
    def final_submit():
        # Placeholder is the most important part, or else errors
        # Placeholder will be the same as the text that act as input hints
        var_n_func_call = {
            'url_var' : ('add_videos', URL_PLACEHOLDER),
            'path_var' : ('save_path', DEFAULT_ENTRY_PLACEHOLDER),
            'quality_var' : ('save_quality', QUALITY_PLACEHOLDER),
            'av_var' : ('save_av', AV_PLACEHOLDER),
            'include_var' : ('save_include', DEFAULT_ENTRY_PLACEHOLDER),
            'exclude_var' : ('save_exclude', DEFAULT_ENTRY_PLACEHOLDER),
        }

        for k, v in var_n_func_call.items():
            func, placeholder = v
            var = Cache.vars[k].get()
            # d_print(var)
            getattr(Cache, func)(var, placeholder)

        return 0

    @staticmethod
    def download_selection():


        select = sorted(set(Cache.include) - set(Cache.exclude))

        if not select:
            select = range(len(Cache.videos))


        quality = MEDIUM if not Cache.quality else Cache.quality
        av = AV_BOTH if not Cache.av else Cache.av

        d_print(Cache.include, Cache.exclude)
        d_print(select)
        d_print(quality, av)
        d_print()
