from pysim.environments.simple import SimpleEnvironment
from pysim.actors.actor import Actor
import importlib


source = '''
forward()
forward()
'''


def main():
    actor = Actor(source, SimpleEnvironment)
    print(actor.receive())
    print(actor.receive())


if __name__ == '__main__':
    main()
