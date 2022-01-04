class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Warehouse:
    def __init__(self, office_equipments=None):
        if not office_equipments:
            office_equipments = {}
        self.office_equipments = office_equipments

    def add_equipment(self, office_equipment):
        equipment_name = office_equipment.full_name
        result = self.office_equipments.get(equipment_name, None)
        if result:
            self.office_equipments[equipment_name] += 1
        else:
            self.office_equipments.update({equipment_name: 1})

    def remove_equipment(self, office_equipment):
        equipment_name = office_equipment.full_name
        result = self.office_equipments.get(equipment_name, None)
        if result and result > 0:
            self.office_equipments[equipment_name] -= 1
            return True
        else:
            return False


class Division:
    def __init__(self, title):
        self.title = title
        self.office_equipment = None
        self.have_equipment = False

    def add_equipment(self, office_equipment):
        self.office_equipment = office_equipment
        self.have_equipment = True

    def remove_equipment(self):
        self.office_equipment = None
        self.have_equipment = False


class WarehouseManager:
    def __init__(self, name, warehouse):
        self.name = name
        self.warehouse = warehouse

    def give_equipment(self, office_equipment, division):
        if not division.have_equipment:
            wh_have_office_equipment = self.warehouse.remove_equipment(office_equipment)
            if wh_have_office_equipment:
                division.add_equipment(office_equipment)
            else:
                print('На складе не осталось этого вида оргтехники.')
        else:
            print('В подразделении уже есть оргтехника.')

    def take_equipment(self, office_equipment, division):
        if division.have_equipment and division.office_equipment == office_equipment:
            division.remove_equipment()
            self.warehouse.add_equipment(office_equipment)
        else:
            print('В подразделении нет нужной оргтехники.')


class OfficeEquipments:
    def __init__(self, company_manufacturer, model):
        self.__company_manufacturer = company_manufacturer
        self.__model = model

    @property
    def full_name(self):
        return f'{self.__company_manufacturer} {self.__model}'

    def __str__(self):
        return self.full_name


class Printer(OfficeEquipments):
    def __init__(self, company_manufacturer, model, color):
        super().__init__(company_manufacturer, model)
        self.__color = color


class Scanner(OfficeEquipments):
    def __init__(self, company_manufacturer, model, optical_resolution):
        super().__init__(company_manufacturer, model)
        self.__optical_resolution = optical_resolution


class Xerox(OfficeEquipments):
    def __init__(self, company_manufacturer, model, print_speed):
        super().__init__(company_manufacturer, model)
        self.__print_speed = print_speed


my_office_equipment_1 = Printer('HP', 'DeskJet 2720', True)
my_office_equipment_2 = Scanner('Canon', 'CanoScan 5600F', (4800, 9600))
my_office_equipment_3 = Xerox('Xerox', 'WorkCentre B205NI', 30)
a = input('Введите количество принтеров на складе (только число): ')
b = input('Введите количество сканеров на складе (только число): ')
c = input('Введите количество ксероксов на складе (только число): ')
my_office_equipments = {}
try:
    if a.isdigit() and b.isdigit() and c.isdigit():
        my_office_equipments = {
            my_office_equipment_1.full_name: int(a),
            my_office_equipment_2.full_name: int(b),
            my_office_equipment_3.full_name: int(c)
        }
    else:
        raise MyException('Количество техники можно ввести только числом.')
except MyException as e:
    print(e)
    exit(0)
my_division_1 = Division('Division 1')
my_division_2 = Division('Division 2')
my_warehouse = Warehouse(my_office_equipments)
my_warehouse_manager = WarehouseManager('Warehouse manager', my_warehouse)

print('0 действие:')
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('1 действие:')
my_warehouse_manager.give_equipment(office_equipment=my_office_equipment_2, division=my_division_1)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('2 действие:')
my_warehouse_manager.give_equipment(office_equipment=my_office_equipment_2, division=my_division_2)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('3 действие:')
my_warehouse_manager.give_equipment(office_equipment=my_office_equipment_1, division=my_division_2)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('4 действие:')
my_warehouse_manager.give_equipment(office_equipment=my_office_equipment_3, division=my_division_1)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('5 действие:')
my_warehouse_manager.take_equipment(office_equipment=my_office_equipment_3, division=my_division_1)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')

print('6 действие:')
my_warehouse_manager.take_equipment(office_equipment=my_office_equipment_2, division=my_division_1)
print(f'Техника в 1 отделе: {my_division_1.office_equipment}')
print(f'Техника во 2 отделе: {my_division_2.office_equipment}')
print(f'Техника на складе: {my_warehouse.office_equipments}')
