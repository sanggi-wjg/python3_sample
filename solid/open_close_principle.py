class CarOwnerInfo:
    car_number = None
    owner_name = None


class SuvOwnerInfo(CarOwnerInfo):
    pass


class TruckOwnerInfo(CarOwnerInfo):
    pass


class CarDetailInfo:
    color = None
    wheel = None


class SuvDetailInfo(CarDetailInfo):
    pass


class TruckDetailInfo(CarDetailInfo):
    is_trunk_opened = False
    trunk_kind = None


class Car:
    id_number = None
    owner_info = None
    detail_info = None

    def __init__(self, id_number, owner_info: CarOwnerInfo, detail_info: CarDetailInfo):
        self.id_number = id_number
        self.owner_info = owner_info
        self.detail_info = detail_info


class Suv(Car):
    pass


class Truck(Car):
    pass


"""
확장성을 고려
"""


class Vehicle:
    car_number = None
    owner_name = None


class Car(Vehicle):
    pass


class MotorCycle(Vehicle):
    pass
