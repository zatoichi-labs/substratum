from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    Module as ModuleType,
)

from .module import (
    Module,
)


class Meta(Module):
    _provider: BaseProvider

    def __init__(self, provider: BaseProvider, module: Module):
        super().__init__(provider)
        self._name = module['name']
        self._prefix = module['prefix']
        self._storage = module['storage']
        self._calls = module['calls']
        self._events = module['events'],
        self._constants = module['constants']
        self._errors = module['errors']

    @property
    def name(self) -> str:
        return self._name

    @property
    def prefix(self) -> str:
        return self._prefix

    @property
    def storage(self) -> str:
        return self._storage

    @property
    def calls(self) -> str:
        return self._calls

    @property
    def events(self) -> str:
        return self._events

    @property
    def constants(self) -> str:
        return self._constants

    @property
    def errors(self) -> str:
        return self._errors
