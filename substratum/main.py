from typing import (
    Dict,
)

from substratum.api import (
    Chain,
    Module,
    State,
    System,
)
from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    RPCMethods,
)


def get_default_modules() -> Dict[str, Module]:
    return {
        "system": System,
        "chain": Chain,
        "state": State,
    }


class Substratum:
    def __init__(self, provider: BaseProvider, modules: Dict[str, Module]=None) -> None:
        self._provider = provider
        if modules is None:
            modules = get_default_modules()

        for namespace, module in modules.items():
            setattr(self, namespace, module(self._provider))

    @property
    def rpc_methods(self) -> RPCMethods:
        return self._provider.make_request("rpc_methods", [])
