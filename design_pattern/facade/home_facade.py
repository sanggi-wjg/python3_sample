from design_pattern.facade.funitures import Screen, Projector, DvdPlayer, Light


class HomeFacade:

    def __init__(self, screen: Screen, projector: Projector, dvd_player: DvdPlayer, light: Light):
        self.screen = screen
        self.projector = projector
        self.dvd_player = dvd_player
        self.light = light

    def start_watch_movie(self):
        self.screen.down()
        self.projector.on()
        self.dvd_player.on()
        self.dvd_player.eject_dvd('Terminator')
        self.dvd_player.start()
        self.light.off()

    def finish_watch_movie(self):
        self.light.on()
        self.dvd_player.pop_dvd()
        self.dvd_player.off()
        self.projector.off()
        self.screen.up()


if __name__ == '__main__':
    home_facade = HomeFacade(Screen(), Projector(), DvdPlayer(), Light())
    home_facade.start_watch_movie()
    print()
    home_facade.finish_watch_movie()
