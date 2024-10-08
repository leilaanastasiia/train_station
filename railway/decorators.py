import functools

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
