import platform

OS = platform.system()


# Defined Constants for the GUI
## Please Check Twice Before Changing These Constants As Some Values May Break The Application
WIDTH = 1080
HEIGHT = 620
PANE_MIN_WIDTH = 500
PANE_MIN_SUB_HEIGHT = 500
URL_PLACEHOLDER = "Enter a playlist url..."
DEFAULT_ENTRY_PLACEHOLDER = "Enter..."
DEFAULT_DROPDOWN_PLACEHOLDER = "Select"
QUALITY_PLACEHOLDER = "Select"
AV_PLACEHOLDER = "Select"


# Text Modifiers
underline = UL = "\033[4m"
reset = RS = "\033[0m"
sp = spaces = lambda text, times : ' '*times + text + ' '*times


# Defined Constants For A Video Meta Data Filter
LOW = '144p'
MEDIUM = '360p'
HIGH = '720p'

# Experimental Quality Meta Data
HIGH_MED = '480p'
HD = '1080p'

AV_BOTH = "av_both"
AUDIO_ONLY = "audio_only"
VIDEO_ONLY = "video_only"


# Default Values For Tutorial
playlist_url = "https://www.youtube.com/playlist?list=PL3IdQ7nHrG706h74SqSjKGbBn6lhpmMxs"
video_url = "https://www.youtube.com/watch?v=PziYflu8cB8"


# For Tutorials
playlist_dummy_url = 'https://www.youtube.com/playlist?list=PLhyHc3W8oSov-ucuA2YzzFMTJPZ6GNXJy'
video_dummy_url = 'https://www.youtube.com/watch?v=xh79e5mA2Yo'

# Some error URLs
url1 = "https://www.youtube.com/watch?v=32nkdvLq3oQ"            # This video has been removed for violating YouTube's Terms of Service
url2 = "https://www.youtube.com/watch?v=4rQbyPz40w0"            # Sign in to confirm your age. This video may be inappropriate for some users.



# For Debugging
DEBUG = True