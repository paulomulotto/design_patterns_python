class Property:
    def __init__(self):
        self._list_rooms = []
        self._square_meters = None
        self._id = None
        self._name = None
        self._description = None
        self._value = None

    @property
    def _number_of_rooms(self):
        return len(self._list_rooms)

    def __str__(self):
        identification_txt = f"Name: {self._name}.\n"+\
            f"Description: {self._description}\n"
            
        rooms = [f"The property has {self._number_of_rooms} rooms:"]
        for room in self._list_rooms:
            rooms.append('   '+str(room))
        rooms_txt = '\n'.join(rooms)

        return identification_txt + rooms_txt


from enum import Enum
class TypeRoom(Enum):
    KITCHEN = 'KITCHEN'
    BEDROOM = 'BEDROOM'
    BATHROOM = 'BATHROOM'
    LIVINGROOM = 'LIVINGROOM'

# Rooms of a property
class Room():
    def __init__(self):
        self._type_room = None
        self._square_meters_room = None

    def __str__(self):
        return f"{self._type_room.value} with {self._square_meters_room} square meters".capitalize()

class Bedroom(Room):
    def __init__(self, square_meters_room : int=0) -> None:
        self._type_room = TypeRoom.BEDROOM
        self._square_meters_room = square_meters_room

class Bathroom(Room):
    def __init__(self, square_meters_room : int=0) -> None:
        self._type_room = TypeRoom.BATHROOM
        self._square_meters_room = square_meters_room

class LivingRoom(Room):
    def __init__(self, square_meters_room : int=0) -> None:
        self._type_room = TypeRoom.LIVINGROOM
        self._square_meters_room = square_meters_room

class Kitchen(Room):
    def __init__(self, square_meters_room : int=0) -> None:
        self._type_room = TypeRoom.KITCHEN
        self._square_meters_room = square_meters_room


class PropertyBuilder:
    def __init__(self, __property=None):
        if __property==None: __property = Property()
        self._property = __property

    def _add_room(self, room):
        self._property._list_rooms.append(room)

    @property
    def has_a(self):
        return PropertyRoomBuilder(self._property)

    @property
    def identified_by(self):
        return PropertyDescribeBuilder(self._property)

    @property
    def value(self):
        return PropertyValueBuilder(self._property)

    def build(self):
        return self._property


class PropertyRoomBuilder(PropertyBuilder):
    def __init__(self, __property):
        super().__init__(__property)
    
    def bedroom(self,bedroom):
        self._add_room(bedroom)
        return self

    def bathroom(self,bathroom):
        self._add_room(bathroom)
        return self

    def living_room(self,living_room):
        self._add_room(living_room)
        return self

    def kitchen(self,kitchen):
        self._add_room(kitchen)
        return self


class PropertyDescribeBuilder(PropertyBuilder):
    def __init__(self, __property):
        super().__init__(__property)

    def name(self, name):
        self._property._name = name
        return self

    def id(self, id):
        self._property._id = id
        return self

    def description(self, description):
        self._property._description = description
        return self



class PropertyValueBuilder(PropertyBuilder):
    def __init__(self, __property):
        super().__init__(__property)

    def costs(self, value):
        self._property._value = value
        return self


class SmallHouseBuilder(PropertyBuilder):
    def __init__(self):
        super().__init__(Property())
        self\
            .has_a\
                .bathroom(Bathroom(square_meters_room=2))\
                .bathroom(Bathroom(square_meters_room=4))\
                .bedroom(Bedroom(square_meters_room=12))\
                .living_room(LivingRoom(square_meters_room=15))\
                .kitchen(Kitchen(square_meters_room=12))\
            .identified_by\
                .id(1)\
                .name('Small Family Residence - Spring Valley, CA')\
                .description('Single House in Spring Valley for you and your family')\
            .value\
                .costs(value=10000)
        

class LargeHouseBuilder(PropertyBuilder):
    def __init__(self):
        super().__init__(Property())
        self\
            .has_a\
                .bathroom(Bathroom(square_meters_room=2))\
                .bathroom(Bathroom(square_meters_room=4))\
                .bathroom(Bathroom(square_meters_room=4))\
                .bathroom(Bathroom(square_meters_room=4))\
                .bedroom(Bedroom(square_meters_room=20))\
                .bedroom(Bedroom(square_meters_room=15))\
                .bedroom(Bedroom(square_meters_room=12))\
                .living_room(LivingRoom(square_meters_room=15))\
                .kitchen(Kitchen(square_meters_room=12))\
            .identified_by\
                .id(1)\
                .name('Large Family Residence - Spring Valley, CA')\
                .description('Single House in Spring Valley for you and your family')\
            .value\
                .costs(value=30000)


class Apartment(Property):
    def __init__(self):
        super().__init__()
        self._floor = None
        self._block = None
        self._condominium_name = None
        

    def __str__(self):
        identification_txt = f"Apartment Name: {self._name}.\n"+\
            f"Description: {self._description}\n"
            
        rooms = [f"The apartment stay in the {self._floor}th floor and has {self._number_of_rooms} rooms:"]
        for room in self._list_rooms:
            rooms.append('   '+str(room))
        rooms_txt = '\n'.join(rooms)

        return identification_txt + rooms_txt


class ApartmentBuilder(PropertyBuilder):
    def __init__(self, apartment:Apartment=None):
        if apartment==None: apartment = Apartment()
        super().__init__(apartment)
        

    @property
    def stay(self):
        return ApartmentLocationBuilder(self._property)


class ApartmentLocationBuilder(ApartmentBuilder):
    def __init__(self, apartment):
        super().__init__(apartment)

    def on_floor(self, floor):
        self._property._floor = floor
        return self

    def in_block(self, block):
        self._property._block = block
        return self

    def condominium_name(self, condominium_name):
        self._property._condominium_name = condominium_name
        return self
        

if __name__ == '__main__':
    print("Generic Property")
    property_builder = PropertyBuilder()
    __property = property_builder\
        .has_a\
            .bathroom(Bathroom(square_meters_room=2))\
            .bathroom(Bathroom(square_meters_room=4))\
            .bedroom(Bedroom(square_meters_room=12))\
            .living_room(LivingRoom(square_meters_room=15))\
            .kitchen(Kitchen(square_meters_room=12))\
        .identified_by\
            .id(1)\
            .name('Generic Property Name')\
            .description('Generic Property Description')\
        .value\
            .costs(value=10000)\
        .build()
    print(__property)
    print('\n\n')

    print("Small House Property")
    house_builder = PropertyBuilder()
    house = house_builder\
        .has_a\
            .bathroom(Bathroom(square_meters_room=2))\
            .bedroom(Bedroom(square_meters_room=12))\
            .kitchen(Kitchen(square_meters_room=12))\
        .identified_by\
            .id(1)\
            .name('House Property Name')\
            .description('House Property Description')\
        .value\
            .costs(value=20000)\
        .build()
    print(house)
    print('\n\n')

    print("Large House Property")
    house_builder = PropertyBuilder()
    house = house_builder\
        .has_a\
            .bathroom(Bathroom(square_meters_room=2))\
            .bathroom(Bathroom(square_meters_room=3))\
            .bathroom(Bathroom(square_meters_room=4))\
            .bedroom(Bedroom(square_meters_room=12))\
            .bedroom(Bedroom(square_meters_room=15))\
            .kitchen(Kitchen(square_meters_room=20))\
        .identified_by\
            .id(1)\
            .name('Large House Property Name')\
            .description('Large House Property Description')\
        .value\
            .costs(value=50000)\
        .build()
    print(house)
    print('\n\n')

    print("StoreProperty")
    house_builder = PropertyBuilder()
    house = house_builder\
        .has_a\
            .bathroom(Bathroom(square_meters_room=2))\
            .bathroom(Bathroom(square_meters_room=3))\
            .kitchen(Kitchen(square_meters_room=10))\
            .living_room(LivingRoom(square_meters_room=30))\
        .identified_by\
            .id(1)\
            .name('Large House Property Name')\
            .description('Large House Property Description')\
        .value\
            .costs(value=50000)\
        .build()
    print(house)
    print('\n\n')


    apartament_builder = ApartmentBuilder()
    apartment =apartament_builder\
        .stay\
            .on_floor(7)\
            .in_block("A")\
        .has_a\
            .bathroom(Bathroom(square_meters_room=2))\
            .bathroom(Bathroom(square_meters_room=4))\
            .bedroom(Bedroom(square_meters_room=12))\
            .living_room(LivingRoom(square_meters_room=15))\
            .kitchen(Kitchen(square_meters_room=12))\
        .identified_by\
            .id(1)\
            .name('Apartment Residence - Spring Valley, CA')\
            .description('Single Apartment in Spring Valley for you and your family')\
        .value\
            .costs(value=10000)\
        .build()

    print(apartment)
    print('\n\n')

