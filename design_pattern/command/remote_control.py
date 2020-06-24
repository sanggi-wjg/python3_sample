from design_pattern.command.command import Command


class RemoteControl:

    def __init__(self):
        self.on_command = []
        self.off_command = []

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_command[slot] = on_command
        self.off_command[slot] = off_command

    def on_button_press(self, slot: int):
        self.on_command[slot].execute()

    def off_button_press(self, slot: int):
        self.off_command[slot].execute()
