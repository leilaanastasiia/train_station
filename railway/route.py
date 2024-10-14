from __future__ import annotations

from railway.station import Station
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .station import Station

class Route:
    """
    Represents a route class.
    """

    def __init__(self, start: Station, end: Station):
        if self._is_valid(start, end):
            self.start = start
            self.end = end
            self._way = []
        else:
            raise ValueError("Route's start or end must be an object of Station class.")

    @staticmethod
    def _is_valid(start, end):
        if isinstance(start, Station) and isinstance(end, Station):
            return start, end
        return None

    def get_way(self):
        if len(self._way) != 0:
            intermediate_stops = [i.name for i in self._way]
            return [self.start.name, *intermediate_stops, self.end.name]
        return [self.start.name, self.end.name]

    def add_intermediate_station(self, station):
        return self._way.append(station)

    def delete_intermediate_station(self, station):
        try:
            self._way.remove(station)
            return self._way
        except ValueError as ve:
            return f'No station were found: {ve}.'

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}(start={self.start!r}, end={self.end!r})"
