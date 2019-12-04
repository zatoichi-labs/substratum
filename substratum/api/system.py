from substratum.providers import (
    BaseProvider,
)

from .module import (
    Module,
)


class System(Module):
    provider: BaseProvider

    @property
    def version(self) -> str:
        return self.provider.make_request("system_version", [])

    @property
    def name(self) -> str:
        return self.provider.make_request("system_name", [])
