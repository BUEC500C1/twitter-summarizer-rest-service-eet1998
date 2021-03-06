import queue
from threading import Thread

from tweet2video import get_tweets
from tweet2video import image2video

class VideoWorker(Thread):
    
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get work from the queue
            handles = self.queue.get()
            try:
                get_tweets(handles)
                #image2video(handles) # creates directory but error arises when creating video
            finally:
                self.queue.task_done()

def main():
    # Create a queue to communicate with worker threads
    q = queue.Queue()
    handles = ["@NatGeo", "@REI"]
    # Create 4 worker threads
    for x in range(4):
        worker = VideoWorker(q)
        # Setting daemon to True will let the main 
        # thread exit even though the workers are blocking
        worker.daemon = True
        worker.start()
    # Put tasks into queue
    for handle in handles:
        q.put(handle)
    # Causes main thread to wait for the queue to finish processing all tasks
    q.join()


    

if __name__ == '__main__':
    main()