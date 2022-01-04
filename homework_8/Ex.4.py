class Warehouse:
    def __init__(self, office_equipments=None):
        if not office_equipments:
            office_equipments = {}
        self.office_equipments = office_equipments


class OfficeEquipments:
    def __init__(self, company_manufacturer, model):
        self.company_manufacturer = company_manufacturer
        self.model = model


class Printer(OfficeEquipments):
    def __init__(self, company_manufacturer, model, color):
        super().__init__(company_manufacturer, model)
        self.color = color


class Scanner(OfficeEquipments):
    def __init__(self, company_manufacturer, model, optical_resolution):
        super().__init__(company_manufacturer, model)
        self.optical_resolution = optical_resolution


class Xerox(OfficeEquipments):
    def __init__(self, company_manufacturer, model, print_speed):
        super().__init__(company_manufacturer, model)
        self.print_speed = print_speed


my_office_equipment_1 = Printer('HP', 'DeskJet 2720', True)
my_office_equipment_2 = Scanner('Canon', 'CanoScan 5600F', (4800, 9600))
my_office_equipment_3 = Xerox('Xerox', 'WorkCentre B205NI', 30)
