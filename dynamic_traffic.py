import threading
import time
import random

class TrafficLight:
    def __init__(self, name, initial_green=5, initial_yellow=2, initial_red=7):
        self.name = name
        self.green_duration = initial_green
        self.yellow_duration = initial_yellow
        self.red_duration = initial_red
        self.current_color = 'Red'
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            self.set_light('Green')
            time.sleep(self.green_duration)
            if self.stop_event.is_set():
                break

            self.set_light('Yellow')
            time.sleep(self.yellow_duration)
            if self.stop_event.is_set():
                break

            self.set_light('Red')
            time.sleep(self.red_duration)

            # Adjust durations dynamically (example: random adjustment)
            self.green_duration = random.randint(5, 10)
            self.yellow_duration = random.randint(2, 4)
            self.red_duration = random.randint(7, 10)

    def set_light(self, color):
        self.current_color = color
        print(f'{self.name} is {self.current_color}')

    def stop(self):
        self.stop_event.set()

class Intersection:
    def __init__(self, name, lights):
        self.name = name
        self.lights = lights

    def run(self):
        for light in self.lights:
            thread = threading.Thread(target=light.run)
            thread.start()

    def stop(self):
        for light in self.lights:
            light.stop()

def main():
    intersections = {
        'Intersection 1': Intersection('Intersection 1', [
            TrafficLight('Light 1A'), TrafficLight('Light 1B')
        ]),
        'Intersection 2': Intersection('Intersection 2', [
            TrafficLight('Light 2A'), TrafficLight('Light 2B')
        ]),
        'Intersection 3': Intersection('Intersection 3', [
            TrafficLight('Light 3A'), TrafficLight('Light 3B')
        ]),
        'Intersection 4': Intersection('Intersection 4', [
            TrafficLight('Light 4A'), TrafficLight('Light 4B')
        ]),
    }

    threads = []

    for intersection in intersections.values():
        thread = threading.Thread(target=intersection.run)
        threads.append(thread)
        thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for intersection in intersections.values():
            intersection.stop()
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    main()
