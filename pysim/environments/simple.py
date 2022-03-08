from pysim.actors.actor import Channel, export


class SimpleEnvironment:
    __channel : Channel[str]

    def __init__(self, channel : Channel[str]):
        self.__channel = channel

    @export
    def forward(self) -> None:
        self.__channel.send('forward')

    @export
    def turn_left(self) -> None:
        self.__channel.send('turn-left')
