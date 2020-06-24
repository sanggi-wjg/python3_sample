class Screen:

    def up(self):
        print('Screen up')

    def down(self):
        print('Screen down')


class Projector:

    def on(self):
        print('Projector power on')

    def off(self):
        print('Project power off')


class DvdPlayer:

    def on(self):
        print('DVD Player power on')

    def off(self):
        print('DVD Player power off')

    def eject_dvd(self, dvd_title):
        self.dvd_title = dvd_title
        print('{} is ejected on DVD Player'.format(self.dvd_title))

    def pop_dvd(self):
        print('{} is popped on DVD Player'.format(self.dvd_title))

    def start(self):
        print('{} is start on DVD Player'.format(self.dvd_title))

    def stop(self):
        print('{} is start on DVD Player'.format(self.dvd_title))


class Light:

    def on(self):
        print('Light on')

    def off(self):
        print('Light off')
