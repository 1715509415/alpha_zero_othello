from collections import deque
import random
try:
   import cPickle as pickle
except:
   import pickle

class ReplayBuffer(object):

    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.count = 0
        self.buffer = deque()

    def add(self, experience):
        if self.count < self.buffer_size: 
            self.buffer.append(experience)
            self.count += 1
        else:
            self.buffer.popleft()
            self.buffer.append(experience)
        
    def merge(self, buffer):
        for elem in buffer:
            self.add(elem)
        
    def size(self):
        return self.count

    def sample(self, sample_size):
        sample = []

        if self.count < sample_size:
            sample = random.sample(self.buffer, self.count)
        else:
            sample = random.sample(self.buffer, sample_size)

        return sample

    def save(self, filename):
        file = open(filename, 'wb') 
        pickle.dump(pickle.dumps(self.buffer), file)
        file.close() 
    
    def load(self, filename):
        try:
            file = open(filename, 'rb') 
            if len(self.buffer) == 0:
                self.buffer = pickle.loads(pickle.load(file))
            else:
                buf = pickle.loads(pickle.load(file))
                self.merge(buf)
            file.close() 
        except Exception:
            pass

    def clear(self):
        self.buffer.clear()
        self.count = 0