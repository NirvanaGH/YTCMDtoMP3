# YTCMDtoMP3

This project is designed to make downloading songs from YouTube a lot easier!
Just a simple search, select the song you want, then boom.. itll automatically convert to a MP3!

#Installation
NOTE THIS IS A WINDOWS GUIDE. For other operating systems i'll assist the best I can, but cannot promise great help.

1. Install all the dependencies using pip EXCEPT ffmpeg (This program is weird with using pip for ffmpeg). The dependencies are yt_dlp and requests.
2. Get FFmpeg from https://ffmpeg.org/download.html
3. By default, this program expects it at c:\ffmpeg\bin for the executable, but you may change that if you want it somewhere else.
4. Get a YouTube API Key, to do that you must first go to the Googles Developer Console at https://console.developers.google.com/project, then create a new project.  On the new project dashboard, go to the APIs & Services tab. Click "Enable APIs and Services" then get the "YouTube Data API v3 under YouTube APIs." Once you have done that, click on the credentials tab. And create a new credential for an API, and you should get a API key.
5. With that API key go into the py file and replace 'YOUR_API_KEY_HERE' with your API key.
6. Run the script and you should be good to go!
