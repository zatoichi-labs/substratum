from substratum.providers import (
    BaseProvider,
)

from .module import (
    Module,
)


class System(Module):
    _provider: BaseProvider

    @property
    def version(self) -> str:
        return self._provider.make_request("system_version", [])

    @property
    def name(self) -> str:
        return self._provider.make_request("system_name", [])
