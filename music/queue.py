from music.track import ITrack


class Queue():
    queue = []
    
    def add_track(self, track: ITrack):
        """
        Ads a track to the queue

        Args:
            track (ITrack): Track to be added
        """
        self.queue.append(track)
        
        
    def pop_track(self) -> ITrack:
        """Returns and removes the first track of the queue"""
        return self.queue.pop(0)
        
    def get_next(self) -> ITrack | None:
        """Returns the first track of the queue without deleting it"""
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        """Returns whether the queue is empty or not
        """
        return True if len(self.queue) == 0 else False
    