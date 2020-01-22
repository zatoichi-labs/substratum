from typing import (
    List,
)

from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    ChainProperties,
    Health,
    NetworkState,
    NodeRole,
    PeerInfo,
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

    @property
    def chain(self) -> str:
        return self._provider.make_request("system_chain", [])

    @property
    def health(self) -> Health:
        return self._provider.make_request("system_health", [])

    @property
    def networkState(self) -> NetworkState:
        return self._provider.make_request("system_networkState", [])

    @property
    def nodeRoles(self) -> List[NodeRole]:
        return self._provider.make_request("system_nodeRoles", [])

    @property
    def peers(self) -> List[PeerInfo]:
        return self._provider.make_request("system_peers", [])

    @property
    def properties(self) -> ChainProperties:
        return self._provider.make_request("system_properties", [])
