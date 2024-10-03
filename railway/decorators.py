# def instance_counter(cls):
#     cls._instances = 0
#
#     def __init__(self, *args, **kwargs):
#         cls._instances = _register_instance(cls)
#     def instances():
#         return cls._instances
#     def _register_instance(self):
#         cls._instances += 1
#         return self._instances
#
#     return cls
import functools


# class InstanceCounter:
#     def __init__(self, cls):
#         self.cls = cls
#
#     def __call__(self, *args, **kwargs):
#         result = self.cls(*args, **kwargs)
#         print('hey')
#         return result
def instance_counter(cls):

    @functools.wraps(cls, updated=())
    class InstanceCounter(cls):
        original_init = cls.__init__
        _instances = 0

        def __init__(self, original_init, *args, **kwargs):
            original_init(self, *args, **kwargs)
            self._instances = self._register_instance()
            cls.instances = self.instances

        def instances(self):
            return cls._instances

        def _register_instance(self):
            self._instances += 1
            return self._instances

        cls.__init__ = __init__

    return InstanceCounter