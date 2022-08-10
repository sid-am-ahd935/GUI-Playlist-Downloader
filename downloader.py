from custom_exceptions import DownloaderException
from custom_typing import _Quality
from constants import (
    LOW,
    MEDIUM,
    HIGH
)
from typing import (
    List,
    Union,
    Type
)
from helper_functions import d_print
import os
import pytube.request
from pytube import (
    YouTube,
    Playlist,
    Stream
)
from pytube.exceptions import (
    VideoUnavailable,
    VideoPrivate,
    VideoRegionBlocked,
    RegexMatchError
)


# Change the value here to something smaller to decrease chunk sizes,
#  thus increasing the number of times that the progress callback occurs
# pytube.request.default_range_size = 9437184  # 9MB chunk size
pytube.request.default_range_size = 1024        # 1KB chunk size


available_qualities = (LOW, MEDIUM, HIGH)
exception_sub_msgs = {
    VideoUnavailable : 'unavailable',
    VideoPrivate : 'a private video',
    VideoRegionBlocked : 'blocked in this region',
    RegexMatchError : 'not found due to error in parsing the url'
}


def get_video(url : str) -> Union[YouTube, None]:
    video = None

    try:
        video =  YouTube(url)
    except Exception as e:
        d_print(f"Video at url [{url}] is {exception_sub_msgs.get(type(e), f'having an unknown error:{e}')}")

    return video


def get_video_details(url) -> dict:
    video_obj = get_video(url)
    d_print(video_obj)
    # d_print(video_obj.vid_info)

    return video_obj.vid_info


def get_playlist(url : str, raise_error : bool= False) -> List[YouTube]:
    playlist = []

    try:
        playlist = Playlist(url)

        # To activate the error if any:
        playlist[:1]

    except (KeyError, IndexError):
        #### 1st Error
        # ==> 1) return f"https://www.youtube.com/playlist?list={self.playlist_id}"
        # ==> 2) self._playlist_id = extract.playlist_id(self._input_url)
        # ==> 3) return parse_qs(parsed.query)['list'][0]
        # ==> 4) KeyError: 'list'

        #### 2nd Error
        # ==> 1) playlist[:1]
        # ==> 2) return self.video_urls[i]
        # ==> 3) raise IndexError

        if raise_error:
            raise DownloaderException from None

        d_print(f"Not a valid playlist url [{url}]")


    return playlist



def download_video(url : str, quality : Union[Type[_Quality], None]= MEDIUM) -> None:
    video = get_video(url)
    streams = video.streams

    if quality not in available_qualities:
        quality = MEDIUM

    try:
        file : Stream
        file = streams.filter(progressive= True, res= quality).first()
    except KeyError:
        # return self.vid_info['streamingData'] in pytube throws error
        # KeyError: 'streamingData'
        d_print(f'Video not reachable, either deleted or restricted for url [{url}]')
        return

    if not file:
        d_print(f"Video {streams.first()._monostate.title} of {quality} resolution is not available, please try again with another resolution.")
        return

    file_size = file.filesize
    file.download()


def download_playlist(url : str, quality : Union[Type[_Quality], None]= MEDIUM, path : Union[str, None]= None) -> None:
    playlist = get_playlist(url)

    if not playlist:
        d_print(f"No playlist is available at url [{url}]")
        return

    dir_name = os.path.join((path or os.getcwd()), playlist.title)

    if not dir_name in os.listdir():
        os.mkdir(dir_name)

    for video_url in playlist:
        download_video(url, quality= quality)
