class ParkingLot(object):
    def __init__(self):
        self.list_of_levels = []
        self.slot_mapping = {"vacant": [], "filled": []}

    def park(self, car):
        import random

        vacant_slots = self.slot_mapping["vacant"]
        random_slot_index = random.randrange(0, len(vacant_slots))
        vacant_slot = self.slot_mapping["vacant"].pop(random_slot_index)

        vacant_slot.is_vacant = False
        vacant_slot.car = car

        self.slot_mapping["filled"].append(vacant_slot)

    def un_park(self, car):
        filled_slot_index = None
        for idx, each_slot in enumerate(self.slot_mapping["filled"]):
            if each_slot.car.reg_number == car.reg_number:
                filled_slot_index = idx
                break

        if not filled_slot_index:
            print("Car is not present i our parking lot")
            return None

        filled_slot = self.slot_mapping["filled"].pop(filled_slot_index)

        filled_slot.is_vacant = True
        filled_slot.car = None

        self.slot_mapping["vacant"].append(filled_slot)

    def get_count_for_colored_car(self, color):
        count = 0
        for each_slot in self.slot_mapping["filled"]:
            if each_slot.car.color == color:
                count += 1
        print("Color - {}, count - {}".format(color, count))
        return count

    def get_car_count_for_level(self, level_number):
        filled_lots = set(self.slot_mapping["filled"])
        lots = set()

        for each_level in self.list_of_levels:
            if each_level.number == level_number:
                lots = set(each_level.list_of_slots)
                break

        if lots:
            level_filled_lots = lots.intersection(filled_lots)
            return len(level_filled_lots)

        return 0


class Level(object):
    def __init__(self, number, list_of_slots):
        self.number = number
        self.list_of_slots = list_of_slots


class Slot(object):
    def __init__(self, slot_number, level, is_vacant=True, car=None):
        self.slot_number = slot_number
        self.is_vacant = is_vacant
        self.level = level
        self.car = car


class Car(object):
    def __init__(self, reg_number, color):
        self.reg_number = reg_number
        self.color = color


def parking_lot_service():
    car1 = Car("123", "blue")
    car2 = Car("234", "green")
    car3 = Car("345", "blue")
    car4 = Car("567", "blue")

    slot1 = Slot("1", 0)
    slot2 = Slot("2", 0)
    slot3 = Slot("3", 0)
    slot4 = Slot("4", 0)
    slot5 = Slot("5", 1)
    slot6 = Slot("6", 1)
    slot7 = Slot("7", 1)
    slot8 = Slot("8", 1)
    slot9 = Slot("9", 2)
    slot10 = Slot("10", 2)
    slot11 = Slot("11", 2)
    slot12 = Slot("12", 2)

    level0 = Level(0, [slot1, slot2, slot3, slot4])
    level1 = Level(1, [slot5, slot6, slot7, slot8])
    level2 = Level(2, [slot9, slot10, slot11, slot12])

    parking_lot = ParkingLot()
    parking_lot.list_of_levels = [level0, level1, level2]
    temp_vacant_slots = []
    for each_level in parking_lot.list_of_levels:
        temp_vacant_slots.extend(each_level.list_of_slots)
    parking_lot.slot_mapping["vacant"].extend(temp_vacant_slots)

    parking_lot.park(car1)
    parking_lot.park(car4)
    parking_lot.park(car2)
    parking_lot.un_park(car4)
