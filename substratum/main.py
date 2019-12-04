from substratum.providers import (
    BaseProvider,
)
from substratum.api import (
    Chain,
    System,
)


class Substratum:
    def __init__(self, provider: BaseProvider) -> None:
        self.provider = provider
        self.chain = Chain(self.provider)
        self.system = System(self.provider)
