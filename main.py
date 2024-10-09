from railway.train import PassengerTrain, CargoTrain, Train
from railway.station import Station
from railway.wagon import CargoWagon, PassengerWagon


def created_stations():
    if len(Station.instances_dict) > 0:
        print('Created stations:', *Station.instances_dict.keys(), sep='\n')
        user_station = input("Choose the station's name: ").strip()
        return Station.instances_dict[user_station]
    return None

def created_trains():
    if len(Train.instances) > 0:
        print('Created trains:', *Train.instances.keys(), sep='\n')
        user_train = input("Choose the train's number: ").strip()
        return Train.instances[user_train]
    return None

def created_wagons(train):
    if train:
        wagons = train.get_wagons()
        if wagons:
            print('Created wagons:', *wagons, sep='\n')
            user_number = input("Enter only wagon's number: ").strip()
            wagon = [wagon for wagon in wagons if wagon.number == int(user_number)]
            return wagon[0]
        return None
    return None


def create_station():
    try:
        user_input = input('Enter name of the Station: ').strip()
        station = Station(user_input)
        return f'Station {station.name} was created.'
    except ValueError as ve:
        return f'Try again. Wrong input: {ve}'

def create_train():
    try:
        train_type, number = input('Enter type of the train and its number '
                                '(ex. passenger_500-AX / cargo_200UA: ').strip().split(sep='_')
        if train_type == 'passenger':
            train = PassengerTrain(number)
            return f'Passenger train with a number {train.number} was created.'
        if train_type == 'cargo':
            train = CargoTrain(number)
            return f'Cargo train with a number {train.number} was created.'
    except ValueError as ve:
        return f'Try again. Wrong input: {ve}'

def add_wagon_to_train():
    train = created_trains()
    try:
        if train and isinstance(train, PassengerTrain):
            number, capacity = input('Enter a number of wagon and its capacity '
                                    '(ex. 20 100): ').strip().split()
            wagon = PassengerWagon(int(number), int(capacity))
            train.add_wagon(wagon)
            return f'Wagon {wagon.number} was added to the train {train.number}.'
        if train and isinstance(train, CargoTrain):
            number, weight = input('Enter a number of wagon and its max weight '
                                    '(ex. 20 100): ').strip().split()
            wagon = CargoWagon(int(number), int(weight))
            train.add_wagon(wagon)
            return f'Wagon {wagon.number} was added to the train {train.number}.'
        return 'No trains were created.'
    except ValueError as ve:
        return f'Try again. Wrong input: {ve}'

def remove_wagon_from_train():
    train = created_trains()
    wagon = created_wagons(train)
    if train and wagon:
        train.remove_wagon(wagon)
        return f'Wagon {wagon.number} was removed.'
    return 'No trains or wagons were there.'

def take_seat_or_load_weight_wagon():
    train = created_trains()
    wagon = created_wagons(train)
    if train and wagon:
        if isinstance(wagon, PassengerWagon):
            try:
                wagon.take_seat()
                return (f'You took a seat at the wagon {wagon.number}. '
                                f'Sets left: {wagon.free_seats()}.')
            except ValueError as ve:
                return ve
        elif train and isinstance(wagon, CargoWagon):
            try:
                wagon.load_weight(int(input('Enter the weight to load in kg: ')))
                return f'The weight was loaded. Free weight left: {wagon.free_weight()} kg.'
            except ValueError as ve:
                return ve
    else:
        return 'No trains or wagons were there.'

def add_train_to_station():
    station = created_stations()
    train = created_trains()
    if train and station:
        station.add_train(train)
        return f'Train {train.number} was added to the Station {station.name}.'
    return 'Create trains or stations first.'

def list_objects(item):
        print(item)

def show_all_stations_and_trains():
    station = created_stations()
    if station:
        try:
            station.call_trains(list_objects)
        except TypeError as te:
            return te
    else:
        return 'No stations were created.'

def show_all_trains_wagons():
    train = created_trains()
    if train:
        try:
            train.call_wagons(list_objects)
        except TypeError as te:
            return te
    else:
        return 'No trains were created.'


def main():
    options_dict = {
        'station_creation': create_station,
        'train_creation': create_train,
        'add_wagon_to_train': add_wagon_to_train,
        'remove_wagon_from_train': remove_wagon_from_train,
        'take_seat_or_load_weight_wagon': take_seat_or_load_weight_wagon,
        'add_train_to_station': add_train_to_station,
        'show_all_stations_and_trains': show_all_stations_and_trains,
        'show_all_trains_wagons': show_all_trains_wagons,
    }
    print('Available options:\n', *options_dict.keys(), sep='\n', end='\n\n')
    user_input = input('Please, enter an option to run: ')

    if user_input in options_dict:
        output = options_dict[user_input]()
        print(output, '\n')
    else:
        print("Wrong input, try again.")


if __name__ == '__main__':
    while True:
        main()
