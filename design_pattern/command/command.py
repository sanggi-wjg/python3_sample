from design_pattern.command.menu.light import Light


class Command:
    def execute(self):
        raise NotImplementedError('Not implemented execute()')


class LightCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()
