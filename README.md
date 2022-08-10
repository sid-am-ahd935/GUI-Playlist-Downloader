- **Deprecated**
- **No longer in production**


## The development may start again but not soon...
Due to unknown bugs, and errors in pytube, the entire downloader script became useless against multithreading. Hence using youtube-dl or finding similar libraries to migrate to seemed a bit demotivating and too much leg. So instead when I decide someday, I would be creating my own Multi threaded downloader for youtube videos and then restart this project again.
The issue was of having too many requests, caused the request library inside pytube to explode and terminating every single youtube details request.


## The GUI Part Idea

The widget should have 3 sections, one header, one body and one footer


Header:
    It should have an option to select where the the link is playlist or video.
    Then there is a text bar where we have to put in the url and click on submit button
    It will also have 3 options to select from, high, mid and low the quality of the video(s)
    After the submit button, the gui would call the main.py file and do the workings there
    There should also be a checkbox 'Check All' where all the videos check boxes will get checked
    Then


Body:
    Then all the videos collected inside a list, would get displayed in a list box
    All videos will have a check box beside their name and a little details like in file explorer
    

Footer:
    There should be the total donwload size of the checked items, no. of items, etc.
    Then there should be a prefilled text folder of the full location of where the download is going to be placed
    If there is a playlist downloading, there would be a label on the right to show after the download location is selected, another folder will be created for storing the videos

### The Motive
All the playlist downloaders out there, do not have support for choosing a range of videos to download, hence became the worst nightmare for checking and unchecking each video for downloading.
