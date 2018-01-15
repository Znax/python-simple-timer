
import time

class PythonTimer:

    def __init__(self):
        self.perf_counter = {}
        self.process_time = {}
        self.cumulated_perf_counter = {}
        self.cumulated_process_time = {}
        self.count = {}

    def start(self, name):
        self.perf_counter[name] = time.perf_counter()
        self.process_time[name] = time.process_time()

    def stop(self, name):
        elapsed_perf_counter = (time.perf_counter() - self.perf_counter[name]) * 1000
        elapsed_process_time = (time.process_time() - self.process_time[name]) * 1000
        if name not in self.cumulated_perf_counter:
            self.cumulated_perf_counter[name] = 0
            self.cumulated_process_time[name] = 0
            self.count[name] = 0
        self.cumulated_perf_counter[name] += elapsed_perf_counter
        self.cumulated_process_time[name] += elapsed_process_time
        self.count[name] += 1

    def get_perf_counter_ms(self):
        return self.cumulated_perf_counter

    def get_process_time_ms(self):
        return self.cumulated_process_time

    def get_count(self):
        return self.count

    def reset(self):
        self.perf_counter = {}
        self.cumulated_perf_counter = {}
        self.count = {}
