from random import randint
from railway.route import Route
from railway.train import PassengerTrain, CargoTrain, Train
from railway.station import Station
from railway.wagon import CargoWagon, PassengerWagon


def created_stations():
    if len(Station.instances_dict) > 0:
        print(f'Created stations:', *Station.instances_dict.keys(), sep='\n')
        user_station = input("Choose the station's name: ").strip()
        return Station.instances_dict[user_station]
    else:
        return None

def created_trains():
    if len(Train.instances) > 0:
        print(f'Created trains:', *Train.instances.keys(), sep='\n')
        user_train = input("Choose the train's number: ").strip()
        return Train.instances[user_train]
    else:
        return None

def create_station():
    user_input = input('Enter name of the Station: ')
    station = Station(user_input)
    return f'Station {station.name} was created.'

def create_train():
    train_type, number = input('Enter type of the train and its number '
                            '(passenger_55 / cargo_20: ').strip().split(sep='_')
    if train_type == 'passenger':
        train = PassengerTrain(number)
        return f'Passenger train with a number {train.number} was created.'
    elif train_type == 'cargo':
        train = PassengerTrain(number)
        return f'Cargo train with a number {train.number} was created.'
    else:
        return 'Enter valid parameters'

def add_wagon_to_train():
    train = created_trains()
    if train and isinstance(train, PassengerTrain):
        wagon = PassengerWagon(randint(1, 100), randint(50, 200))
        train.add_wagon(wagon)
        return f'Wagon {wagon.number} was added to the train {train.number}.'
    elif train and isinstance(train, CargoTrain):
        wagon = CargoWagon(randint(1, 100), randint(100, 1000))
        train.add_wagon(wagon)
        return f'Wagon {wagon.number} was added to the train {train.number}.'
    else:
        return 'No trains were created.'

def remove_wagon_from_train():
    train = created_trains()
    wagons = train.get_wagons() if train else None
    if train and wagons:
        user_wagon = input("Choose the wagon's number: ").strip()
        train.remove_wagon(user_wagon)
    else:
        return 'No trains or wagons were there.'

def add_train_to_station():
    station = created_stations()
    train = created_trains()
    if train and station:
        station.add_train(train)
        return f'Train {train.number} was added to the Station {station.name}.'
    else:
        return 'Create trains or stations first.'

def show_all_stations_and_trains():
    station = created_stations()
    return station.get_trains() if station else 'No stations were created.'


def main():
    options_dict = {
        'station_creation': create_station,
        'train_creation': create_train,
        'add_wagon_to_train': add_wagon_to_train,
        'remove_wagon_from_train': remove_wagon_from_train,
        'add_train_to_station': add_train_to_station,
        'show_all_stations_and_trains': show_all_stations_and_trains,
    }
    print('Available options:\n', *options_dict.keys(), sep='\n', end='\n\n')
    user_input = input('Please, enter an option to run: ')

    if user_input in options_dict:
        output = options_dict[user_input]()
        print(output, '\n')
    else:
        print("Wrong input")


if __name__ == '__main__':
    while True:
        main()