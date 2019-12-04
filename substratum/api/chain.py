from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    Block,
    BlockHash,
    BlockHeader,
    BlockNumber,
    RuntimeVersion,
)
from substratum.utils import (
    to_int,
)

from .module import (
    Module,
)


class Chain(Module):
    _provider: BaseProvider

    def getHead(self) -> BlockHash:
        return self._provider.make_request("chain_getHead", [])

    def getFinalisedHead(self) -> BlockHash:
        return self._provider.make_request("chain_getFinalisedHead", [])

    def getBlockHash(self, block_number: BlockNumber) -> BlockHash:
        return self._provider.make_request("chain_getBlockHash", [block_number])

    def getHeader(self, block_hash: BlockHash) -> BlockHeader:
        return self._provider.make_request("chain_getHeader", [block_hash])

    def getBlockNumber(self, block_hash: BlockHash) -> BlockNumber:
        return to_int(self.getHeader(block_hash)['number'])

    def getBlock(self, block_hash: BlockHash) -> Block:
        return self._provider.make_request("chain_getBlock", [block_hash])

    def getRuntimeVersion(self, block_hash: BlockHash) -> RuntimeVersion:
        return self._provider.make_request("chain_getRuntimeVersion", [block_hash])
