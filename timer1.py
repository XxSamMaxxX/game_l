import config

class Timer:
    def __init__(self, time):
        self.time_since_last_execution = 0
        self.execution_interval = time

    def timer_start(self):
        self.time_since_last_execution += config.clock.get_time()