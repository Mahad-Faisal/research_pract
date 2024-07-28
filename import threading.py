import threading
import time

class TrafficLight:
    def __init__(self, name, green_duration=5, yellow_duration=2, red_duration=7):
        self.name = name
        self.green_duration = green_duration
        self.yellow_duration = yellow_duration
        self.red_duration = red_duration
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

    def set_light(self, color):
        self.current_color = color
        print(f'{self.name} is {self.current_color}')

    def stop(self):
        self.stop_event.set()

def main():
    # Define traffic light configurations for each intersection
    intersections = {
        'Intersection 1': [TrafficLight('Light 1A', 5, 2, 7), TrafficLight('Light 1B', 5, 2, 7)],
        'Intersection 2': [TrafficLight('Light 2A', 6, 3, 8), TrafficLight('Light 2B', 6, 3, 8)],
        'Intersection 3': [TrafficLight('Light 3A', 4, 2, 6), TrafficLight('Light 3B', 4, 2, 6)],
        'Intersection 4': [TrafficLight('Light 4A', 5, 2, 7), TrafficLight('Light 4B', 5, 2, 7)],
    }

    threads = []

    for intersection, lights in intersections.items():
        for light in lights:
            thread = threading.Thread(target=light.run)
            threads.append(thread)
            thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for intersection, lights in intersections.items():
            for light in lights:
                light.stop()
        for thread in threads:
            thread.join()

if __name__ == '__main__':
    main()
