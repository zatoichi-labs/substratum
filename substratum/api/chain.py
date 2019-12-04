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


class Chain:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def getHead(self) -> BlockHash:
        return self.provider.make_request("chain_getHead", [])

    def getFinalisedHead(self) -> BlockHash:
        return self.provider.make_request("chain_getFinalisedHead", [])

    def getBlockHash(self, block_number: BlockNumber) -> BlockHash:
        return self.provider.make_request("chain_getBlockHash", [block_number])

    def getHeader(self, block_hash: BlockHash) -> BlockHeader:
        return self.provider.make_request("chain_getHeader", [block_hash])

    def getBlockNumber(self, block_hash: BlockHash) -> BlockNumber:
        return to_int(self.getHeader(block_hash)['number'])

    def getRuntimeVersion(self, block_hash: BlockHash) -> RuntimeVersion:
        return self.provider.make_request("chain_getRuntimeVersion", [block_hash])
