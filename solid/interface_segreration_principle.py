from abc import ABCMeta, abstractmethod


class CarOwnerInfo:

    def __init__(self, car_number, owner_name):
        self.__car_number = car_number
        self.__owner_name = owner_name

    @property
    def car_number(self):
        return self.__car_number

    @car_number.setter
    def car_number(self, value):
        self.__car_number = value

    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, value):
        self.__owner_name = value

    def show(self):
        print('Car number : {} / Owner name : {}'.format(self.car_number, self.owner_name))


class SuvOwnerInfo(CarOwnerInfo):
    pass


class TruckOwnerInfo(CarOwnerInfo):
    pass


################################################################################################


class CarDetailInfo(metaclass = ABCMeta):

    def __init__(self, color, wheel):
        self.__color = color
        self.__wheel = wheel

    @abstractmethod
    def show(self):
        pass

    @property
    def color(self):
        return self.__color

    @property
    def wheel(self):
        return self.__wheel


class SuvDetailInfo(CarDetailInfo):

    def show(self):
        print('Color : {} / Wheel : {}'.format(self.color, self.wheel))


class TrunkType1(metaclass = ABCMeta):
    is_trunk_opened = False
    trunk_kind = None

    @abstractmethod
    def covered(self, value):
        pass

    @abstractmethod
    def opened(self):
        pass


class TruckDetailInfo(CarDetailInfo, TrunkType1):

    def covered(self, value):
        self.is_trunk_opened = False
        self.trunk_kind = value

    def opened(self):
        self.is_trunk_opened = True

    def show(self):
        print('Color : {} / Wheel : {} / Trunk : {} {}'.format(self.color, self.wheel, self.trunk_kind, self.is_trunk_opened))


################################################################################################

class Car(metaclass = ABCMeta):
    id_number = None
    owner_info = None
    detail_info = None

    def __init__(self, id_number, owner_info: CarOwnerInfo, detail_info: CarDetailInfo):
        self.id_number = id_number
        self.owner_info = owner_info
        self.detail_info = detail_info

    @abstractmethod
    def drive(self):
        pass


class Suv(Car):

    def drive(self):
        pass


class Truck(Car):

    def drive(self):
        pass
