from multiprocessing import Queue, Process
from queue import Empty


class Forward():
    def __str__(self):
        return 'forward'


class TurnLeft():
    def __str__(self):
        return 'turn left'


class Park():
    def __str__(self):
        return 'park'


def create_environment(send):
    return {
        "forward": lambda: send(Forward()),
        "turn_left": lambda: send(TurnLeft()),
        "park": lambda: send(Park())
    }


def client(queue, source):
    def send(message):
        queue.put(message)

    instructions = read_instructions(source, send)
    instructions()


def interact(queue):
    running = True
    while running:
        try:
            action = queue.get(True, 0.1)
            print(action)
            if isinstance(action, Park):
                running = False
        except Empty:
            print("Empty!")
            running = False


def read_instructions(source, send):
    environment = create_environment(send)
    exec(source, environment)
    return environment['instructions']


def server():
    queue = Queue(maxsize=1)
    with open('student.py') as file:
        source = file.read()
    process = Process(target=client, args=(queue, source))
    process.start()
    interact(queue)
    process.kill()


if __name__ == '__main__':
    server()
