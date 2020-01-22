from typing import (
    Dict,
)

from substratum.api import (
    Account,
    Chain,
    Meta,
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
        "account": Account,
        "system": System,
        "chain": Chain,
        "state": State,
    }


class Substratum:
    _provider: BaseProvider
    _installed_modules: Dict[str, Module]

    def __init__(self, provider: BaseProvider, modules: Dict[str, Module]=None) -> None:
        self._provider = provider
        self._installed_modules = dict()
        if modules is None:
            modules = get_default_modules()

        for namespace, module in modules.items():
            setattr(self, namespace, module(self._provider))
            self._installed_modules[namespace] = module

        metadata = self.state.getMetadata(self.chain.getHead())
        for raw_module in metadata['modules']:
            module = Meta(self._provider, raw_module)
            setattr(self, module.name, module)
            self._installed_modules[module.name] = module

        # Configure basic testnets
        chain = self.system.chain
        if chain == "Development":
            self.account.add_from_uri("//Alice")
            self.account.add_from_uri("//Alice//stash")
            self.account.add_from_uri("//Bob")
            self.account.add_from_uri("//Bob//stash")
        elif chain == "Local":
            self.account.add_from_uri("//Alice")
            self.account.add_from_uri("//Alice//stash")
            self.account.add_from_uri("//Bob")
            self.account.add_from_uri("//Bob//stash")
            self.account.add_from_uri("//Charlie")
            self.account.add_from_uri("//Charlie//stash")
            self.account.add_from_uri("//Dave")
            self.account.add_from_uri("//Dave//stash")
            self.account.add_from_uri("//Eve")
            self.account.add_from_uri("//Eve//stash")
            self.account.add_from_uri("//Ferdie")
            self.account.add_from_uri("//Ferdie//stash")


    @property
    def installed_modules(self) -> Dict[str, Module]:
        return self._installed_modules

    @property
    def rpc_methods(self) -> RPCMethods:
        return self._provider.make_request("rpc_methods", [])
