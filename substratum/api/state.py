from typing import (
    Any,
)

from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    BlockHash,
    HexStr,
    Metadata,
)
from substratum.utils import (
    decode_metadata,
)

from .module import (
    Module,
)

SYSTEM_EVENTS_STORAGE_HASH: HexStr = \
    "0xcc956bdb7605e3547539f321ac2bc95c"
#V9:    "0x26aa394eea5630e07c48ae0c9558cef780d41e5e16056765bc8461851072c9d7"


class State(Module):
    _provider: BaseProvider

    def getMetadata(self, block_hash: BlockHash) -> Metadata:
        raw_metadata = self._provider.make_request("state_getMetadata", [block_hash])
        return decode_metadata(raw_metadata)

    def getStorageAt(self, storage_key: HexStr, block_hash: BlockHash) -> Any:
        # TODO Decode storage using metadata
        return self._provider.make_request("state_getStorageAt", [storage_key, block_hash])

    def getBlockEvents(self, block_hash: BlockHash) -> Any:
        return self.getStorageAt(SYSTEM_EVENTS_STORAGE_HASH, block_hash)
