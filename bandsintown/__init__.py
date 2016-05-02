__version__ = (0, 2, 0)

try:
    from .client import Client
    from .bandsintown import Bandsintown
except ImportError:
    pass
