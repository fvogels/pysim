from pysim.actors.actor import Channel, export
import pysim.simulation.actions as actions

class SimpleEnvironment:
    __channel : Channel[actions.Action]

    def __init__(self, channel : Channel[actions.Action]):
        self.__channel = channel

    @export
    def forward(self) -> None:
        self.__channel.send(actions.ForwardAction())

    @export
    def backward(self) -> None:
        self.__channel.send(actions.BackwardAction())

    @export
    def turn_left(self) -> None:
        self.__channel.send(actions.TurnLeftAction())

    @export
    def turn_right(self) -> None:
        self.__channel.send(actions.TurnRightAction())
