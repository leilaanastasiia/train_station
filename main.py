class Train:
    speed = 0
    current_route = None
    current_station_index = None

    def __init__(self, number, train_type, wagons_amount):
        self.number = number
        self.train_type = train_type
        self.wagons_amount = wagons_amount

    def gain_speed(self):
        self.speed += 10
        return self.speed

    def brake(self):
        self.speed = 0
        return self.speed

    def get_speed(self):
        return f'The current speed of the train is {self.speed} km/h.'

    def get_wagons_amount(self):
        return self.wagons_amount

    def add_wagon(self):
        if self.speed == 0:
            self.wagons_amount += 1
            return self.wagons_amount
        else:
            return f'The current speed of the train is {self.speed} km/h. Please, stop first.'

    def remove_wagon(self):
        if self.speed == 0:
            self.wagons_amount -= 1
            return self.wagons_amount
        else:
            return f'The current speed of the train is {self.speed} km/h. Please, stop first.'

    def add_route(self, route):
        self.current_route = route
        self.current_station_index = 0
        return self.current_route.get_way()

    def get_train_stops(self):
        if self.current_route:
            way = self.current_route.get_way()
            current_station = way[self.current_station_index]
            previous_station = None if self.current_station_index == 0 else way[self.current_station_index - 1]
            next_station = None if self.current_station_index == len(way) - 1 else way[self.current_station_index + 1]
            return (f"Current station: {current_station}\n"
                    f"Previous station: {'-' if previous_station is None else previous_station}\n"
                    f"Next station: {'-' if next_station is None else next_station}")
        else:
            return 'Train has no route'

    def move_to_next_station(self):
        if self.current_route and self.current_station_index < len(self.current_route.get_way()) - 1:
            self.current_station_index += 1
            return f"Train moved to {self.current_route.get_way()[self.current_station_index]}"
        else:
            return "Train is already at the last station."

    def move_to_previous_station(self):
        if self.current_route and self.current_station_index > 0:
            self.current_station_index -= 1
            return f"Train moved to {self.current_route.get_way()[self.current_station_index]}"
        else:
            return "Train is already at the first station."

    def __repr__(self):
        class_name = type(self).__name__
        return (f"{class_name}(number={self.number!r}, train_type={self.train_type!r}, "
                f"wagons_amount={self.wagons_amount!r})")


class Station:
    trains = []

    def __init__(self, name):
        self.name = name

    def get_trains(self, train_filter=None):
        if not train_filter:
            return self.trains
        elif train_filter == 'passenger':
            return [train for train in self.trains if train.train_type == 'passenger']
        elif train_filter == 'cargo':
            return [train for train in self.trains if train.train_type == 'cargo']

    def add_train(self, train: Train) -> list:
        self.trains.append(train)
        return self.trains

    def departure_train(self, train: Train):
        try:
            self.trains.remove(train)
            return self.trains
        except ValueError as ve:
            return f'No train at the station were found: {ve}.'

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(name={self.name!r})"


class Route:
    way = []

    def __init__(self, start: Station, end: Station):
        self.start = start
        self.end = end

    def get_way(self):
        if len(self.way) != 0:
            intermediate_stops = [i.name for i in self.way]
            return [self.start.name, *intermediate_stops, self.end.name]
        else:
            return [self.start.name, self.end.name]

    def add_intermediate_station(self, station):
        return self.way.append(station)

    def delete_intermediate_station(self, station):
        try:
            self.way.remove(station)
            return self.way
        except ValueError as ve:
            return f'No station were found: {ve}.'
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(start={self.start!r}, end={self.end!r})"
