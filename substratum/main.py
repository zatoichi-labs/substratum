from typing import (
    Dict,
)

from substratum.providers import (
    BaseProvider,
)
from substratum.api import (
    Chain,
    Module,
    System,
)


def get_default_modules() -> Dict[str, Module]:
    return {
        "system": System,
        "chain": Chain,
    }


class Substratum:
    def __init__(self, provider: BaseProvider, modules: Dict[str, Module]=None) -> None:
        self.provider = provider
        if modules is None:
            modules = get_default_modules()

        for namespace, module in modules.items():
            setattr(self, namespace, module(self.provider))
