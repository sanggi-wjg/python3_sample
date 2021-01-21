class Car:
    id_number = None
    car_number = None
    owner_name = None

    def __init__(self, id_number, car_number, owner_name):
        self.id_number = id_number
        self.car_number = car_number
        self.owner_name = owner_name


"""
차대번호는 생산에 따라 부여된 고유 번호로 변경되지 않지만,
여기서 car_number 나 owner_name 은 변경 될 수 있으므로...
아래와 같이
"""


class Car:
    id_number = None
    owner_info = None
    car_detail = None

    def __init__(self, id_number, owner_info: CarOwnerInfo, car_detail: CarDetail):
        self.id_number = id_number
        self.owner_info = owner_info
        self.car_detail = car_detail


class CarOwnerInfo:
    car_number = None
    owner_name = None


class CarDetail:
    color = None
    wheel = None
