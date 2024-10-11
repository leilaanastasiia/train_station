import functools
import re


def instance_counter(cls):
    """Counts the number of instances of s class."""

    @functools.wraps(cls, updated=())
    class InstanceCounter(cls):
        original_init = cls.__init__
        cls._instances = 0

        def __init__(self, *args, **kwargs):
            self.original_init(*args, **kwargs)
            cls._instances = self._register_instance()
            cls.instances = self.instances

        @classmethod
        def instances(cls):
            return cls._instances

        @classmethod
        def _register_instance(cls):
            cls._instances += 1
            return cls._instances

        cls.__init__ = __init__

    return InstanceCounter

def validate_manufacturer(func):
    @functools.wraps(func)
    def wrapper(self, manufacturer_name=None, *args, **kwargs):
        if manufacturer_name is None or isinstance(manufacturer_name, str) and len(manufacturer_name) > 0:
            return func(self, manufacturer_name, *args, **kwargs)
        raise ValueError("Manufacturer's name must be a string.")
    return wrapper

def validate_number(func):
    @functools.wraps(func)
    def wrapper(self, number, *args, **kwargs):
        if isinstance(number, int):
            return func(self, number, *args, **kwargs)
        raise ValueError("Invalid number.")
    return wrapper

def validate_wagon_subclass(func):
    @functools.wraps(func)
    def wrapper(self, number, capacity_weight, *args, **kwargs):
        if isinstance(capacity_weight, int):
            return func(self, number, capacity_weight, *args, **kwargs)
        raise ValueError("Invalid capacity|weight.")
    return wrapper


def validate_train_number_pattern(func):
    @functools.wraps(func)
    def wrapper(self, number, *args, **kwargs):
        pattern = r"^[a-zA-Z0-9]{3}(-?[a-zA-Z0-9]{2})$"
        if re.match(pattern, number):
            return func(self, number, *args, **kwargs)
        raise ValueError("Train's number must be in a valid pattern.")
    return wrapper
