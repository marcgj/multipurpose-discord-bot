# This file will contain an interface for a source and for the implementations


# Import discord audio processors
from discord import FFmpegPCMAudio

import yt_dlp


class ITrack(FFmpegPCMAudio):
    def __init__(self, input):
        super().__init__(self.get_source(input))

    # Url of the track
    url = None

    # Name of the track
    title = None

    # In seconds
    duration = None

    # Url to the thumbnail to be used
    thumbnail = None

    # This method should return an url to the audio and fill the above variables

    def get_source(self, input):
        pass


class YoutubeTrack(ITrack):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': True,
        'quiet': False,
        'no_warnings': True,
        'default_search': 'auto',
        # bind to ipv4 since ipv6 addresses cause issues sometimes
        'source_address': '0.0.0.0',
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
    }

    def get_source(self, input) -> FFmpegPCMAudio:
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            data = ydl.extract_info(input, download=False)

            # If in any case it finds a playlist, only get the first item
            if 'entries' in data:
                data = data['entries'][0]

            # Save track data
            self.url = data["url"]
            self.title = data["title"]
            self.duration = data["duration"]
            self.thumbnail = data["thumbnail"]

        return self.url
