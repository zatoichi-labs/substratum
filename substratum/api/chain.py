from substratum.providers import (
    BaseProvider,
)


class Chain:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def getHead(self) -> str:
        return self.provider.make_request("chain_getHead", [])

    def getFinalisedHead(self) -> str:
        return self.provider.make_request("chain_getFinalisedHead", [])

    def getBlockHash(self, block_id):
        return self.provider.make_request("chain_getBlockHash", [block_id])

    def getHeader(self, block_hash):
        return self.provider.make_request("chain_getHeader", [block_hash])

    def getBlockNumber(self, block_hash):
        return self.getHeader(block_hash)['number']

    def getRuntimeVersion(self, block_hash):
        return self.provider.make_request("chain_getRuntimeVersion", [block_hash])
