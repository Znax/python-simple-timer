
import time

class PythonTimer:

    def __init__(self):
        self.all_times = {}
        self.cumulated_times = {}
        self.cumulated_count = {}

    def reset_timer(self):
        self.all_times = {}
        self.cumulated_times = {}
        self.cumulated_count = {}

    def start_timer(self, name):
        self.all_times[name] = time.time()

    def stop_timer(self, name):
        elapsed = time.time() - self.all_times[name]
        if name not in self.cumulated_times:
            self.cumulated_times[name] = 0
            self.cumulated_count[name] = 0
        self.cumulated_times[name] += elapsed
        self.cumulated_count[name] += 1

    def get_cumulated_times(self):
        return self.cumulated_times

    def get_cumulated_count(self):
        return self.cumulated_count
