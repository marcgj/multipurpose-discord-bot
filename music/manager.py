from music.queue import Queue
from music.track import ITrack

from discord.voice_client import VoiceClient



class GuildMusicManager():
    # Related to discordpy
    voice_client = None
    
    # Related to song management
    current_track = None
    queue = Queue()
    
    def __init__(self, voice_client:VoiceClient) -> None:
        self.voice_client = voice_client
        
    def process_track(self, track: ITrack):
        # Directly add to queue
        self.queue.add_track(track)
        print(self.queue.queue)
        
        # If nothing is playing, play next track 
        if not self.current_track:
            self.play_next()
            
    def play_next(self):
        # Check if queue empty
        if self.queue.is_empty():
            return
        
        # Get track from queue
        track = self.queue.pop_track()
        
        # Set current track
        self.current_track = track
        
        # Play track
        self.voice_client.play(track, after=self._after_track)
      
    # Called after the track ends
    def _after_track(self, error):
        # TODO Handle errors
        self.current_track = None
        self.play_next()
        
        
        
        
        
        
        
    
    